#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

void setup(void);
void win(void);

int main(int argc, char *argv[]) {
  int idx;
  char arr[8][8];

  setup();

  while (1) {
    printf("Idx: ");
    scanf("%d", &idx);

    if (idx >= 8) {
      printf("Wrong index!\n");
    } else {
      printf("Data: ");
      read(0, arr[idx], 8);
    }
  }

  return 0;
}

void setup(void) {
  setbuf(stdin, NULL);
  setbuf(stdout, NULL);
  setbuf(stderr, NULL);
}

void win(void) {
  int fd;
  char buf[256] = { '\0' };

  fd = open("/challenge/flag.txt", O_RDONLY);
  read(fd, buf, 256);
  write(1, buf, 256);
}
