# Night Coder

## Write-up

The challenge is going to be solved in two parts, we first need to find a way to reverse the shuffle knowing the seed, this is basically an easy algebra permutation, you can find an explanation [here](https://crypto.stackexchange.com/questions/78309/how-to-get-the-original-list-back-given-a-shuffled-list-and-seed)

Then we will have to bruteforce the seed knowing that the script was written the night of Hack.INI 2k22.

Here is a python script doing so.

```python
import random 
import datetime

def seed_shuffler(my_list, seed):
  random.seed(seed)
  random.shuffle(my_list)
  return my_list


def unshuffle_my_list(shuffled, seed):
  n = len(shuffled)
  
  perm = [i for i in range(1, n + 1)]
  
  perm = seed_shuffler(perm, seed)
  indexer = list(zip(shuffled, perm))
  
  indexer.sort(key=lambda i: i[1])
  
  return [a for (a, b) in indexer]


enc="N_gs{aesD_he_3AtrsOLlh3ROT1sECRl0m}s"

recover =""
seed_time=(datetime.datetime(2022, 5, 25, 10, 0))


while("shellmates" not in recover):
  seed = int(seed_time.strftime('%Y%m%d%H%M'))
  recover="".join(unshuffle_my_list(enc,seed))
  seed_time = seed_time + datetime.timedelta(minutes=1)
  print(recover + str(seed_time), end="\r")

print(recover + str(seed_time))
```


## Flag

`shellmates{N1ghT_C0D3Rs_ArE_LOOs3Rs}`