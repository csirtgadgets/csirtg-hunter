import logging
import arrow
import re
from pprint import pprint
from csirtg_indicator import Indicator
from csirtg_dnsdb.client import Client
from csirtg_dnsdb.exceptions import QuotaLimit
import os

TOKEN = os.getenv('FARSIGHT_TOKEN', None)
PROVIDER = os.environ.get('FARSIGHT_PROVIDER', 'dnsdb.info')
MAX_QUERY_RESULTS = os.environ.get('FARSIGHT_QUERY_MAX', 10000)
CLIENT = Client()

logger = logging.getLogger(__name__)


def _enabled(i):
    if not TOKEN:
        return

    if not i.is_ipv4:
        return

    if i.tags and 'search' not in i.tags:
        return

    if i.confidence and i.confidence < 4:
        return

    if re.search('^(\S+)\/(\d+)$', i.indicator):
        return

    # don't want to use their stuff atm
    #return True


def process(i, max=MAX_QUERY_RESULTS):
    if not _enabled(i):
        return

    try:
        for r in CLIENT.search(i.indicator):
            first = arrow.get(r.get('time_first') or r.get('zone_time_first'))
            first = first.datetime
            last = arrow.get(r.get('time_last') or r.get('zone_time_last'))
            last = last.datetime

            reporttime = arrow.utcnow().datetime

            r['rrname'] = r['rrname'].rstrip('.')

            ii = Indicator(
                indicator=r['rdata'],
                rdata=r['rrname'].rstrip('.'),
                count=r['count'],
                tags='pdns',
                confidence=4,
                first_at=first,
                last_at=last,
                reported_at=reporttime,
                provider=PROVIDER,
                tlp='amber',
                group='everyone',
                resolve_geo=True,
                resolve_fqdn=True
            )

            yield ii

            max -= 1
            if max == 0:
                break

    except QuotaLimit:
        logger.warn('farsight quota limit reached... skipping')
    except Exception as e:
        logger.exception(e)
        return
