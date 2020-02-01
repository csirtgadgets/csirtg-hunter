import arrow
from urllib.parse import urlparse


def process(i):
    if not i.is_url:
        return

    u = urlparse(i.indicator)
    if not u.hostname:
        return

    fqdn = i.copy(**{
        'indicator': u.hostname,
        'rdata': i.indicator,
        'last_at': arrow.utcnow(),
        'reported_at': arrow.utcnow(),
        'confidence': 0,
    })

    if i.confidence == 1:
        fqdn.confidence = 0
    else:
        fqdn.confidence = i.confidence - 2

    yield fqdn
