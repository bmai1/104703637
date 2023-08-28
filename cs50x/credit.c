#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdbool.h>

int main(void)
{
    // get card number between 0 and 10^16
    long num;
    do
    {
        printf("Number: ");
        scanf("%ld", &num);
    }
    while (num < 0 || num > pow(10, 16));
    long divisor = 1;
    bool check = false;
    // Luhn's algorithm sums
    int first = 0;
    int second = 0;
    // loop number of digits times
    long num_digits = floor(log10(labs(num))) + 1;
    for (int i = 0; i < num_digits; i++)
    {
        // check if i is odd, to find every other digit from 2nd to last
        if (i % 2 != 0)
        {
            check = true;
        }
        else
        {
            check = false;
        }
        int digit = (num / divisor) % 10;
        if (check == true)
        {
            digit *= 2;
            // sum of digits if 10 or more
            if (digit >= 10)
            {
                digit = (digit % 10) + ((digit / 10) % 10);
            }
            first += digit;
        }
        else // remaining digits
        {
            second += digit;
        }
        divisor *= 10;
    }
    // check if card is valid
    int fd, sd;
    int count = log10(num);
    fd = num / pow(10, count); // first digit
    sd = num / pow(10, count - 1); // first two digits
    sd = sd % 10; // second digit only
    if (((second + first) % 10) == 0)
    {
        // check card type
        if (fd == 3 && num_digits == 15 && (sd == 4 || sd == 7))
        {
            printf("AMEX\n");
        }
        else if (fd == 5 && num_digits == 16 && (sd == 1 || sd == 2 || sd == 3 || sd == 4 || sd == 5))
        {
            printf("MASTERCARD\n");
        }
        else if (fd == 4 && (num_digits == 13 || num_digits == 16))
        {
            printf("VISA\n");
        }
        else
        {
            printf("INVALID\n");
        }
    }
    else
    {
        printf("INVALID\n");
    }
}