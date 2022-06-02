#include <stdio.h>
#include <stdlib.h>
#include <string.h>
char flag[51];
int flag_arr[51] = {115,104,101,108,108,109,97,116,101,115,123,117,80,120,95,49,83,95,52,95,78,49,99,51,95,119,52,89,95,70,48,114,95,80,52,67,107,49,110,57,95,66,49,110,52,82,49,51,50,125};
char tmp[2];
int main() {
  for(int i=0;i<50;i++){
  sprintf(tmp,"%c",flag_arr[i]);
  strcat(flag,tmp);
  }
  char input[51];
  printf("Input flag : ");
  fgets(input, 51, stdin);
  if (!strcmp(input,flag)) {
    printf("Correct flag!\n");
  } else {
    printf("Wrong flag!\nTry Again.");
  }
  return 0;
}
