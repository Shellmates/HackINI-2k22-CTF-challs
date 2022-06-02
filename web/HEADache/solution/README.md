# HEADache

## Write-up

After checking, the `app.py` we can see that it's checking if the header `wanna-something` has the value `can-i-have-a-flag-please` in order to return the flag, so we only need to set it.

```bash
curl https://headache.challs.shellmates.club -H "wanna-something: can-i-have-a-flag-please"
```

## Flag

`shellmates{hTTp_H34d37R5_&_p0L173N355_c4n_B3_U53FULL}`
