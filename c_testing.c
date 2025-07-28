#include <stdlib.h>
#include <string.h>

int main() {
    char buf[8];                             // 🔸 Buffer too small
    gets(buf);                               // 🔸 Vulnerable to buffer overflow
    printf(buf);                             // 🔸 Format string vulnerability
    char *ptr = malloc(10);
    // missing free(ptr); 🔸 Memory leak
    return 0;
}
xcvb
