from pprint import pprint
from csirtg_indicator import Indicator


def process(i):
    return
    try:
        for ii in i.csirtg():
            yield Indicator(**ii, resolve_geo=True)

    except Exception as e:
        pass
