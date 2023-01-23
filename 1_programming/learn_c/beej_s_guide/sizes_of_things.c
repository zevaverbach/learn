#include <stdio.h>

int main() {
    printf("the size of an int is %zu,\n", sizeof(int));
    printf("where as the size of a size_t is %zu.\n", sizeof(size_t));
    printf("then, the size of a long is %lu", sizeof(long));
    printf("and the size of a double is %lu\n", sizeof(double));
    return 0;
}
