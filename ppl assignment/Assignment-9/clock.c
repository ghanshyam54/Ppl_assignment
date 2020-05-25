//11803091

#include<stdlib.h>
#include<stdio.h>
#include<pthread.h>
#include<unistd.h>
#include<time.h>

/* mutex for thread synchronization */
pthread_mutex_t lock;

/* global variables */
int seconds, minutes, hours;

/* function to print the hours */
void* print_hour(void* pString)
{
    pthread_mutex_lock(&lock);
    if(minutes > 59){
        hours++;
        minutes = 0;
        seconds = 0;
    }
    pthread_mutex_unlock(&lock);
    return 0;
}

/* function to print the minutes */
void* print_min(void* pString)
{
    pthread_mutex_lock(&lock);
    if(seconds > 59) {
        minutes++;
        seconds = 0;
    }
    pthread_mutex_unlock(&lock);
    return 0;
}

/* function to print the seconds */
void* print_sec(void* pString)
{
    pthread_mutex_lock(&lock);
    //seconds++;
    if(seconds == 59 && minutes == 59 && hours == 23){
        hours = 0;
        minutes = 0;
        seconds = -1;
    }
    seconds++;
    pthread_mutex_unlock(&lock);
    return 0;
}

int main() {
    /* current time value */
    time_t rawtime;
    struct tm * timeinfo;

    time(&rawtime); //provide system time
    
    timeinfo = localtime(&rawtime);  //convert the time in hrs,min,sec

    hours = timeinfo->tm_hour;
    minutes = timeinfo->tm_min;
    seconds = timeinfo->tm_sec;

    printf("The current time is : \n");
    printf("HH:MM:SS\n");
    printf("%2d:%2d:%2d\n", hours, minutes, seconds);
    
    pthread_t second_thread, minute_thread, hours_thread;
    
    while(1) {

        sleep(1);
        pthread_create(&second_thread, NULL, print_sec, NULL);
        pthread_join(second_thread, NULL);
        
        pthread_create(&minute_thread, NULL, print_min, NULL);
        pthread_join(minute_thread, NULL);

        pthread_create(&hours_thread, NULL, print_hour, NULL);
        pthread_join(hours_thread, NULL);
        
        printf("%2d:%2d:%2d\n", hours, minutes, seconds);
    }
    return 0;
}
