from csirtg_hunter import resolve

DATA = [
    'google.com',
    '1.1.1.1',
    '8.8.8.8',
    'csirtgadets.com',
    'yimg.com'
]


def test_basics():

    c = 0
    for i in DATA:
        r = resolve(i)
        c += len(r)

    assert c > 0
