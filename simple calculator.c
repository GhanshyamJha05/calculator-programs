#include <stdio.h>

void add(float x, float y) {
    printf("%.2f + %.2f = %.2f\n", x, y, x + y);
}

void subtract(float x, float y) {
    printf("%.2f - %.2f = %.2f\n", x, y, x - y);
}

void multiply(float x, float y) {
    printf("%.2f * %.2f = %.2f\n", x, y, x * y);
}

void divide(float x, float y) {
    if (y == 0) {
        printf("Error! Division by zero.\n");
    } else {
        printf("%.2f / %.2f = %.2f\n", x, y, x / y);
    }
}

int main() {
    int choice;
    float num1, num2;

    do {
        printf("\nSelect operation:\n");
        printf("1. Add\n");
        printf("2. Subtract\n");
        printf("3. Multiply\n");
        printf("4. Divide\n");
        printf("5. Exit\n");

        printf("Enter choice (1/2/3/4/5): ");
        scanf("%d", &choice);

        if (choice >= 1 && choice <= 4) {
            printf("Enter first number: ");
            scanf("%f", &num1);
            printf("Enter second number: ");
            scanf("%f", &num2);
        }

        switch (choice) {
            case 1:
                add(num1, num2);
                break;
            case 2:
                subtract(num1, num2);
                break;
            case 3:
                multiply(num1, num2);
                break;
            case 4:
                divide(num1, num2);
                break;
            case 5:
                printf("Exiting the calculator.\n");
                break;
            default:
                printf("Invalid input. Please enter a number between 1 and 5.\n");
        }
    } while (choice != 5);

    return 0;
}
