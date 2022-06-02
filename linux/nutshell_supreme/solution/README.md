# nutshell supreme

## Write-up

The `sl` command on arch is not the original one made by [Toyoda Masashi](https://github.com/mtoyoda/sl)  but a branch made by [eyJhb](https://github.com/eyJhb/sl), the difference between them is few options and the exit code, on arch the exit code is `1`, so even when the train passes, the `cat flag` isn't executed. The solution is to inject `-v` to get the version, but the `-` isn't in the whitelist, so you need to give it as hex, to write in `v2` we procede the same way as in [nutshell 1](../../nutshell1), and in `v2` we give 	`\\2dv`

## Flag

`shellmates{nUt$H3ll_supreme_good_job_12345}`
