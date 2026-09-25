#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <ctype.h>
#include <string.h>

int main()
{
    char text[1000];
    char result[1000];

    // Read from Process 1
    int fd1 = open("pipe1", O_RDONLY);
    read(fd1, text, sizeof(text));
    close(fd1);

    int characters = 0;
    int words = 0;
    int lines = 0;
    int inword = 0;

    for (int i = 0; text[i] != '\0'; i++)
    {
        characters++;

        if (text[i] == '\n')
            lines++;

        if (isspace(text[i]))
        {
            inword = 0;
        }
        else if (inword == 0)
        {
            words++;
            inword = 1;
        }
    }

    // Write result to file
    FILE *fp = fopen("result.txt", "w");

    fprintf(fp, "Characters: %d\n", characters);
    fprintf(fp, "Words: %d\n", words);
    fprintf(fp, "Lines: %d\n", lines);

    fclose(fp);

    // Read result file
    fp = fopen("result.txt", "r");

    int n = fread(result, 1, sizeof(result) - 1, fp);
    result[n] = '\0';

    fclose(fp);

    // Send result to Process 1
    int fd2 = open("pipe2", O_WRONLY);
    write(fd2, result, strlen(result) + 1);
    close(fd2);

    return 0;
}