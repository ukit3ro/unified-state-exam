from functools import lru_cache

#1 (19, 20, 21)
def moves(x, s):
    return (x + 4, s), (x * 3, s), (x, s + 4), (x, s * 3)

@lru_cache
def game(x, s):
    if any(sum(m) >= 105 for m in moves(x, s)): return 'WIN1'
    if all(game(*m) == 'WIN1' for m in moves(x, s)): return 'LOSS1'
    if any(game(*m) == 'LOSS1' for m in moves(x, s)): return 'WIN2'
    if all(game(*m) == 'WIN1' or game(*m) == 'WIN2' for m in moves(x, s)): return 'LOSS12'

x = 4

for s in range(1, 101):
    if game(x, s) == 'LOSS12':
        print(s)

