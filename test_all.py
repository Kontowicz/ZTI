from glob import glob
from parse import parse_odp as parse
from main import own_fun

files = glob('training/*.ttl')

def compare(pred, gt):
    kont = 0
    for p in pred:
        if p in gt:
            print(p)
            kont+=1

    return kont

good = 0
total = 0

for file in files:
    gt = parse(file)
    pred = own_fun(file)

    pkt = compare(pred, gt)
    good += pkt
    total += len(gt)

print(f'Result: {good}/{total}')
