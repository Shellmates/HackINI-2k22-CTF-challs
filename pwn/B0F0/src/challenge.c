#include <stdio.h>
#include <stdlib.h>
#include <string.h>


//gcc -m32 -no-pie -fno-stack-protector challenge.c -o challenge

int main(){
    int date=2852022;
    char name[128];

    setbuf(stdin, NULL);
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);

    printf("Give me your name: ");
    gets(name);
    printf("date = %d\n",date);
    if(date == 2752022){
        printf("You win\n");
        system("/bin/cat flag");
    }else{
        printf("You are not allowed\n");
    }
    return 0;
}
