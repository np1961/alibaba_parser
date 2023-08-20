from random import random as random
from random import randint
def norm_method(diapazone_, _diapazone):
    return diapazone_+_diapazone*random()
    
def get_random_url(urls):
    random_index=randint(0,len(urls)-1)
    return urls[random_index]
