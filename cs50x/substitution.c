#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
// prototypes for 3 functions
bool only_alpha(string argv); // check argument is alphabetical
bool unique(string argv); // check unique letters in key
string rotate(string plaintext, string key); // substitute function


int main(int argc, string argv[])
{
    // check for right amount of command line arguments
    if (argc == 2)
    {
        string key = argv[1];
        // check key length
        if (strlen(key) < 26)
        {
            printf("Key must contain 26 characters.\n");
            return 1;
        }
        // check only alphabetical
        else if (!only_alpha(key))
        {
            printf("Key must only contain alphabetical characters.\n");
            return 1;
        }
        // check no duplicate letters
        else if (!unique(key))
        {
            printf("Key cannot contain identitcal letters.\n");
            return 1;
        }
        // valid key
        if (strlen(key) == 26 && only_alpha(key) && unique(key))
        {
            string plaintext = get_string("plaintext: ");
            string ciphertext = rotate(plaintext, key);
            printf("ciphertext: %s\n", ciphertext);
            return 0;
        }
    }
    // wrong amount of command line args
    else
    {
        printf("Usage: ./substituion key\n");
        return 1;
    }
}


bool only_alpha(string argv)
{
    for (int i = 0; i < 26; i++)
    {
        if (!isalpha(argv[i]))
        {
            return false;
        }
    }
    return true;
}


bool unique(string argv)
{
    // two loops to see if any same letters
    for (int j = 0; j < 26; j++)
    {
        for (int k = j + 1; k < 26; k++)
        {
            if (argv[j] == argv[k])
            {
                return false;
            }
        }
    }
    return true;
}


// Using ASCII values so A/a would equal the first index of the key, then keeping upper/lower cases
string rotate(string plaintext, string key)
{
    for (int l = 0; l < strlen(plaintext); l++)
    {
        // check only for alphabetical, so doesn't encrypt numbers or spaces
        if (isalpha(plaintext[l]))
        {
            if (islower(plaintext[l]))
            {
                plaintext[l] = tolower(key[(plaintext[l] - 97)]); // 97-122
            }
            else if (isupper(plaintext[l]))
            {
                plaintext[l] = toupper(key[(plaintext[l] - 65)]); // 65-90
            }
        }
    }
    return plaintext;
}
