#include <stdio.h>

struct Process{
    int pid, bt, at, rt;
    int ct, wt, tat;
};

void display(struct Process p[], int n){

    int atat = 0;
    int awt = 0;

    printf("\nPID\tAT\tBT\tWT\tCT\tTAT\n");

    for (int i = 1; i <= n; i++)
{
        printf("P%d\t%d\t%d\t%d\t%d\t%d\n",
               p[i].pid, p[i].at, p[i].bt,
               p[i].wt, p[i].ct, p[i].tat);

        awt += p[i].wt;
        atat += p[i].tat;
    }

    printf("\n Avg WT : %d", awt / n);
    printf("\n Avg TAT : %d", atat / n);
}

void fcfs(struct Process p[], int n){

    int time = 0;

    for (int i = 1; i <= n; i++)
{

        if (time < p[i].at)
    {
            time = p[i].at;
        }

        time += p[i].bt;

        p[i].ct = time;

        p[i].tat = p[i].ct - p[i].at;
        p[i].wt = p[i].tat - p[i].bt;
    }

    display(p, n);
}

void sjf_preemptive(struct Process p[], int n){

    int time = 0, completed = 0;

    while (completed < n)
{

        int index = -1;         // index of process with shortest remaining time/shortest_rt process index
        int shortest_rt = 9999; // shortest remaining time of process

        // Find process with shortest remaining time
        for (int i = 1; i <= n; i++)
    {

            if (p[i].at <= time &&
                p[i].rt > 0 &&
                p[i].rt < shortest_rt)
        {

                shortest_rt = p[i].rt;
                index = i;
            }
        }

        // idle case no process run by cpu
        if (index == -1)
    {
            time++;
            continue;
        }

        // process is running hence remaining time is decremented
        // and clock time is incremented
        p[index].rt--;
        time++;

        // process completely executed
        if (p[index].rt == 0)
    {

            completed++;

            p[index].ct = time;
            p[index].tat = p[index].ct - p[index].at;
            p[index].wt = p[index].tat - p[index].bt;
        }
    }

    display(p, n);
}



void round_robin(struct Process p[], int n, int quantum) {

    // Ready queue
    int queue[100];
    int front = 0, rear = 0;

    // Check if process is added
    int added[100] = {0};

    int time = 0, completed = 0;

    while (completed < n) {

        // Add arrived processes to queue
        for (int i = 1; i <= n; i++) {

            if (p[i].at <= time && added[i] == 0) {

                queue[rear++] = i;
                added[i] = 1;
            }
        }

        // CPU idle
        if (front == rear) {
            time++;
            continue;
        }

        // Get process from queue
        int index = queue[front++];

        int run = quantum;

        // Run process for quantum
        while (run > 0 && p[index].rt > 0) {

            p[index].rt--;
            time++;
            run--;

            // Add new processes
            for (int i = 1; i <= n; i++) {

                if (p[i].at <= time && added[i] == 0) {

                    queue[rear++] = i;
                    added[i] = 1;
                }
            }
        }

        // Process completed
        if (p[index].rt == 0) {

            completed++;

            p[index].ct = time;
            p[index].tat = p[index].ct - p[index].at;
            p[index].wt = p[index].tat - p[index].bt;
        }
        else {
            queue[rear++] = index;
        }
    }

    display(p, n);
}



int main(){

    struct Process p[20];

    int n, choice, quantum;

    printf("Enter number of processes: ");
    scanf("%d", &n);

    for (int i = 1; i <= n; i++)
{

        p[i].pid = i;

        printf("Enter arrival time & burst time for process %d: ", i);
        scanf("%d %d", &p[i].at, &p[i].bt);

        p[i].rt = p[i].bt;
    }

    printf("\n--- CPU Scheduling ---\n");
    printf("1. FCFS\n");
    printf("2. SJF Preemptive\n");
    printf("3. Round Robin \n \n");

    printf("Enter your choice: ");
    scanf("%d", &choice);

    if (choice == 1)
{
        fcfs(p, n);
    }
    else if (choice == 2)
{
        sjf_preemptive(p, n);
    }
    else if (choice == 3)
{

        printf("Enter time quantum: ");
        scanf("%d", &quantum);

        round_robin(p, n, quantum);
    }
    else
{
        printf("Invalid choice. Please try again.\n");
    }

    return 0;
}