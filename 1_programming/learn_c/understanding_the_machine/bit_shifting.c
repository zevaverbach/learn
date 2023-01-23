#include <stdio.h>

int main() {
    signed char num = 16;
    printf("size of %d (char): %lu\n", num, sizeof num);
    signed char exp = 5;
    signed char result = num << exp;
    printf("%d << %d == %d\n", num, exp, result);
    return 0;
}
