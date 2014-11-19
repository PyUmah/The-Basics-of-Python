def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
        print '%s got: %s, expected: %s' % (prefix, repr(got), repr(expected))
