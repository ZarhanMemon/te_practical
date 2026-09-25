#include<stdio.h>

#include<pthread.h>


int data = 0;

int read_count = 0;


pthread_mutex_t r_mutex;

pthread_mutex_t doc_lock;



void *reader ( void *arg){

    int id = *(int *)arg;  // for the reader id no


    pthread_mutex_lock(&r_mutex);

    read_count++;

    if( read_count == 1){
        pthread_mutex_lock(&doc_lock);
    }
    pthread_mutex_unlock(&r_mutex);



// CRITICAL SECTION
    printf("Reader %d reads data = %d\n", id, data);


    pthread_mutex_lock(&r_mutex);

    read_count--;

    if(read_count ==0){
        pthread_mutex_unlock(&doc_lock);
    }

    pthread_mutex_unlock(&r_mutex);


   return NULL; 
}



void *writer( void *arg){

    int id = *(int *)arg;  // FOR THE id of the write


    pthread_mutex_lock(&doc_lock);

    data = data + 1;    // critical section for editing the doc data

    printf("Writer %d writes data = %d\n", id, data);

    pthread_mutex_unlock(&doc_lock);


    return NULL;
}



int main(){

    pthread_t r[3] , w[2];

    int rid[3] = {1 ,2 ,3};
    int wid[2] = {1 ,2} ;


    pthread_mutex_init(&r_mutex , NULL);
    pthread_mutex_init(&doc_lock , NULL);

    
    for( int i=0 ; i<3 ; i++){
        pthread_create(&r[i] , NULL , reader , &rid[i]);
    }

    for( int i=0; i<2 ; i++){
        pthread_create(&w[i] , NULL , writer , &wid[i]);
    }



    for( int i=0; i<3 ; i++){
        pthread_join(r[i] , NULL );
    }

    for( int i=0 ; i<2 ; i++){
        pthread_join(w[i] , NULL);
    }


    return 0;
}



RUN :
gcc rw.c -o rw -pthread
./rw


Reader 1 reads data = 0
Reader 2 reads data = 0
Reader 3 reads data = 0
Writer 1 writes data = 1
Writer 2 writes data = 2
