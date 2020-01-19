from glob import glob
from parse import parse_odp as parse
from main import own_fun
from tqdm import tqdm

files = glob('training/*.ttl')

def compare(pred, gt):
    good, bad = 0, 0
    for p in pred:
        if p in gt:
            good+=1
        else:
            bad+=1

    return good, bad

good = 0
bad = 0
total = 0

for file in tqdm(files):
    gt = parse(file)
    pred = own_fun(file)

    g,b  = compare(pred, gt)
    good += g
    bad += b
    total += len(gt)

print(f'Poprawne/wszystkie: {good}/{total}')
print(f'Niepoprawne/wszystkie: {bad}/{total}')
