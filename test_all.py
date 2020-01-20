from glob import glob
from parse import parse_odp as parse
from main import own_fun
from tqdm import tqdm
from dicts import big_dict
files = glob('training/*.ttl')

def compare(pred, gt):
    good, bad = 0, 0
    print('\n', gt)
    for p in pred:
        print(p)
        for g in gt:
            if sum([h in p for h in g]) == 3:
                good +=1
        else:
            bad+=1
    print('*'*20, '\n\n')
    return good, bad

good = 0
bad = 0
total = 0
possibleRelations = [item.lower() for sublist in list(big_dict.values()) for item in sublist]
for file in tqdm(files):
    gt = parse(file)
    gt2 = y = [g for g in gt if g[1] in possibleRelations]

    pred = own_fun(file)

    g,b  = compare(pred, gt2)
    good += g
    bad += b
    total += len(gt2)

print(f'Poprawne/wszystkie: {good}/{total}')
print(f'Niepoprawne/wszystkie: {bad}/{total}')
