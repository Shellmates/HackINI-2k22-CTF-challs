# Nutshell2

## Write-up

In this challenge, the script reads in `v1`, then create a file named with the value inputed, then it checks if the birth date is bigher than the last modify date, wich seems illogic.
By reading the man page of `touch` command, we find the option `-t` wich allows us to specify the last modify date. 
In docker the `stat` command can't get the birth date, so it gives 0 instead, all you need to do is to give a date before the epoch, you can give the following input: `-t 000001010000 nutshell_file`

## Flag

`shellmates{nUt$H3ll_2_PWnED_vkfdnvjfk}` 
