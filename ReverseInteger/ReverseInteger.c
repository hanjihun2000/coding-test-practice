#include <math.h>

int reverse(int x) {
    int reverse = 0;
    int i = x;
    int P = 0;
    while (i != 0) {
        i = i / 10;
        P++;
    };
    while (x != 0) {
        int y = x % 10;
        if (y * pow(10, (P - 1)) < -2147483648 || y * pow(10, (P - 1)) > 2147483647) {
            return 0;
        };
        if (reverse + y * pow(10, (P - 1)) < -2147483648 || reverse + y * pow(10, (P - 1)) > 2147483647) {
            return 0;
        };
        reverse = reverse + y * ((int)pow(10, (P--) - 1));
        x = x / 10;
    };
    return reverse;
}
