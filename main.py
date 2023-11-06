import re

tokens = {
    'open_par': r'\(',
    'close_par': r'\)',
    'open_brack': '{',
    'close_brack': '}',
    'semicolon': ';',
    'int_kw': 'int',
    'return_kw': 'return',
    'variable_pattern': r'[a-zA-Z]\w*',
    'integer': '[0-9]'
}


def get_first_token(s):
    s = s.lstrip()
    for t in tokens:
        r = '^' + tokens[t]
        searched = re.search(r, s)
        if searched is not None:
            return t, s[searched.span()[1]:]
    raise ValueError(f'No token found at the beginning of {s=}')


def lex(s):
    res = []
    while len(s.lstrip()) > 0:
        t, s = get_first_token(s)
        res.append(t)
    return res


with open('file1.c') as f:
    s_ = f.read()

print(lex(s_))
