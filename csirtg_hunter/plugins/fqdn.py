import arrow
import os, re
from pprint import pprint


def _invalid(i):
    if not i.is_fqdn:
        return True

    if i.tags and 'pdns' in i.tags:
        return True

    # i.fqdn_resolve()

    if i.get("rdata", '') == '':
        return True


def _copy(i, indicator):
    yield i.copy(**{
        'indicator': indicator,
        'confidence': 0,
        'ns': None,
        'mx': None,
        'rdata': None,
    })


def _rdata(i):
    if not isinstance(i.rdata, list):
        i.rdata = [i.rdata]

    for r in i.rdata:
        ip = i.copy(**{'indicator': r, 'last_at': arrow.utcnow()})

        ip.rdata = [i.indicator]
        ip.confidence = 0
        if i.confidence > 0:
            ip.confidence = i.confidence - 1

        if not ip.description and i.tags:
            ip.description = i.tags[0]

        # this could be a url too, the var is mis-leading
        yield ip

        if ip.is_ip:
            pdns = ip.copy(tags=['pdns'], confidence=4.0, rdata=[i.indicator])
            yield pdns


def _ns(i):
    for ns in i.get('ns', []):
        for ii in _copy(i, ns.rstrip('.')):
            if not ii:
                continue

            yield ii

            if ii.rdata:
                pdns = ii.copy(tags=['pdns'], confidence=4.0,
                               indicator=ii.rdata[0], rdata=ns)
                yield pdns


def _mx(i):
    for mx in i.get('mx', []):
        mx = re.sub(r'^\d+ ', '', mx)
        for ii in _copy(i, mx.rstrip('.')):
            if not ii.indicator or ii.indicator == '':
                continue

            yield ii


def _cname(i):
    for r in i.get('cname', []):
        for ii in _copy(i, r.rstrip('.')):
            yield ii


def process(i):
    if _invalid(i):
        return

    for f in [_rdata, _ns, _mx, _cname]:
        for ii in f(i):
            if not ii:
                continue

            ii.fqdn_resolve()
            ii.geo_resolve()
            yield ii


def main():
    import logging

    logger = logging.getLogger('')
    logger.setLevel(logging.DEBUG)

    from csirtg_indicator import Indicator
    i = Indicator('yimg.com', confidence=2, tags='phishing')
    rv = process(i)

    for r in rv:
        print(str(r))


if __name__ == '__main__':
    main()
