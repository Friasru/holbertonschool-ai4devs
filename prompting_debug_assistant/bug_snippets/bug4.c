#include <stdio.h>

int square(int x) {
    return x * x
}

int main(void) {
    int n = 5;
    int *p;
    *p = square(n);
    printf("Square: %d\n", *p);
    return 0;
}