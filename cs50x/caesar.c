#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>
// string caesar_shift(plaintext);
bool only_digits(string argv);

// argument count and array with arguments
int main(int argc, string argv[])
{
    // check if one argument and numeric
    if (argc == 2 && only_digits(argv[1]))
    {
        // forced to add this to reject non-numeric key, not sure why my function doesn't already handle this
        for (int i = 0; i < strlen(argv[1]); i++)
        {
            if (isdigit(argv[1][i]) == 0)
            {
                return 1;
            }
        }

        // DO NOT define this key variable before checking if argument exists otherwise it will return segfault
        int k = atoi(argv[1]);
        // wrapping around alphabet if key is greater than 26
        do
        {
            if (k > 26)
            {
                k = k - 26;
            }
        }
        while (k > 26);

        string plaintext = get_string("plaintext: ");
        // iterate through each letter and increase ascii value by key
        for (int i = 0; i < strlen(plaintext); i++)
        {
            if isalpha(plaintext[i])
            {
                plaintext[i] = plaintext[i] + k;
                // so it doesn't become a symbol
                if (!isalpha(plaintext[i]))
                {
                    plaintext[i] = plaintext[i] - 26;
                }
            }
        }
        printf("ciphertext: %s\n", plaintext);
        return 0;
    }
    else
    {
        // error message if invalid command line argument
        printf("Usage: ./caesar key\n");
        return 1;
    }
}


// function to check if string is all digits
bool only_digits(string argv)
{
    for (int i = 0; i < strlen(argv); i++)
    {
        if isdigit(argv[i])
        {
            return true;
        }
    }
    return false;
}


