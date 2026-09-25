#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/stat.h>

int main()
{
    char text[1000];
    char result[1000];

    mkfifo("pipe1", 0666);
    mkfifo("pipe2", 0666);

    printf("Enter sentences:\n");
    fgets(text, sizeof(text), stdin);

    // Write to Process 2
    int fd1 = open("pipe1", O_WRONLY);
    write(fd1, text, sizeof(text));
    close(fd1);

    // Read result from Process 2
    int fd2 = open("pipe2", O_RDONLY);
    read(fd2, result, sizeof(result));
    close(fd2);

    printf("\nResult received from Process 2:\n");
    printf("%s", result);

    return 0;
}


// Output:-

// gcc fifo1.c -o fifo1
// gcc fifo2.c -o fifo2

// Enter sentences:
// hello copilot

// Result received from Process 2:
// Characters: 13
// Words: 2
// Lines: 1


