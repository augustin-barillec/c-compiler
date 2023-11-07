import os
from lex import lex
from parse import parse

i = 1

for b in os.listdir(f'stage_{i}/valid'):
    p = f'stage_1/valid/{b}'
    with open(p) as f:
        x = f.read()
        x = lex(x)
        x = parse(x)
        print(x)

