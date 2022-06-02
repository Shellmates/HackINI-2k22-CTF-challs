#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <unistd.h>
#include <assert.h>

#define MAX_FILENAME_SIZE 256

void disable_buffering(void);
void read_str(char *msg, char *buf, unsigned int size);
unsigned long read_num(char *msg);
void error(char *str);
void menu(void);
void allocate_file(void);
void read_file(void);
void write_file(void);
void delete_file(void);

char *file = NULL;
bool isdeleted = true;
unsigned long filename_size, file_size;

void menu(void)
{
    puts("Welcome to the fast in-memory file service!");
    puts("1) Allocate file");
    puts("2) Read file");
    puts("3) Write file");
    puts("4) Delete file");
    puts("0) Exit");
}

void allocate_file(void)
{
    filename_size = read_num("Filename size: ");
    assert(filename_size <= MAX_FILENAME_SIZE);
    file_size = read_num("File size: ");

    file = (char *)malloc(filename_size + file_size + 2);
    if (file == NULL)
        error("Failed to allocate");

    read_str("Filename: ", file, file_size);
    file[file_size] = '\0';

    isdeleted = false;
}

void read_file(void)
{
    if (file == NULL)
        error("File is deleted");
    printf("Filename: %s\n", file);
    printf("File content: %s\n", file + filename_size + 1);
}

void write_file(void)
{
    if (isdeleted)
        error("File is deleted");
    read_str("File content: ", file + filename_size + 1, file_size);
}

void delete_file(void)
{
    if (isdeleted)
        error("File is already deleted");
    free(file);
    isdeleted = true;
}

int main(int argc, char *argv[])
{
    disable_buffering();

    printf("Gift: %p\n", system);

    while (true)
    {
        menu();
        switch (read_num("Choice: "))
        {
        case 1:
            allocate_file();
            break;
        case 2:
            read_file();
            break;
        case 3:
            write_file();
            break;
        case 4:
            delete_file();
            break;
        case 0:
            puts("Bye!");
            return EXIT_SUCCESS;
        default:
            error("Invalid option.");
            break;
        }
    }

    return EXIT_SUCCESS;
}

void disable_buffering(void)
{
    setbuf(stdin, NULL);
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);
}

void read_str(char *msg, char *buf, unsigned int size)
{
    printf("%s", msg);
    assert(read(STDIN_FILENO, buf, size));
}

unsigned long read_num(char *msg)
{
    char buf[24] = {'\0'};

    read_str(msg, buf, 24);
    return strtoull(buf, NULL, 10);
}

void error(char *str)
{
    fprintf(stderr, "%s", str);
    exit(1);
}
