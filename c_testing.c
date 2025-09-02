#include <stdio.h>
#include <string.h>
#include <sqlite3.h>

  // 🚨 Vulnerable query building
    snprintf(sql, sizeof(sql),
             "SELECT * FROM users WHERE username='%s' AND password='%s';",
             user, password);

    printf("Executing query: %s\n", sql);

    // Execute SQL
    if (sqlite3_prepare_v2(db, sql, -1, &res, 0) == SQLITE_OK) {
        if (sqlite3_step(res) == SQLITE_ROW) {
            printf("Login successful!\n");
        } else 
            return;
    }
