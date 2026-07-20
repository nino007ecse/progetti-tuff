#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <curl/curl.h>
#include <unistd.h>

int main() {
    char webhooks[10][2048];  // Support up to 10 webhooks
    int num_webhooks = 0;
    char message[4096];
    int delay_ms = 0;
    int count = 0;

    printf("Enter the webhook(s) links (one per line, empty line to finish):\n");
    while (num_webhooks < 10) {
        fgets(webhooks[num_webhooks], sizeof(webhooks[0]), stdin);
        webhooks[num_webhooks][strcspn(webhooks[num_webhooks], "\n")] = 0;
        if (strlen(webhooks[num_webhooks]) == 0) break;
        num_webhooks++;
    }

    printf("Enter the message to spam:\n");
    fgets(message, sizeof(message), stdin);
    message[strcspn(message, "\n")] = 0;

    printf("Enter delay between messages in ms (0 for no delay): ");
    scanf("%d", &delay_ms);
    printf("Enter number of times to spam (0 for infinite): ");
    scanf("%d", &count);

    CURL *curl;
    curl_global_init(CURL_GLOBAL_ALL);
    curl = curl_easy_init();

    if (curl) {
        int i = 0;
        while (count == 0 || i < count) {
            for (int w = 0; w < num_webhooks; w++) {
                char json[8192];
                snprintf(json, sizeof(json), "{\"content\":\"%s\"}", message);

                curl_easy_setopt(curl, CURLOPT_URL, webhooks[w]);
                curl_easy_setopt(curl, CURLOPT_POSTFIELDS, json);
                curl_easy_setopt(curl, CURLOPT_HTTPHEADER, curl_slist_append(NULL, "Content-Type: application/json"));

                CURLcode res = curl_easy_perform(curl);
                if (res != CURLE_OK) {
                    fprintf(stderr, "Error: %s\n", curl_easy_strerror(res));
                } else {
                    printf("Sent to %s\n", webhooks[w]);
                }
            }
            i++;
            if (delay_ms > 0) usleep(delay_ms * 1000);
        }
        curl_easy_cleanup(curl);
    }

    curl_global_cleanup();
    return 0;
}
