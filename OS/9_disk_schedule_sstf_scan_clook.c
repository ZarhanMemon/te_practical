

#include <stdio.h>
#include <stdlib.h>

void sort(int a[], int n)
{
    for (int i = 0; i < n - 1; i++)
    {
        for (int j = i + 1; j < n; j++)
        {
            if (a[i] > a[j])
            {
                int temp = a[i];
                a[i] = a[j];
                a[j] = temp;
            }
        }
    }
}


// -------------------------------------
// SSTF
// -------------------------------------

void sstf(int request[], int n, int head)
{
    int visited[n];
    int total = 0;

    for (int i = 0; i < n; i++)
        visited[i] = 0;

    printf("\nSSTF Order: %d", head);

    for (int count = 0; count < n; count++)
    {
        int min = 9999;
        int index = -1;

        for (int i = 0; i < n; i++)
        {
            if (!visited[i])
            {
                int distance = abs(head - request[i]);

                if (distance < min)
                {
                    min = distance;
                    index = i;
                }
            }
        }

        visited[index] = 1;

        total += abs(head - request[index]);
        head = request[index];

        printf(" -> %d", head);
    }

    printf("\nTotal Head Movement = %d\n", total);
}


// -------------------------------------
// SCAN
// Direction: Away from spindle
// -------------------------------------

void scan(int request[], int n, int head, int disk_size)
{
    int a[n + 1];

    for (int i = 0; i < n; i++)
        a[i] = request[i];

    a[n] = head;

    sort(a, n + 1);

    int pos = 0;

    for (int i = 0; i < n + 1; i++)
    {
        if (a[i] == head)
        {
            pos = i;
            break;
        }
    }

    int total = 0;

    printf("\nSCAN Order: %d", head);

    // Move toward higher cylinder numbers
    for (int i = pos + 1; i <= n; i++)
    {
        total += abs(head - a[i]);
        head = a[i];

        printf(" -> %d", head);
    }

    // Go to end of disk
    if (head != disk_size - 1)
    {
        total += abs(head - (disk_size - 1));
        head = disk_size - 1;

        printf(" -> %d", head);
    }

    // Reverse direction
    for (int i = pos - 1; i >= 0; i--)
    {
        total += abs(head - a[i]);
        head = a[i];

        printf(" -> %d", head);
    }

    printf("\nTotal Head Movement = %d\n", total);
}


// -------------------------------------
// C-LOOK
// Direction: Away from spindle
// -------------------------------------

void clook(int request[], int n, int head)
{
    int a[n];

    for (int i = 0; i < n; i++)
        a[i] = request[i];

    sort(a, n);

    int total = 0;
    int pos = 0;

    for (int i = 0; i < n; i++)
    {
        if (a[i] >= head)
        {
            pos = i;
            break;
        }
    }

    printf("\nC-LOOK Order: %d", head);

    // Move toward higher values
    for (int i = pos; i < n; i++)
    {
        total += abs(head - a[i]);
        head = a[i];

        printf(" -> %d", head);
    }

    // Jump to lowest request
    if (pos > 0)
    {
        total += abs(head - a[0]);
        head = a[0];

        printf(" -> %d", head);

        // Continue upward
        for (int i = 1; i < pos; i++)
        {
            total += abs(head - a[i]);
            head = a[i];

            printf(" -> %d", head);
        }
    }

    printf("\nTotal Head Movement = %d\n", total);
}


int main()
{
    int n, head, disk_size;

    printf("Enter number of requests: ");
    scanf("%d", &n);

    int request[n];

    printf("Enter request queue:\n");

    for (int i = 0; i < n; i++)
        scanf("%d", &request[i]);

    printf("Enter initial head position: ");
    scanf("%d", &head);

    printf("Enter disk size: ");
    scanf("%d", &disk_size);

    sstf(request, n, head);

    scan(request, n, head, disk_size);

    clook(request, n, head);

    return 0;
}



Output:-

Enter number of requests: 8
Enter request queue:
98 183 37 122 14 124 65 67
Enter initial head position: 53
Enter disk size: 200

SSTF Order: 53 -> 65 -> 67 -> 37 -> 14 -> 98 -> 122 -> 124 -> 183
Total Head Movement = 236

SCAN Order: 53 -> 65 -> 67 -> 98 -> 122 -> 124 -> 183 -> 199 -> 37 -> 14
Total Head Movement = 331

C-LOOK Order: 53 -> 65 -> 67 -> 98 -> 122 -> 124 -> 183 -> 14 -> 37
Total Head Movement = 322