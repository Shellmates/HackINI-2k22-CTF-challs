# correct

## Write-up

There is a function `check` with a condition. Once we pass the condition, we get the flag. The idea is to send an object to the function in which we will overwrite the '__eq__' method responsible for `==` and make it return True in all cases.

```python
check(type('true', (), {'__eq__': lambda self, wthvr:True})())
``` 

## Flag

`shellmates{Sn4k3_objects_h4s_b33n_corrupted}`
