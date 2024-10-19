#include <stdio.h>

int main() {
    char operator;
    double num1, num2, result;

    // Display a menu for the user
    printf("Simple Calculator\n");
    printf("Select an operation:\n");
    printf(" +  : Addition\n");
    printf(" -  : Subtraction\n");
    printf(" *  : Multiplication\n");
    printf(" /  : Division\n");
    printf("Enter your choice: ");
    scanf(" %c", &operator); // Read the operator

    // Read the two numbers
    printf("Enter two numbers: ");
    scanf("%lf %lf", &num1, &num2);

    // Perform the selected operation
    switch (operator) {
        case '+':
            result = num1 + num2;
            printf("%.2lf + %.2lf = %.2lf\n", num1, num2, result);
            break;
        case '-':
            result = num1 - num2;
            printf("%.2lf - %.2lf = %.2lf\n", num1, num2, result);
            break;
        case '*':
            result = num1 * num2;
            printf("%.2lf * %.2lf = %.2lf\n", num1, num2, result);
            break;
        case '/':
            // Check for division by zero
            if (num2 != 0) {
                result = num1 / num2;
                printf("%.2lf / %.2lf = %.2lf\n", num1, num2, result);
            } else {
                printf("Error: Division by zero is undefined.\n");
            }
            break;
        default:
            printf("Error: Invalid operator.\n");
            break;
    }

    return 0;
}
