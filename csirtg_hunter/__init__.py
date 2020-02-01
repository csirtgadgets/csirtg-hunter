#!/usr/bin/env python3

import logging
import sys
import os
import textwrap
from argparse import ArgumentParser
from argparse import RawDescriptionHelpFormatter
from pprint import pprint
from multiprocessing import Pool, cpu_count
import dns

from csirtg_indicator import Indicator
from csirtg_indicator.constants import LOG_FORMAT
from csirtg_indicator.format import FORMATS

from csirtg_hunter import plugins as hunters
from csirtg_hunter.utils import load_plugins, get_argument_parser

THREADS = os.getenv('THREADS', cpu_count() * 1.5)
THREADS = int(THREADS)

logger = logging.getLogger(__name__)


def resolve(i):
    plugins = load_plugins(hunters.__path__)

    try:
        i = Indicator(i, resolve_geo=True, resolve_fqdn=True)

    except dns.resolver.NoNameservers as e:
        logger.error(e)
        i = Indicator(i)

    data = [i.__dict__()]
    for p in plugins:
        try:
            indicators = p.process(i)
            indicators = [i2.__dict__() for i2 in indicators]
            data += indicators

        except (KeyboardInterrupt, SystemExit):
            break

        except Exception as e:
            if 'SERVFAIL' in str(e):
                continue

            logger.error(e)
            if logger.getEffectiveLevel() == logging.DEBUG:
                import traceback
                traceback.print_exc()

            continue

    return data


def main():  # pragma: no cover
    global THREADS
    p = get_argument_parser()
    p = ArgumentParser(
        description=textwrap.dedent('''\
        Env Variables:

        example usage:
            $ csirtg-hunter 52.22.149.152,1.1.1.1,google.com,hotjasmine.su
        '''),
        formatter_class=RawDescriptionHelpFormatter,
        prog='csirtg-hunter',
        parents=[p]
    )

    p.add_argument('indicators', help='Indicators to Hunt (CSV)')

    args = p.parse_args()

    loglevel = logging.getLevelName('INFO')

    if args.debug:
        loglevel = logging.DEBUG

    console = logging.StreamHandler()
    logging.getLogger('').setLevel(loglevel)
    console.setFormatter(logging.Formatter(LOG_FORMAT))
    logging.getLogger('').addHandler(console)

    if not sys.stdin.isatty():
        data = [l.rstrip("\n") for l in sys.stdin]
        if ',' in data[0]:
            data = data[0].split(',')
    else:
        data = args.indicators
        if ',' in data:
            data = data.split(',')
        else:
            data = [data]

    if len(data) < THREADS:
        THREADS = len(data)

    COLS = ['cc', 'asn', 'indicator', 'rtype', 'tags', 'rdata', 'ns', 'mx']
    pool = Pool(THREADS)

    logger.info('hunting...')
    n = 0
    for output in pool.imap(resolve, data):
        logger.info('results for %s' % data[n])
        for l in FORMATS['table'](output, cols=COLS):
            print(l.rstrip("\n"))
        n += 1


if __name__ == "__main__":
    main()
