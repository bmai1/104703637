// gcc volume.c -o volume    
// Modifies the volume of an audio file

#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

// Number of bytes in .wav header
const int HEADER_SIZE = 44;

int main(int argc, char *argv[])
{
    // Check command-line arguments
    if (argc != 4)
    {
        printf("Usage: ./volume input.wav output.wav factor\n");
        return 1;
    }

    // Open files and determine scaling factor
    FILE *input = fopen(argv[1], "r");
    if (input == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    FILE *output = fopen(argv[2], "w");
    if (output == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    float factor = atof(argv[3]);

    // TODO: Copy header from input file to output file
    uint8_t header[HEADER_SIZE]; // array of 44 bytes, store data from WAV file header
    fread(&header, HEADER_SIZE, 1, input); // fread/write(array/buffer, how many bytes, num bytes each, file pointer)
    fwrite(&header, HEADER_SIZE, 1, output);

    // TODO: Read samples from input file and write updated data to output file
    // volume * factor
    int16_t buffer; // store audio, buffer argument to fread or write into/from buff

    while (fread(&buffer, sizeof(int16_t), 1, input)) // this reads until end of file
    {
        buffer *= factor;
        fwrite(&buffer, sizeof(int16_t), 1, output); // writing buffer into output
    }

    // Close files
    fclose(input);
    fclose(output);
}
