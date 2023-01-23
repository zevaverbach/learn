#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <errno.h>
#include <assert.h>

#include <termios.h>

#include <unistd.h>

#define EDITOR_CAPACITY (10*1024)
#define return_defer(value) do { result = (value); goto defer; } while(0)


typedef struct {
    size_t begin;
    size_t end;
} Line;

typedef struct {
    Line *items;
    size_t count;
    size_t capacity;
} Lines;

typedef struct {
    char *items;
    size_t count;
    size_t capacity;
} Data;

typedef struct {
    Data data;
    Lines lines;
    size_t cursor;
} Editor;

#define ITEMS_INIT_CAPACITY (10*1024)

#define dynamic_array_append(da, item) do {                                        \
    if ((da)->count >= (da)->capacity) {                                           \
        (da)->capacity = (da)->capacity == 0                                       \
            ? ITEMS_INIT_CAPACITY                                                  \
            : (da)->capacity * 2;                                                  \
        (da)->items = realloc((da)->items, (da)->capacity * sizeof(*(da)->items)); \
        assert(                                                                    \
            (da)->items != NULL                                                    \
            &&                                                                     \
            "ran out of RAM while trying to allocate more memory to do "           \
            "`editor_push_char`"                                                   \
        );                                                                         \
    }                                                                              \
    (da)->items[(da)->count++] = (item);                                           \
} while (0)

#define dynamic_array_reserve(da, desired_capacity) do { \
    if ((da)->capacity < desired_capacity {                                                \
        (da)->capacity = desired_capacity;                                                 \
        (da)->items = realloc((da)->items, (da)->capacity * sizeof(*(da)->items)); \
    }                                                                              \
} while (0)

void editor_compute_lines(Editor *e) {
    e->lines.count = 0;
    size_t begin = 0;
    for (size_t i = 0; i < e->data.count; ++i) {
        if (e->data.items[i] == '\n') {
            dynamic_array_append(&e->lines, ((Line){.begin = begin, .end = i}));
            begin = i + 1;
        }
    }
    dynamic_array_append(&e->lines, ((Line){.begin = begin, .end = e->data.count}));
}

void editor_insert_char(Editor *e, char x) {
    if (e->data.count < EDITOR_CAPACITY) {
        dynamic_array_append(&e->data, '\0');
        memmove(
            &e->data.items[e->cursor + 1], 
            &e->data.items[e->cursor],
            e->data.count - 1 - e->cursor
        );
        e->data.items[e->cursor] = x;
        e->cursor += 1;
        editor_compute_lines(e);
    }
}

size_t editor_current_line(const Editor *e) {
    assert(e->cursor <= e->data.count);
    Line line;
    for (size_t i = 0; i < e->lines.count; ++i) {
        line = e->lines.items[i];
        if (
            line.begin <= e->cursor 
            && 
            e->cursor <= line.end
        ) return i;
    }
    return 0;
}

void editor_rerender(const Editor *e) {
    printf("\033[2J\033[H"); // clear screen and go to 0, 0
    fwrite(e->data.items, sizeof(*e->data.items), e->data.count, stdout);
    size_t line = editor_current_line(e);
    // position the cursor
    printf(
        "\033[%zu;%zuH", // '%zu' is a specifier for a `size_t`
        line + 1, 
        e->cursor - e->lines.items[line].begin + 1
    );
}

int editor_start_interactive(Editor *e, const char * filepath) {
    if (!isatty(0)) {
        fprintf(stderr, "Please run in the terminal!\n");
        return 1;
    }

    struct termios term; // stores the state of the terminal
    if (tcgetattr(0, &term)) {
        fprintf(
            stderr, 
            "ERROR: could not save the state of the terminal: %s\n", 
            strerror(errno)
        );
        return 1;
    }

    term.c_lflag = term.c_lflag & ~ECHO; // equivalent of &= ~ECHO
    term.c_lflag = term.c_lflag & ~ICANON;

    if (tcsetattr(0, 0, &term)) {
        fprintf(
            stderr, 
            "ERROR: could not update the state of the terminal: %s\n", 
            strerror(errno)
        );
        return 1;
    }

    bool quit = false;
    bool insert = false;

    while (!quit && !feof(stdin)) {
        editor_rerender(e);
        if (insert) {
            int i = fgetc(stdin);
            switch (i) {
                case 27: {
                    insert = false;
                    FILE *f = fopen(filepath, "wb");
                    fwrite(e->data.items, sizeof(*e->data.items), e->data.count, f);
                } break;
                default: {
                    editor_insert_char(e, i);
                }
            }
        } else {
            int x = fgetc(stdin);
            switch (x) {
                case 'i': {
                    insert = true;
                } break;
                case 'q': {
                    quit = true;
                } break;
                case 'h': {
                    if (e->cursor > 0) {
                        e->cursor = e->cursor - 1;
                    }
                } break;
                case 'l': {
                    if (e->cursor < e->data.count - 1) {
                        e->cursor += 1;
                    }
                } break;
                case 'j': {
                    size_t current_line = editor_current_line(e);
                    if (current_line < e->lines.count - 1) {
                        size_t current_col = e->cursor - e->lines.items[current_line].begin;
                        e->cursor = e->lines.items[current_line + 1].begin + current_col;
                        if (e->cursor > e->lines.items[current_line + 1].end) {
                            e->cursor = e->lines.items[current_line + 1].end;
                        }
                    }
                } break;
                case 'k': {
                    size_t current_line = editor_current_line(e);
                    if (current_line > 0) {
                        size_t current_col = e->cursor - e->lines.items[current_line].begin;
                        e->cursor = e->lines.items[current_line - 1].begin + current_col;
                        if (e->cursor > e->lines.items[current_line - 1].end) {
                            e->cursor = e->lines.items[current_line - 1].end;
                        }
                    }
                } break;
            }
        }
    }

    printf("\033[2J");

    term.c_lflag |= ECHO;
    tcsetattr(0, 0, &term);
    return 0;

}

int get_file_size(FILE *f, size_t *out) {
    long saved_position = ftell(f);

    if (saved_position < 0) return errno;
    if (fseek(f, 0, SEEK_END)) return errno;

    long size = ftell(f);

    if (size < 0) return errno;
    if (fseek(f, saved_position, SEEK_SET) < 0) return errno;

    *out = (size_t) size;
    return 0;
}

static Editor editor;

int main(int num_args, char **args) {
    if (num_args < 2) {
        fprintf(stderr, "Usage: zed <input.txt>\n");
        fprintf(stderr, "ERROR: no input file was provided\n");
        return_defer(1);
    }

    const char *file_path = args[1];
    FILE *f = fopen(file_path, "rb");
    if (f == NULL) {
        fprintf(
            stderr, 
            "ERROR: could not open file %s: %s\n", 
            file_path, 
            strerror(errno)
        );
        return 1;
    }

    assert(0 && "TODO: reading the file has to be completely rewritten to accommodate dynamic memory");
    size_t file_size;
    int err = get_file_size(f, &file_size);
    if (err != 0) {
        fprintf(stderr, "ERROR: could not determine file size %s: %s\n", file_path, strerror(errno));
        return_defer(1);
    }
    dynamic_array_reserve(&editor.data, file_size);
    // load contents of file into `editor.data.items`
    // assign length of file to `editor.data.count`
    editor.data.count = fread(
        editor.data.items, 
        sizeof(*editor.data.items), 
        EDITOR_CAPACITY, 
        f
    );

    fclose(f);
    editor_compute_lines(&editor);

    return editor_start_interactive(&editor, file_path);
    return 0;
}
