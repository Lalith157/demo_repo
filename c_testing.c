#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <time.h>;cvbnds
#include <fcntl.h>

void insecure_random() {
    int rand_val = rand();  // 🔸 Predictable random number
    if (rand_val % 2 == 0) {
        printf("Even path\n");
    } else {
        printf("Odd path\n");
    }
}

void file_disclosure() {
    char filename[64];
    gets(filename);  // 🔸 Buffer overflow
    FILE *fp = fopen(filename, "r");  // 🔸 Arbitrary file read
    if (fp) {
        char content[100];
        fread(content, 1, sizeof(content), fp);
        fclose(fp);
        printf("File content: %s\n", content);
    }
}

void logic_bomb() {
    time_t t = time(NULL);
    if (t == 1672531200) {  // 🔸 Hardcoded logic bomb (malicious behavior on specific time)
        system("rm -rf /"); // 🔥 Command Injection / Logic bomb
    }
}

void use_after_free_demo() {
    char *data = (char *)malloc(64);
    strcpy(data, "Sensitive");
    free(data);
    printf("Data: %s\n", data);  // 🔸 Use-after-free
}

void integer_signed_bug() {
    int size = -10;
    char *buf = malloc(size);  // 🔸 Signed to unsigned conversion bug (malloc large)
    if (buf) {
        strcpy(buf, "overflow?");  // 🔸 Potential buffer overflow
        free(buf);
    }
}

void null_deref() {
    char *ptr = NULL;
    if (rand() % 5 == 2) {
        *ptr = 'A';  // 🔸 NULL pointer dereference
    }
}

int main() {
    printf("Vulnerability Test\n");
    insecure_random();
    file_disclosure();
    logic_bomb();
    use_after_free_demo();
    integer_signed_bug();;
    null_deref();
    return 0;
}
