# pyjail2

## Write-up
If we check `sudo -l` we will find out that we can execute `challenge.py` as the user cracked that can read the `flag.txt`.

If we see the source code, we notice that it's exactly like `pyjail1` with the only difference being that the `breakpoint` function is filtered, so the solution for `pyjail1` won't work. Since we don't really need to get a shell but only to read the content `flag.txt`that's what we are going to try.

In order to do this, we need to reproduce this `open("flag.txt")`  with only the allowed characters.

### Step 1 

We can't write `"flag.txt"` directly, so we need to find an alternative for this. `open(input())` will do the work, but it's filtered. Another way to get input is by reading the file descriptor 0, 

```python
open(open(0).read())
``` 

Now we need to find a way to replace `0` with something else, and for that there are multiple solutions:

- `len(list())`

- `int()`

- `int(bool())`

We will end up with this payload: 

```python
open(open(int()).read())
```

### Step 2 

The next step is trying to bypass the `.read`. After some investigation, you may discover that you can accomplish this using for in the following manner:

```python

[line for line in open(int())]

```

Since we only need the first line, we can take advantage of `next` and `iter` and use it to read only the first line.

```python
print(next(iter(open(int()))))
```

```python
>>> print(next(iter(open(int()))))
flag.txt
flag.txt
```

We got flag.txt now we just need to read it using the same method.

```python
print(next(iter(open(next(iter(open(int())))))))
```

But it won't work after writing `flag.txt` and pressing `enter`. We get this 

```
FileNotFoundError: [Errno 2] No such file or directory: 'flag.txt\n'
```

That's because when pressing enter to indicate the end of your input, it will add `\n` to the name of the file, making it wrong.

### Step 3

We must find a way to end the input stream without pressing enter. This can be done using `EOF` which indicates the end of the stream and there is special signal for it. If you press `CTRL + D` it will send and `EOF` signal making the open stops reading and allowing you to only write `flag.txt` and get the flag.


## Flag

`shellmates{I7's_4ll_4b0U7_PYYYYY_SKILZZZ}`
