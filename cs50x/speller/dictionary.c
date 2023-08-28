// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>

#include "dictionary.h"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;


const unsigned int N = 255;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    int hashv = hash(word);
    // creating a copy to loop to end of linked list
    node *temp = table[hashv];
    while (temp != NULL)
    {
        // try to find word in dict
        if (strcasecmp(word, temp->word) == 0)
        {
            return true;
        }
        // continue searching linked lists for word
        else
        {
            temp = temp->next;
        }

    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    unsigned int sum = 0;
    for (int i = 0; i < strlen(word); i++)
    {
        sum *= toupper(word[i]);
    }
    return sum % N;

}
// word count
int wordc = 0;
// check successful load
bool loaded = false;
// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // open file, check if exists
    FILE *d = fopen(dictionary, "r");
    if (d == NULL)
    {
        return false;
    }
    char word[LENGTH + 1];
    // read word, allocate memory, copy word into node, insert node into one linked list in hash table
    while (fscanf(d, "%s", word) == 1)
    {
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            return false;
        }
        int hashv = hash(word);
        strcpy(n->word, word);
        // insert node into table
        // first node
        if (table[hashv] == NULL)
        {
            // new node is only node and therefore no next node
            n->next = NULL;
            table[hashv] = n;
        }
        else
        {
            // set pointers in order, new node points to hash table first
            n->next = table[hashv];
            // new node becomes head of hash table
            table[hashv] = n;
        }
        wordc++;
    }
    // check for EOF
    if (feof(d))
    {
        loaded = true;
    }
    fclose(d);
    return loaded;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    if (loaded == true)
    {
        return wordc;
    }
    else
    {
        return 0;
    }
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    for (int i = 0; i < N; i++)
    {
        node *temp = table[i];
        while (temp != NULL)
        {
            // make copy of node
            node *temp2 = temp;
            // move original node to next
            temp = temp->next;
            // free the copy in that memory location
            free(temp2);
        }
    }
    return true;
    // no need to return false at end here
}


// I skipped this problem for a while
// And I saved it for when I wanted to feel immense pain
// Still need to solve Tideman though...