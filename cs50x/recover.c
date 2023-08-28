#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

// number of bytes in each block to read
#define BLOCK_SIZE 512

// size of each byte
typedef uint8_t BYTE;


int main(int argc, char *argv[])
{
    // check number of command line arguments
    if (argc != 2)
    {
        printf("Usage: ./recover IMAGE\n");
        return 1;
    }

    // card.raw file
    char *filename = argv[1];
    FILE *file = fopen(filename, "r");

    // check if card.raw exists
    if (file == NULL)
    {
        printf("Cannot open %s.\n", filename);
        return 1;
    }

    // num of jpegs for name
    int num = 0;
    char jpg_name[8];

    // check for if not jpeg header
    int check = 0;

    // set new jpg file for loop
    FILE *new_file = NULL;

    // define buffer array to hold bytes
    BYTE buffer[BLOCK_SIZE];

    // iterate over memory card looking for signatures
    while (fread(buffer, 1, BLOCK_SIZE, file) == BLOCK_SIZE)
    {
        // check for jpeg header
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            // if first jpeg
            if (num == 0)
            {
                // new jpeg name
                sprintf(jpg_name, "%03i.jpg", num);
                // new jpeg file
                new_file = fopen(jpg_name, "w");
                // write into new file
                fwrite(buffer, sizeof(BYTE), BLOCK_SIZE, new_file);
                check = 69;
                // increase jpeg value
                num++;
            }
            else
            {
                // close and repeat
                fclose(new_file);
                sprintf(jpg_name, "%03i.jpg", num);
                new_file = fopen(jpg_name, "w");
                fwrite(buffer, sizeof(BYTE), BLOCK_SIZE, new_file);
                num++;
            }
        }
        // keep writing into current jpeg if not jpeg header
        else if (check == 69)
        {
            fwrite(buffer, sizeof(BYTE), BLOCK_SIZE, new_file);
        }
    }
    fclose(new_file);
    // filename ###.jpg, start 000.jpg
    // helo i am in pain
    // suffering
}