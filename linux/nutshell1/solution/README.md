# Challenge name

## Write-up

In the line `11`, the content of `v2` gets executed, but in line `8`, `v2` recieve the output of the `read` command, and we know that `read` returns nothing.
By reading the `man` page of `read` in `zsh`, we see that the options `-e` and `-E` allow to echo and affect the variable in the same time.
so all you need to do is to give `-E` or `-e` to `v1`, and then `v2=$(read $v1)` will be interpreted as `v2=$(read -e)`, giving  `cat flag` will print the flag 

# Flag

`shellmates{nUt$H3ll_1_PWnED}`
