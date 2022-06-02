#include <stdio.h>
#include <stdlib.h>
#include <string.h>


//gcc -m32 -no-pie -fno-stack-protector challenge.c -o challenge

void open_shell(int password){
    if (password==1337){
        printf("good job you get a shell :)\n");
		system("/bin/sh");
		exit(0);
    }else{
        printf("password incorrect\n");
        exit(0);
    }
}

void say_my_name(){
    char name[20];
    printf("Give me your name: \n");
    gets(name);
    printf("Hello %s\n",name);
}


int main(){
    setbuf(stdin, NULL);
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);

    say_my_name();
    return 0;
}
