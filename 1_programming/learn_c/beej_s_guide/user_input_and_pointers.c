#include <stdio.h>

int main() {
    int i;
    printf("give me a number: ");
    scanf("%d", &i);
    printf("\nokay, you input %d\n", i);
    int *p;
    printf("sizeof p is %zu, whereas ", sizeof p);
    printf("sizeof *p is %zu.\n", sizeof *p);
    return 0;
}
