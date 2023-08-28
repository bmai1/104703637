#include <stdio.h>

int main(void)
{
    // height input between 1 and 8
    int h;
    do
    {
        printf("Height: ");
        scanf("%d", &h);
    }
    while (h < 1 || h > 8);


    // set i to one so nested loops will print one hash for first iteration
    for (int i = 1; i < h + 1; i++)
    {
        // j = h works because the amount of spaces is one less than height
        for (int j = h; j > i; j--)
        {
            printf(" ");
        }
        for (int k = 0; k < i; k++)
        {
            printf("#");
        }
        // constant two space
        printf("  ");
        for (int l = 0; l < i; l++)
        {
            printf("#");
        }
        printf("\n");
    }
}