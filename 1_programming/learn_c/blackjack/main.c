#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
#include <stdarg.h>


char cards[][2] = {"2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"};

void deal(uint32_t* player_card_1, uint32_t* player_card_2, uint32_t* dealer_card_1, uint32_t* dealer_card_2) {
    *player_card_1 = arc4random_uniform(13 + 1);
    *player_card_2 = arc4random_uniform(13 + 1);
    *dealer_card_1 = arc4random_uniform(13 + 1);
    *dealer_card_2 = arc4random_uniform(13 + 1);
}

int get_card_value(uint32_t card) {
    switch (card) {
        case 0:
            return 2;
        case 1:
            return 3;
        case 2:
            return 4;
        case 3:
            return 5;
        case 4:
            return 6;
        case 5:
            return 7;
        case 6:
            return 8;
        case 7:
            return 9;
        case 8:
            return 10;
        case 9:
            return 10;
        case 10:
            return 10;
        case 11:
            return 10;
        case 12:
            return 100;
        default:
            printf("invalid card");
            return 0;
    }
}

int get_hand_value(size_t count, ...) {
    // TODO: this has to handle arbitrary numbers of cards
    size_t possible_values[3];
    va_list arg_list;:
    size_t card_1_val = get_card_value(card_1);
    size_t card_2_val = get_card_value(card_2);
    return card_1_val + card_2_val;
}

size_t play() {
    size_t result;
    uint32_t player_card_1, player_card_2, dealer_card_1, dealer_card_2;
    deal(&player_card_1, &player_card_2, &dealer_card_1, &dealer_card_2);
    printf("your hand:\n '%s' '%s'\n", cards[player_card_1], cards[player_card_2]);
    printf("dealer shows '%s'\n", cards[dealer_card_1]);
    int hand_value = get_hand_value(2, player_card_1, player_card_2);
    if (hand_value != 21) {
        char action;
        printf("do you want to hit [h] or stay [s]\n > ?");
        scanf("%s", &action);
    }


    return result;
}

void lowercase(char word[]) {
    for (size_t i = 1; word[i]; i++) {
        word[i] = tolower(word[i]);
    }
}

int main(int argc, char *argv[]) {
    printf("Welcome to the blackjack table! Let's get started, eh?\n\n");
    size_t funds = 200;
    size_t quit = 0;
    size_t bet;
    size_t result;
    while (funds != 0 && quit == 0) {
        printf("How much do you want to bet (you have $%zu) > ", funds);
        scanf("%zu", &bet);
        if (bet > funds) {
            printf("Sorry, you don't have enough to support that bet!");
            continue;
        }

        result = play();
        if (result == 0) {
            funds -= bet;
        } else if (result == -1) {
            quit = 1;
        } else {
            funds += bet;
        }

        char lets_continue[3];
        printf("Do you want to play again? [yes]");
        scanf("%s", lets_continue);
        lowercase(lets_continue);
        if (strcmp(lets_continue, "") || strcmp(lets_continue, "y") || strcmp(lets_continue, "yes")) {
            printf("Okay, next round:\n");
        } else {
            quit = 1;
        }
        if (funds == 0) printf("You're out of funds!\n");
        printf("See you next time.\n");
        return 0;
    }
}
