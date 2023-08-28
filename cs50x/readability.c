#include <cs50.h>
#include <stdio.h>
// strlen
#include <string.h>
// identify data type
#include <ctype.h>
// round()
#include <math.h>

//prototypes for functions
int count_letters(string text);
int count_words(string text);
int count_sentences(string text);


int main(void)
{
    string passage = get_string("Text: ");
    // count how many letters
    int letter_count = count_letters(passage);
    // count how many words (float so it can be divided without truncation returning 0)
    float word_count = count_words(passage);
    float sentence_count = count_sentences(passage);
    // percent of a hundred words
    float per_hundred = (word_count / 100.0);
    // find average amount of letters per hundred words
    float L = letter_count / per_hundred;
    // find average amount of sentences per hundred words
    float S = sentence_count / per_hundred;
    // Coleman-Liau index formula
    float index = 0.0588 * L - 0.296 * S - 15.8;
    int grade = round(index);
    // check what message to print
    if (grade < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (grade >= 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", grade);
    }
}

// function to count how many letters in text
int count_letters(string text)
{
    int letters = 0;
    for (int i = 0; i < strlen(text); i++)
    {
        if (isalpha(text[i]))
        {
            letters++;
        }
    }
    return letters;
}

// function to count how many words in text
int count_words(string text)
{
    int words = 0;
    for (int j = 0; j < strlen(text); j++)
    {
        if (isspace(text[j]))
        {
            words++;
        }
    }
    return words + 1;
}

// function to count how many sentences in text
int count_sentences(string text)
{
    // had difficulty comparing strings and chars, resort to defining three valid cases as variable
    char period = '.';
    char exclam = '!';
    char quest = '?';
    int sentences = 0;
    for (int k = 0; k < strlen(text); k++)
    {
        if (ispunct(text[k]))
        {
            // code can be improved here
            if ((text[k] == period) || (text[k] == exclam) || (text[k] == quest))
            {
                sentences++;
            }
        }
    }
    return sentences;
}