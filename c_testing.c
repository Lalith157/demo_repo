#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <limits.h>
#include <time.h> // For predictable random number
#include <pthread.h> // For race condition

// Global variable for hardcoded credentials
char *GLOBAL_PASSWORD = "adminpassword123"; // Hardcoded credentials

// Global variable for race condition example
int shared_resource = 0;

// Function for race condition thread
void *increment_shared_resource(void *arg) {
    for (int i = 0; i < 100000; i++) {
        shared_resource++;
    }
    return NULL;
}

int main(int argc, char *argv[]) {
    // 1. Buffer overflow (using gets - highly insecure)
    char buffer[10];
    printf("Enter some text: ");
    gets(buffer); // Vulnerability: Buffer overflow (gets does not check buffer size)

    // 2. Command injection
    char user_input_cmd[100];
    printf("Enter a command: ");
    fgets(user_input_cmd, sizeof(user_input_cmd), stdin);
    user_input_cmd[strcspn(user_input_cmd, "\n")] = 0; // Remove newline
    system(user_input_cmd); // Vulnerability: Command injection (executes user-controlled input directly)

    // 3. Format string vulnerability
    char format_input[100];
    printf("Enter a format string: ");
    fgets(format_input, sizeof(format_input), stdin);
    printf(format_input); // Vulnerability: Format string vulnerability (user-controlled format string)

    // 5. Integer overflow
    short s_val = 32767;
    s_val++; // Vulnerability: Integer overflow (short max is 32767, incrementing overflows)
    printf("\nInteger overflow example: %d\n", s_val);

    // 6. Integer underflow
    int i_val = INT_MIN;
    i_val--; // Vulnerability: Integer underflow (int min is -2147483648, decrementing underflows)
    printf("Integer underflow example: %d\n", i_val);

    // 7. Memory leak
    char *leak_ptr = (char *)malloc(100); // Vulnerability: Memory leak (allocated memory is never freed)
    if (leak_ptr == NULL) {
        perror("malloc failed");
        return 1;
    }
    strcpy(leak_ptr, "This memory will leak.");

    // 8. Null pointer dereference
    int *null_ptr = NULL;
    // *null_ptr = 10; // Vulnerability: Null pointer dereference (commented out to allow program to run)
    // printf("Null pointer dereference example: %d\n", *null_ptr);

    // 9. Off-by-one error
    int arr[5];
    for (int i = 0; i <= 5; i++) { // Vulnerability: Off-by-one error (accesses arr[5] which is out of bounds)
        // arr[i] = i; // Commented out to prevent crash, but the logic is flawed
    }
    printf("Off-by-one error example (loop goes out of bounds).\n");

    // 10. Predictable random number
    srand(time(NULL)); // Vulnerability: Predictable random number (seeded with time, easily guessable)
    int random_num = rand();
    printf("Predictable random number: %d\n", random_num);

    // 11. Race condition
    pthread_t thread1, thread2;
    pthread_create(&thread1, NULL, increment_shared_resource, NULL);
    pthread_create(&thread2, NULL, increment_shared_resource, NULL);
    pthread_join(thread1, NULL);
    pthread_join(thread2, NULL);
    printf("Race condition result (shared_resource): %d (expected 200000, but might be less due to race)\n", shared_resource); // Vulnerability: Race condition (shared_resource accessed by multiple threads without synchronization)

    // 12. Signed/unsigned comparison bug
    unsigned int u_val = 5;
    int s_val_neg = -1;
    if (s_val_neg < u_val) { // This comparison might behave unexpectedly due to type promotion
        printf("Signed/unsigned comparison: -1 is less than 5 (as signed).\n");
    } else {
        printf("Signed/unsigned comparison: -1 is greater than 5 (as unsigned).\n"); // Vulnerability: Signed/unsigned comparison bug (s_val_neg promoted to unsigned, becoming a large positive number)
    }

    // 13. Type confusion
    void *raw_ptr = malloc(sizeof(int));
    if (raw_ptr == NULL) {
        perror("malloc failed");
        return 1;
    }
    *((float *)raw_ptr) = 3.14f; // Storing a float in memory intended for int
    int confused_int = *((int *)raw_ptr); // Vulnerability: Type confusion (interpreting float bits as int)
    printf("Type confusion example: %f (float) interpreted as %d (int)\n", 3.14f, confused_int);
    free(raw_ptr);

    // 14. Uninitialized variable
    int uninitialized_var;
    // printf("Uninitialized variable: %d\n", uninitialized_var); // Vulnerability: Uninitialized variable (accessing uninitialized memory)

    // 15. Use-after-free
    int *uaf_ptr = (int *)malloc(sizeof(int));
    if (uaf_ptr == NULL) {
        perror("malloc failed");
        return 1;
    }
    *uaf_ptr = 100;
    free(uaf_ptr);
    // printf("Use-after-free: %d\n", *uaf_ptr); // Vulnerability: Use-after-free (accessing freed memory)
    // *uaf_ptr = 200; // Double free or use-after-free write

    // Clean up memory leak example (though in a real scenario, it would be a leak)
    // free(leak_ptr); // If this line is uncommented, the memory leak is fixed.

    return 0;
}
