# Whois

## Write-up

There was an unintended solution due to a mistake during the creation of the challenge where the flag was located in the webroot without any restrictions, so you can access it directly.

## Final payload
```bash
curl -v 'https://whois.challs.shellmates.club/flag.txt'
```

## Flag

`shellmates{i_$h0U1D_HaVE_R3AD_7HE_dOc_W3Ll}`
