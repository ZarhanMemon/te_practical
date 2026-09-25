// Assignment 4: Dining Philosophers
// Deadlock-free solution using semaphores


#include <stdio.h>
#include <pthread.h>
#include <semaphore.h>
#include <unistd.h>

#define N 5

sem_t forks[N];
sem_t room;

void* philosopher(void* arg)
{
    int id = *(int*)arg;

    printf("Philosopher %d is thinking\n", id);
    sleep(1);

    printf("Philosopher %d is hungry\n", id);

    // Allow only N-1 philosophers to enter
    sem_wait(&room);

    // Pick up forks
    sem_wait(&forks[id]);
    printf("Philosopher %d picked left fork\n", id);

    sem_wait(&forks[(id + 1) % N]);
    printf("Philosopher %d picked right fork\n", id);

    // Eat
    printf("Philosopher %d is eating\n", id);
    sleep(1);

    // Put down forks
    sem_post(&forks[id]);
    sem_post(&forks[(id + 1) % N]);

    printf("Philosopher %d finished eating\n", id);

    // Leave room
    sem_post(&room);

    return NULL;
}

int main()
{
    pthread_t threads[N];
    int id[N];

    // Initialize forks
    for (int i = 0; i < N; i++)
        sem_init(&forks[i], 0, 1);

    // Allow only 4 philosophers at a time
    sem_init(&room, 0, N - 1);

    // Create philosopher threads
    for (int i = 0; i < N; i++)
    {
        id[i] = i;
        pthread_create(&threads[i], NULL, philosopher, &id[i]);
    }

    // Wait for all threads
    for (int i = 0; i < N; i++)
        pthread_join(threads[i], NULL);

    // Destroy semaphores
    for (int i = 0; i < N; i++)
        sem_destroy(&forks[i]);

    sem_destroy(&room);

    return 0;
}



Output:-

gcc dining.c -o dining -pthread
./dining

Philosopher 0 is thinking
Philosopher 2 is thinking
Philosopher 1 is thinking
Philosopher 3 is thinking
Philosopher 4 is thinking
Philosopher 0 is hungry
Philosopher 2 is hungry
Philosopher 2 picked left fork
Philosopher 2 picked right fork
Philosopher 2 is eating
Philosopher 1 is hungry
Philosopher 1 picked left fork
Philosopher 0 picked left fork
Philosopher 3 is hungry
Philosopher 4 is hungry
Philosopher 2 finished eating
Philosopher 1 picked right fork
Philosopher 3 picked left fork
Philosopher 1 is eating
Philosopher 4 picked left fork
Philosopher 1 finished eating
Philosopher 0 picked right fork
Philosopher 0 is eating
Philosopher 0 finished eating
Philosopher 4 picked right fork
Philosopher 4 is eating
Philosopher 4 finished eating
Philosopher 3 picked right fork
Philosopher 3 is eating
Philosopher 3 finished eating