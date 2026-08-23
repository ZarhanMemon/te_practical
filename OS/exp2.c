#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>




void bubblesort( int a[] , int n){

    for ( int i = 0 ; i < n-1 ; i++){

        for (int j = 0 ; j < n-i-1 ; j++){
            if ( a[j] > a[j+1] ){
                int temp = a[j];
                a[j] = a[j+1];
                a[j+1] = temp;
            }
        }
    }
}


// 1.  Parent and Child process Sorting
 
//     FORK() -> create a new child process
//     WAIT( NULL ) -> pause the process 

int child_parent_sort(){


    int arr[10] , n , i;

    printf("Enter the number of elements: ");
    scanf("%d" , &n);

    printf("Enter the elements: ");
    for(i = 0 ; i<n;i++){
        scanf("%d" , &arr[i]);
    }

    //create a new child process of copy parent process ; both running concurrently
    pid_t pid = fork();    

    
    //Child process
    if( pid == 0){

           
        printf("I am Child id : %d \n", getpid());  // getpid() -> get current process id

        printf("my Parent id : %d \n", getppid()); // getppid() -> get parent process id

        bubblesort(arr , n);

        printf("Child process Sorted: ");
        for(i = 0 ; i<n;i++){
            printf("%d " , arr[i]);
        }

        printf("\n");

    }
    //Parent process
    else if( pid > 0){

        wait(NULL);   // wait for child process to finish execution

        printf("I am Parent id : %d \n", getpid());

        printf("my Child process id : %d \n", pid);  // pid -> get child process id

        bubblesort(arr , n);

        printf("Parent process Sorted: ");
        for(i = 0 ; i<n;i++){
            printf("%d " , arr[i]);
        }

        printf("\n");

    }
    else{
        printf("error in process");
    }


    return 0;
    
}



//=========================================================



// 2.  Zombie Process :-  Child process finishes ;
//                        Parent sleeps(10) till child ended ;
//                        Child process becomes zombie process ; 
//                        Untill Parent process exit(0) / terminated or calls wait().

int zombie_process(){

    pid_t pid = fork();


    if ( pid == 0){

        printf("I amChild id : %d \n" , getpid());
        printf("my Parent id : %d \n", getppid());

        printf("Child process ended \n\n");
        exit(0);    // exit(0) => child process exits/terminated


    }
    else if( pid >0 ){

        sleep(10);   // sleep(10) => parent process sleeps for 10 seconds, during this time child process becomes a zombie process
    
        printf("I am Parent id : %d \n", getpid());
        printf("my Child id : %d \n" , pid );

        printf("Parent process ended \n");
    }

    return 0;
    
}



//=========================================================


// 3.  Orphan Process :-  Parent process finished or exit(0) ;
//                        Before child process finishes ;
//                        Child process becomes orphan process ;
//                        Child process is adopted by init process (pid = 1) ;

int orphan_process(){

    pid_t pid = fork();

     if ( pid > 0){


        printf("I am Parent id : %d \n", getpid());
        
        printf("Parent process ended \n");
        exit(0);     
      
    }
    else if ( pid == 0){

        sleep(5);    

        printf("I am Child id : %d \n" , getpid());
        printf("my NEW Parent id : %d \n", getppid());

    }


    return 0;
}



//---------------------------------------------------------



int main(){

    // 1. Parent and Child process Sorting
    child_parent_sort();

    // 2. Zombie Process
    zombie_process();

    // 3. Orphan Process
    orphan_process();

    return 0;
}