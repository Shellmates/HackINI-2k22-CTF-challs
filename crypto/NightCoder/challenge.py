import random 
import datetime
from secret import flag


#Im a night coder, i coded this at night (thursday morning)

def seed_shuffler(my_list, seed):
  random.seed(seed)
  random.shuffle(my_list)
  return my_list

seed=int(datetime.datetime.now().strftime('%Y%m%d%H%M'))

flag = [f for f in flag]
enc = seed_shuffler(flag,seed)

print("".join(enc))

#result at that time: "N_gs{aesD_he_3AtrsOLlh3ROT1sECRl0m}s"


