#include <stdio.h>

int main() {
    int size, target, count = 0;

    printf("Enter the size of the array: ");
    scanf("%d", &size);

    int arr[size];

    printf("Enter %d elements:\n", size);
    for(int i = 0; i < size; i++) {
        scanf("%d", &arr[i]);
    }

    printf("Enter the target element to count: ");
    scanf("%d", &target);

    for(int i = 0; i < size; i++) {
        if(arr[i] == target) {
            count++;
        }
    }

    printf("%d\n", count);

    return 0;
}
