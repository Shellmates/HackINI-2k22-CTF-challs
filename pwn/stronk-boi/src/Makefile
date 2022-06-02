CC=gcc
CFLAGS=-Wl,-z,relro,-z,now -fstack-protector
SOURCE=stronk-boi.c
OUTFILE=../challenge/stronk-boi

all: $(SOURCE)
	$(CC) $(SOURCE) $(CFLAGS) -o $(OUTFILE)
clean: $(OUTFILE)
	rm -f $(OUTFILE)
