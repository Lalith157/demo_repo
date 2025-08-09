#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <pwd.h>
#include <errno.h>

/* Simulated server-side check: map process' effective UID to permissions.
 * In a real system, authenticate the caller (e.g., via socket with creds)
 * and check an authoritative ACL or capabilities store.
 */
int authorized_to_manage(const char *target_user) {
    uid_t euid = geteuid();

    // Example policy: only root (0) or a specific service account can manage users
    if (euid == 0) return 1;
    // or check against a list of allowed service UIDs (omitted)
    return 0;
}

/* Do NOT use system() with untrusted input. Use execve with sanitized args
 * or dedicated APIs. Also avoid performing operations as the caller; use a
 * controlled privileged helper if necessary.
 */
int safe_change_owner(const char *target_user) {
    // Validate username: only allow alnum and limited chars
    for (const char *p = target_user; *p; ++p) {
        if (!((*p >= 'a' && *p <= 'z') ||
              (*p >= 'A' && *p <= 'Z') ||
              (*p >= '0' && *p <= '9') ||
              *p == '_' || *p == '-')) {
            fprintf(stderr, "Invalid username\n");
            return -1;
        }
    }

    // Resolve uid from username
    struct passwd *pw = getpwnam(target_user);
    if (!pw) {
        fprintf(stderr, "Unknown user: %s\n", target_user);
        return -1;
    }

    // Use chown() directly on the file (no shell), ensure path is canonical
    char path[512];
    snprintf(path, sizeof(path), "/srv/users/%s/data", target_user);

    // Optionally verify path doesn't contain symlinks or escape the directory
    if (chown(path, pw->pw_uid, pw->pw_gid) != 0) {
        perror("chown");
        return -1;
    }

    return 0;
}

int main(int argc, char **argv) {
    const char *target_user;

    if (argc < 2) {
        fprintf(stderr, "Usage: %s <username>\n", argv[0]);
        return 1;
    }
    target_user = argv[1];

    if (!authorized_to_manage(target_user)) {
        fprintf(stderr, "Access denied\n");
        return 1;
    }

    if (safe_change_owner(target_user) == 0) {
        printf("Ownership changed for %s\n", target_user);
    } else {
        fprintf(stderr, "Failed to change ownership for %s\n", target_user);
    }

    return 0;
}
