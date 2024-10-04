#include <stdio.h>
#include <math.h>

void add(double x, double y) {
    printf("%.2f + %.2f = %.2f\n", x, y, x + y);
}

void subtract(double x, double y) {
    printf("%.2f - %.2f = %.2f\n", x, y, x - y);
}

void multiply(double x, double y) {
    printf("%.2f * %.2f = %.2f\n", x, y, x * y);
}

void divide(double x, double y) {
    if (y == 0) {
        printf("Error! Division by zero.\n");
    } else {
        printf("%.2f / %.2f = %.2f\n", x, y, x / y);
    }
}

void power(double base, double exp) {
    printf("%.2f ^ %.2f = %.2f\n", base, exp, pow(base, exp));
}

void square_root(double x) {
    if (x < 0) {
        printf("Error! Square root of negative number.\n");
    } else {
        printf("sqrt(%.2f) = %.2f\n", x, sqrt(x));
    }
}

void sine(double angle) {
    printf("sin(%.2f degrees) = %.2f\n", angle, sin(angle * M_PI / 180));
}

void cosine(double angle) {
    printf("cos(%.2f degrees) = %.2f\n", angle, cos(angle * M_PI / 180));
}

void tangent(double angle) {
    printf("tan(%.2f degrees) = %.2f\n", angle, tan(angle * M_PI / 180));
}

int main() {
    int choice;
    double num1, num2;

    do {
        printf("\nSelect operation:\n");
        printf("1. Add\n");
        printf("2. Subtract\n");
        printf("3. Multiply\n");
        printf("4. Divide\n");
        printf("5. Power\n");
        printf("6. Square Root\n");
        printf("7. Sine\n");
        printf("8. Cosine\n");
        printf("9. Tangent\n");
        printf("10. Exit\n");

        printf("Enter choice (1-10): ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                printf("Enter first number: ");
                scanf("%lf", &num1);
                printf("Enter second number: ");
                scanf("%lf", &num2);
                add(num1, num2);
                break;
            case 2:
                printf("Enter first number: ");
                scanf("%lf", &num1);
                printf("Enter second number: ");
                scanf("%lf", &num2);
                subtract(num1, num2);
                break;
            case 3:
                printf("Enter first number: ");
                scanf("%lf", &num1);
                printf("Enter second number: ");
                scanf("%lf", &num2);
                multiply(num1, num2);
                break;
            case 4:
                printf("Enter first number: ");
                scanf("%lf", &num1);
                printf("Enter second number: ");
                scanf("%lf", &num2);
                divide(num1, num2);
                break;
            case 5:
                printf("Enter base: ");
                scanf("%lf", &num1);
                printf("Enter exponent: ");
                scanf("%lf", &num2);
                power(num1, num2);
                break;
            case 6:
                printf("Enter number: ");
                scanf("%lf", &num1);
                square_root(num1);
                break;
            case 7:
            case 8:
            case 9:
                printf("Enter angle in degrees: ");
                scanf("%lf", &num1);
                if (choice == 7)
                    sine(num1);
                else if (choice == 8)
                    cosine(num1);
                else
                    tangent(num1);
                break;
            case 10:
                printf("Exiting the calculator.\n");
                break;
            default:
                printf("Invalid input. Please enter a number between 1 and 10.\n");
        }
    } while (choice != 10);

    return 0;
}
