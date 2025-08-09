#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <curl/curl.h>

// Callback function to handle response data...
size_t write_callback(void *contents, size_t size, size_t nmemb, void *userp) {
    size_t realsize = size * nmemb;
    printf("%.*s", (int)realsize, (char *)contents);
    return realsize;
}

int main(void) {
    CURL *curl;
    CURLcode res;
    char url[256];

    // Get URL from user input (vulnerable point)
    printf("Enter URL to fetch: ");
    fgets(url, sizeof(url), stdin);

    // Remove trailing newline
    url[strcspn(url, "\n")] = 0;

    // Initialize libcurl
    curl = curl_easy_init();
    if (curl) {
        // Set the URL to fetch (directly using user input)
        curl_easy_setopt(curl, CURLOPT_URL, url);
        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, write_callback);

        // Perform the request
        res = curl_easy_perform(curl);
        if (res != CURLE_OK) {
            fprintf(stderr, "curl_easy_perform() failed: %s\n", curl_easy_strerror(res));
        }

        // Cleanup
        curl_easy_cleanup(curl);
    } else {
        fprintf(stderr, "Failed to initialize curl\n");
    }

    return 0;
}
