#include <unistd.h>

int main(void) {
    char *argv[] = { "/usr/local/bin/python3", "/challenge/chall.py", NULL };
    execve(argv[0], argv, NULL);
    return 0;
}
