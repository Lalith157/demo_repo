#include <stdio.h>
#include <string.h>
#include <sqlite3.h>

// 🚨 Vulnerable: Directly concatenating user input into SQL query
void login(const char *user, const char *password) {
    sqlite3 *db;
    sqlite3_stmt *res;
    char sql[256];

    // Open database
    if (sqlite3_open("test.db", &db) != SQLITE_OK) {
        printf("Cannot open database\n");
        return;
    }

    // 🚨 Vulnerable query building
    snprintf(sql, sizeof(sql),
             "SELECT * FROM users WHERE username='%s' AND password='%s';",
             user, password);

    printf("Executing query: %s\n", sql);

    // Execute SQL
    if (sqlite3_prepare_v2(db, sql, -1, &res, 0) == SQLITE_OK) {
        if (sqlite3_step(res) == SQLITE_ROW) {
            printf("Login successful!\n");
        } else {
            pr
