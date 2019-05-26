from pprint import pprint
from csirtg_indicator import Indicator


def process(i):
    for ii in i.csirtg():
        yield Indicator(**ii, resolve_geo=True)
