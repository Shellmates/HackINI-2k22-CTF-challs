#include <stdio.h>
#include <stdlib.h>
#include <string.h>


//gcc -m32 -no-pie -fno-stack-protector challenge.c -o challenge

int main(){
    setbuf(stdin, NULL);
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);

    int date=2852022;
    char name[128];
    
    printf("Give me your name: ");
    gets(name);

    printf("Date = %d\n",date);
    if(date == 2752022){
        printf("You win\n");
        system("/bin/cat flag");
    }else{
        printf("You are not allowed\n");
    }
    return 0;
}