#include<stdio.h>

#include<pthread.h>
#include<semaphore.h>


int buffer[5];

int front = 0 , rear = 0;

sem_t empty  , full ;

pthread_mutex_t mutex;


void *producer ( void *arg){

    for(int i=1; i<= 10 ; i++){

        sem_wait(&empty);

        pthread_mutex_lock(&mutex);

        buffer[front] = i;
        printf("Produced : %d \n" , buffer[front]);
        front = (front + 1)%5;

        pthread_mutex_unlock(&mutex);

        sem_post(&full);
    }

    return NULL;
}


void *consumer( void *arg){

    for( int i=1; i<=10 ; i++){

        sem_wait(&full);

        pthread_mutex_lock(&mutex);

        printf("Consumed: %d \n" , buffer[rear]);
        rear = (rear+1) % 5;

        pthread_mutex_unlock(&mutex);

        sem_post(&empty);

    }
    return NULL;
}


int main(){

    pthread_t p , c;


    sem_init(&empty , 0 , 5);
    sem_init(&full , 0 , 0);

    pthread_mutex_init(&mutex , NULL);


    pthread_create(&p , NULL , producer , NULL);
    pthread_create(&c , NULL , consumer , NULL);

    pthread_join(p , NULL);
    pthread_join(c , NULL);


    sem_destroy(&empty);
    sem_destroy(&full);
    pthread_mutex_destroy(&mutex);

    return 0;
}


Compile-Run:
gcc producer_consumer.c -o pc -pthread
./pc

Produced : 1 
Produced : 2 
Produced : 3 
Produced : 4 
Produced : 5 
Consumed: 1 
Consumed: 2 
Consumed: 3 
Consumed: 4 
Consumed: 5 
Produced : 6 
Produced : 7 
Produced : 8 
Produced : 9 
Produced : 10 
Consumed: 6 
Consumed: 7 
Consumed: 8 
Consumed: 9 
Consumed: 10 

