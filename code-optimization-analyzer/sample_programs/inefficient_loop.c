#include <stdio.h>

int main() {

    int a[10], b[10], c[10];

    for(int i = 0; i < 10; i++) {
        c[i] = a[i] + b[i];
    }

    return 0;
}