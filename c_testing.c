#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    char input[10];
    gets(input);                            // 🔸 Buffer overflow
    printf(input);                          // 🔸 Format string vulnerability
    char *data = malloc(20);
    strcpy(data, input);                    // 🔸 Potential buffer overflow
    return 0;
}
