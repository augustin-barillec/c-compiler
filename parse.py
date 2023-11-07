def parse(tokens):
    return parse_program(tokens)[1]


def parse_program(tokens):
    tokens, function = parse_function(tokens)
    return tokens, ('prog', function)


def parse_function(tokens):
    t0, t1, t2, t3, t4 = tokens[:5]
    assert t0[0] == 'int_kw'
    assert t1[0] == 'var_pattern'
    assert t2[0] == 'open_par'
    assert t3[0] == 'close_par'
    assert t4[0] == 'open_brack'
    tokens = tokens[5:]
    tokens, statement = parse_statement(tokens)
    assert tokens[0][0] == 'close_brack'
    tokens = tokens[1:]
    return tokens, ('function', (t1[1], statement))


def parse_statement(tokens):
    assert tokens[0][0] == 'return_kw'
    tokens = tokens[1:]
    tokens, expression = parse_expression(tokens)
    assert tokens[0][0] == 'semicolon'
    tokens = tokens[1:]
    return tokens, ('statement', expression)


def parse_expression(tokens):
    t0 = tokens[0]
    assert t0[0] == 'integer'
    tokens = tokens[1:]
    return tokens, ('expression', t0)
