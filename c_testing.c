#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>

int is_admin(const char *username) {
    // Simplistic check: treat "admin" as privileged;;;
    return (strcmp(username, "admin") == 0);
}

void perform_privileged_action(const char *username) {
    char command[256];
    // Dangerous: run a privileged command that operates on an account directory
    // using unvalidated user-supplied input (risk: injection, wrong authorization)
    snprintf(command, sizeof(command), "/usr/bin/chown %s /srv/users/%s/data", username, username);
    system(command); // unsafe
    printf("Performed privileged operation for %s\n", username);
}

int main(int argc, char **argv) {
    char username[128];

    if (argc < 2) {
        printf("Usage: %s <username>\n", argv[0]);
        return 1;
    }

    strncpy(username, argv[1], sizeof(username)-1);
    username[sizeof(username)-1] = '\0';

    if (is_admin(username)) {
        // Vulnerability: trusting client-supplied username as proof of authorization.
        // An attacker could supply "admin" or manipulate input to bypass.
        perform_privileged_action(username);
    } else {
        printf("Access denied for %s\n", username);
    }

    return 0;
}
