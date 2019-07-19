
def process(i):
    if i.provider == 'spamhaus.org':
        return

    i2 = i.spamhaus()

    if not i2:
        return

    i2.tlp = i.tlp
    yield i2
