# byte_by_byte

## Write-up 

If we check the source code, we can see that the way the `q` is generated is a bit weird.

q is the prime number following p. With this setup, the difference between `p` and `q` is generally small. So how can we break this?

This is the direct application of fermat thoerem:

Since we can write every odd number in this format: `n = a^2-b^2 --> n = (a-b)*(a+b) --> p = a-b , q = a+b`

If the difference between `a` and `b` is small, we can easily brute force them by choosing a value for `a` then checking if `a^2-n` is a square number.

We can start with the square root of `n`

## Flag

`shellmates{F3RM47_H4S_Ju57_T0Ok_R$A_D0WN}`