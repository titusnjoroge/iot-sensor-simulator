#include <stdio.h>
#include <stdlib.h>
#include <time.h>

float read_temperature() {
    return (rand() % 350) / 10.0;
}

float read_humidity() {
    return (rand() % 800) / 10.0;
}

int main() {
    srand(time(NULL));

    for (int i = 0; i < 10; i++) {
        float temp = read_temperature();
        float hum = read_humidity();

        printf("{\"temp\": %.2f, \"humidity\": %.2f}\n", temp, hum);
    }

    return 0;
}