import random
import time
from noise import pnoise1
from math import floor

def get_jitter_amount(data_slice, epsilon, chunks):
    chunk_amount = epsilon / chunks
    random.seed(time.time())
    if type(data_slice) is dict:
        j = {}
        keys = []
        for key, _ in data_slice.items():
            j[key] = 0
            keys.append(key)
        
        for c in range(chunks):
            noise = pnoise1(random.random() * 1000000)
            j[keys[floor(noise * len(data_slice))]] += chunk_amount
    else:
        j = [0 for x in range(len(data_slice))]

        for c in range(chunks):
            noise = pnoise1(random.random() * 1000000)
            j[floor(noise * len(data_slice))] += chunk_amount

    return j


def privizor(data, epsilon, chunks = 10000, data_keys=[], options={}, str_change=0.25):
    printed = False
    for i in range(len(data)):
        jitters = get_jitter_amount(data[i], epsilon, chunks)
        if type(data[i]) is dict:
            for key, value in data[i].items():
                if type(value) is str:
                    if key not in options:
                        print("If you want to jitter strings you must specify data_keys and options")
                        printed = True
                    elif jitters[key] > privacy_loss * str_change:
                        data[i][key] = options[key][random.randrange(len(options[key]))]
                else:
                    data[i][key] += data[i][key] * (jitters[key] if pnoise1(random.random() * 1000000) > 0 else (-1 * jitters[key]))
        else:
            for j in range(len(jitters)):
                if type(data[i][j]) is str:
                    if len(data_keys) <= j or data_keys[j] not in options:
                        if not printed:
                            print("If you want to jitter strings you must specify data_keys and options")
                            printed = True
                    elif jitters[j] > privacy_loss * str_change:
                        data[i][j] = options[data_keys[j]][random.randrange(len(options[data_keys[j]]))]
                else:
                    data[i][j] += data[i][j] * (jitters[j] if pnoise1(random.random() * 1000000) > 0 else (-1 * jitters[j]))

    return data
