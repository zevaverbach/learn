#include <stdio.h>

struct Date {
    unsigned month :4;
    unsigned day :5;
    unsigned year :16;
};

void print_byte_by_byte(void *pnt0, size_t size)
{
    unsigned char *pnt = pnt0;
    while (size--) {
        printf("%02x ", *pnt++);
    }
}


int main() {
    struct Date my_date;
    my_date.year = 2023;
    my_date.month = 1;
    my_date.day = 17;
    printf("the following is the binary for the date %d/%d/%d:\n\n", my_date.month, my_date.day, my_date.year);
    print_byte_by_byte(&my_date, 32);
    printf("\n");
    return 0;
}
