#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void process_input(const char *input) {
    char buf[16];
    strcpy(buf, input);                           // 🔸 Buffer overflow

    char *temp = malloc(32);
    if (!temp) return;
    strncpy(temp, input, 32);
    free(temp);
    strcpy(temp, "reuse");                        // 🔸 Use-after-free

    int *arr = malloc(sizeof(int) * 4);
    for (int i = 0; i <= 4; i++) {
        arr[i] = i * 2;                           // 🔸 Off-by-one error (heap overflow)
    }

    int a = -1;
    unsigned int b = 10;
    if (a < b) {                                  // 🔸 Signed/unsigned comparison bug
        printf("Comparison passed\n");
    }

    printf(input);                                // 🔸 Format string vulnerability
}

int main() {
    char user_input[100];
    fgets(user_input, sizeof(user_input), stdin);
    process_input(user_input);
    return 0;
}
