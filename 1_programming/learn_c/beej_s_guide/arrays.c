#include <stdio.h>


int main() {
    int nums[] = {1, 3, 5, 7};
    int *p = nums;
    printf("*p = %d\n", *p);
    printf("*(p + 1) = %d\n", *(p + 1));
    printf("*(p + 2) = %d\n", *(p + 2));
    return 0;
}
