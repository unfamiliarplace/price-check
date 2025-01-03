import itertools
from pathlib import Path
import csv

PATH_PRICE_LISTS = Path('src/data/prices.csv')
PRICE_LIST_NAMES = ('Base prices', 'With tax', 'With tip')

def read_price_lists() -> list[tuple[int]]:
    lists = [[], [], []]

    with open(PATH_PRICE_LISTS) as f:
        reader = csv.reader(f)
        next(reader)

        for row in reader:
            for (i, col) in enumerate(row):
                if col.strip():
                    lists[i].append(normalize_price(col))

    return lists

def is_valid_float(s: str) -> bool:
    try:
        float(s)
        return True
    except:
        return False
    
def normalize_price(s: str) -> int:
    s = s.strip()

    for c in '.$#,':
        s = s.replace(c, '')

    return int(s)

def prompt_target() -> int:
    t = input('Enter target price: ')
    while not is_valid_float(t):
        print('Invalid float')
        t = input('Enter target price: ')

    return normalize_price(t)

def get_combo_sums(prices: list[int]) -> dict[tuple[int], int]:

    # Obviously very inefficient if more than a few options

    d = {}
    for n in range(1, len(prices) + 1):
        for combo in itertools.combinations(prices, n):
            d[combo] = sum(combo)

    return d

def get_matching_combo_sums(target: int, d: dict[tuple[int], int]) -> list[tuple[int]]:
    combos = []
    
    for (k, v) in d.items():
        if v == target:
            combos.append(k)

    return combos

def get_matching_combos(target: int, prices: tuple[int]) -> list[int]:
    combo_sums = get_combo_sums(prices)
    return get_matching_combo_sums(target, combo_sums)
    
def fmt_price(p: int) -> str:
    p = str(p)
    cents = p[-2:].zfill(2)

    if len(p) < 3:
        dollars = '0'

    else:
        dollars = p[:-2]
        chunks = itertools.batched(dollars[::-1], 3)
        chunks = list(''.join(chunk[::-1]) for chunk in chunks)[::-1]
        dollars = ','.join(chunks)

    return f'${dollars}.{cents}'

def fmt_combo(combo: tuple[int]) -> str:
    return ' + '.join(fmt_price(p) for p in combo)

def fmt_combos(combos: list[tuple[int]]) -> str:
    return '\t' + '\n\t'.join(fmt_combo(t) for t in combos)

def run() -> None:
    target = prompt_target()
    print()
    print(f'Searching for combinations that add to {fmt_price(target)}...')
    print()

    any_price_lists = False
    any_valid_combos = False

    for (i, prices) in enumerate(read_price_lists()):
        if prices:
            any_price_lists = True

            combos = get_matching_combos(target, prices)
            if combos:
                any_valid_combos = True

                print(PRICE_LIST_NAMES[i])
                print(fmt_combos(combos))
                print()
    
    if not any_price_lists:
        print('No price lists found')

    elif not any_valid_combos:
        print('No matching combinations of prices found')

if __name__ == '__main__':
    run()
