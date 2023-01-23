#include <stdio.h>


int compared_to_8(int compare, int comparator) {
    return compare & comparator;
}

void test_some_numbers_at_particular_bits() {
    int thirteen = 0b1101;
    int eight = 0b1000;
    const size_t compare_quantity = 5;
    int to_compare[compare_quantity] = {thirteen, 11, 9, 7, 15};
    printf("\n\n");
    for (size_t i = 0; i < compare_quantity; ++i) {
        int masked_by_8 = compared_to_8(to_compare[i], eight);
        printf("%d (0x%x) masked by 8 is %d\n", to_compare[i], to_compare[i], masked_by_8);
        if (masked_by_8 == eight) {
            printf("therefore, %d has a 1 at position 3", to_compare[i]);
        } else {
            printf("therefore, %d does NOT have a 1 at position 3", to_compare[i]);
        }
        printf("\n\n");
    }
}

void count_to_a_million_with_odd_even() {
    // takes 4.4 seconds to run
    for (size_t i = 0; i < 1000000; ++i) {
        printf("your number is %zux in hexadecimal format, %zu in decimal,", i, i);
        int is_odd = i & 1;
        if (is_odd) {
            printf(" which is odd!\n");
        } else {
            printf(" which is even!\n");
        }
    }
}

void print_binary(int number, int num_digits) {
    int digit;
    for(digit = num_digits - 1; digit >= 0; digit--) {
        printf("%c", number & (1 << digit) ? '1' : '0');
    }
}

void module_n_counter() {
    // count to 31 a few times
    size_t num_nums = 0;
    const size_t STOP_AFTER_X_REPEATS = 3;
    size_t cntr = 0;
    size_t prev_cntr;
    size_t modulo_comparator = 31;
    const size_t STOP_AFTER_TOTAL = (modulo_comparator + 1) * STOP_AFTER_X_REPEATS;
    while (num_nums < STOP_AFTER_TOTAL) {
        num_nums += 1;
        printf("counter: %zu\n", cntr);
        prev_cntr = cntr;
        cntr = (cntr + 1) & modulo_comparator;
        if (cntr == 0) {
            printf("\n\n");
            printf("counter was reset to 0 because ");
            print_binary((prev_cntr + 1), 8);
            printf(" (%zu) & ", (prev_cntr + 1));
            print_binary(modulo_comparator, 8);
            printf(" (%zu) is ", modulo_comparator);
            print_binary(((prev_cntr + 1) & modulo_comparator), 8);
            printf(" (%zu)\n\n", ((prev_cntr + 1) & modulo_comparator));
        }
    }
}

void module_n_counter_experiments() {
    printf("%d & %d = %d\n", 35, 34, 35 & 34);
    print_binary(35, 8);
    printf(" & ");
    print_binary(34, 8);
    printf(" = ");
    print_binary(35 & 34, 8);
    printf("\n\n");
    printf("%d & %d = %d\n", 34, 33, 34 & 33);
    print_binary(34, 8);
    printf(" & ");
    print_binary(33, 8);
    printf(" = ");
    print_binary(34 & 33, 8);
    printf("\n\n");
    printf("%d & %d = %d\n", 33, 32, 33 & 32);
    print_binary(33, 8);
    printf(" & ");
    print_binary(32, 8);
    printf(" = ");
    print_binary(33 & 32, 8);
    printf("\n\n");
    printf("%d & %d = %d\n", 32, 31, 32 & 31);
    print_binary(32, 8);
    printf(" & ");
    print_binary(31, 8);
    printf(" = ");
    print_binary(32 & 31, 8);
    printf("\n\n");
    printf("%d & %d = %d\n", 31, 30, 31 & 30);
    print_binary(31, 8);
    printf(" & ");
    print_binary(30, 8);
    printf(" = ");
    print_binary(31 & 30, 8);
    printf("\n\n");
    printf("%d & %d = %d\n", 30, 29, 30 & 29);
    print_binary(30, 8);
    printf(" & ");
    print_binary(29, 8);
    printf(" = ");
    print_binary(30 & 29, 8);
    printf("\n\n");
    printf("%d & %d = %d\n", 29, 28, 29 & 28);
    print_binary(29, 8);
    printf(" & ");
    print_binary(28, 8);
    printf(" = ");
    print_binary(29 & 28, 8);
    printf("\n\n");
    printf("%d & %d = %d\n", 16, 15, 16 & 15);
    print_binary(16, 8);
    printf(" & ");
    print_binary(15, 8);
    printf(" = ");
    print_binary(16 & 15, 8);
    printf("\n\n");
    printf("%d & %d = %d\n", 64, 63, 64 & 63);
    print_binary(64, 8);
    printf(" & ");
    print_binary(63, 8);
    printf(" = ");
    print_binary(64 & 63, 8);
    printf("\n\n");
    printf("%d & %d = %d\n", 16, 15, 16 & 15);
    print_binary(16, 8);
    printf(" & ");
    print_binary(15, 8);
    printf(" = ");
    print_binary(16 & 15, 8);
    printf("\n\n");
}

int main(int argc, char **argv) {
    // count_to_a_million_with_odd_even();
    // test_some_numbers_at_particular_bits();
    // module_n_counter();
    module_n_counter_experiments();
    return 0;
}


