#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>
#include <string.h>

int main()
{
    int pipe1[2];
    int pipe2[2];

    char filename[100];
    char buffer[1000];

    pipe(pipe1);
    pipe(pipe2);

    pid_t pid = fork();

    if (pid > 0)
    {
        // Parent process

        printf("Enter file path: ");
        scanf("%s", filename);

        // Send filename to child
        close(pipe1[0]);

        write(pipe1[1], filename, sizeof(filename));

        close(pipe1[1]);

        // Read file contents from child
        close(pipe2[1]);

        int n = read(pipe2[0], buffer, sizeof(buffer) - 1);

        buffer[n] = '\0';

        close(pipe2[0]);

        printf("\nFile Contents:\n");
        printf("%s", buffer);

        wait(NULL);
    }
    else
    {
        // Child process

        close(pipe1[1]);

        // Receive filename
        read(pipe1[0], filename, sizeof(filename));

        close(pipe1[0]);

        // Open file
        FILE *fp = fopen(filename, "r");

        if (fp == NULL)
        {
            strcpy(buffer, "File not found.\n");
        }
        else
        {
            int n = fread(buffer, 1, sizeof(buffer) - 1, fp);

            buffer[n] = '\0';

            fclose(fp);
        }

        // Send contents to parent
        close(pipe2[0]);

        write(pipe2[1], buffer, strlen(buffer) + 1);

        close(pipe2[1]);
    }

    return 0;
}


Output:-

gcc pipe.c -o pipe
./pipe

Enter file path: sample.txt

File Contents:
Hello World
This is an operating system practical.