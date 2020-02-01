
def process(i):
    if i.provider == 'spamhaus.org':
        return

    if not i.is_ipv4:
        return

    if '/' in i.indicator:
        return

    i2 = i.spamhaus()

    if not i2:
        return

    i2.tlp = i.tlp

    yield i2
