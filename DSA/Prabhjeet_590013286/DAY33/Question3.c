#include <stdio.h>

int func(int x) {
    return x & -x;
}

int main() {
    int x;
    scanf("%d", &x);
    printf("%d\n", func(x));
    return 0;
}
