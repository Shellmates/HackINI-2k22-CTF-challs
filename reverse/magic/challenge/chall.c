#include  <stdio.h>
#include  <stdlib.h>
#include  <unistd.h>
#include <string.h>

#define SECRET_LENGTH 18

int compare_with_secret(char * input);
int mudolo(int op1,int op2);
int main() {
  printf("You think that you found my magic secret?\nTry it out : ");
  char input[SECRET_LENGTH + 1];
  scanf("%18s", input);
  if (compare_with_secret(input)) printf("Congrats you wizard!\n");
  else printf("Wrong! Try again!\n");
  return 0;
}

int mudolo(int op1,int op2){
  return op1%op2;
};

int compare_with_secret(char * input) {
  char cipher[SECRET_LENGTH + 1] = "\x3a\x9\xa\x19\x12\x71\xb\x67\x1c\x1a\xe\x3f\x2b\x20\x3f\x19\x45\x1";
  char c;
  char buf[256];
   memset(buf,'\0',256);
  readlink("/proc/self/exe", buf, 255);
  FILE * fd = fopen(buf, "rb");

  for (char i = 0; i < SECRET_LENGTH; ++i) {
    fseek(fd, mudolo(i,4), SEEK_SET);
    fread( & c, 1, 1, fd);
    input[i] = c ^ input[i];
  }
  return !memcmp(cipher, input, SECRET_LENGTH);
}