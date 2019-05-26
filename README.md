# CSIRTG Hunting Framework

The FASTEST way to build a Threat Hunting Toolkit

### Requirements
* Python 3.6 or higher

### Extras
Not required- but useful.

* Maxmind GeoIP ASN / Country Databases

## Getting Started

### Commandline
```bash
$ export CSIRTG_TOKEN=1234..    # not required- signup at csirtg.io
$ pip install csirtg-hunter

$ $ csirtg-hunter 52.22.149.152,1.1.1.1,google.com,hotjasmine.su

2019-05-26 10:40:16,711 - INFO - csirtg_hunter[107] - hunting...
2019-05-26 10:40:19,477 - INFO - csirtg_hunter[110] - results for 52.22.149.152
+----+-----+-----------+-------+------+-------+----+----+
| cc | asn | indicator | rtype | tags | rdata | ns | mx |
+----+-----+-----------+-------+------+-------+----+----+
+----+-----+-----------+-------+------+-------+----+----+
2019-05-26 10:40:19,743 - INFO - csirtg_hunter[110] - results for 1.1.1.1
+----+-------+-----------+-------+--------------+-------+----+----+
| cc |  asn  | indicator | rtype |     tags     | rdata | ns | mx |
+----+-------+-----------+-------+--------------+-------+----+----+
| au | 13335 |  1.1.1.1  |       | http,scanner |       |    |    |
+----+-------+-----------+-------+--------------+-------+----+----+
2019-05-26 10:40:19,744 - INFO - csirtg_hunter[110] - results for google.com
+----+-------+----------------------------------+-------+--------------+----------------+----------------------------------+----------------------------------+
| cc |  asn  |            indicator             | rtype |     tags     |     rdata      |                ns                |                mx                |
+----+-------+----------------------------------+-------+--------------+----------------+----------------------------------+----------------------------------+
|    |       | https://maps.google.com/?q=250.. |       | uce-urls,uce |                |                                  |                                  |
|    |       | https://maps.google.com/?q=150.. |       | uce-urls,uce |                |                                  |                                  |
|    |       | https://maps.google.com/?q=167.. |       | uce-urls,uce |                |                                  |                                  |
|    |       | https://maps.google.com/?q=39+.. |       | uce-urls,uce |                |                                  |                                  |
|    |       | https://plus.google.com/110416.. |       | uce,uce-urls |                |                                  |                                  |
| us | 15169 |           172.217.4.46           |   a   |     None     |   google.com   | ns1.google.com.,ns2.google.com.. | 10 aspmx.l.google.com.,20 alt1.. |
| us | 15169 |           172.217.4.46           |   a   |     pdns     |   google.com   | ns1.google.com.,ns2.google.com.. | 10 aspmx.l.google.com.,20 alt1.. |
| us | 15169 |          ns1.google.com          |   a   |     None     | 216.239.32.10  |                                  |                                  |
| us | 15169 |          216.239.32.10           |   a   |     pdns     | ns1.google.com |                                  |                                  |
| us | 15169 |          ns2.google.com          |   a   |     None     | 216.239.34.10  |                                  |                                  |
| us | 15169 |          216.239.34.10           |   a   |     pdns     | ns2.google.com |                                  |                                  |
| us | 15169 |          ns3.google.com          |   a   |     None     | 216.239.36.10  |                                  |                                  |
| us | 15169 |          216.239.36.10           |   a   |     pdns     | ns3.google.com |                                  |                                  |
| us | 15169 |          ns4.google.com          |   a   |     None     | 216.239.38.10  |                                  |                                  |
| us | 15169 |          216.239.38.10           |   a   |     pdns     | ns4.google.com |                                  |                                  |
| us | 15169 |        aspmx.l.google.com        |   a   |     None     | 172.217.214.27 |                                  |                                  |
| us | 15169 |     alt1.aspmx.l.google.com      |   a   |     None     | 74.125.141.26  |                                  |                                  |
| us | 15169 |     alt2.aspmx.l.google.com      |   a   |     None     | 64.233.186.26  |                                  |                                  |
| us | 15169 |     alt3.aspmx.l.google.com      |   a   |     None     | 209.85.202.27  |                                  |                                  |
| us | 15169 |     alt4.aspmx.l.google.com      |   a   |     None     | 64.233.184.26  |                                  |                                  |
+----+-------+----------------------------------+-------+--------------+----------------+----------------------------------+----------------------------------+
2019-05-26 10:40:25,828 - INFO - csirtg_hunter[110] - results for hotjasmine.su
+----+-------+----------------------+-------+--------------+----------------+----------------------------------+----+
| cc |  asn  |      indicator       | rtype |     tags     |     rdata      |                ns                | mx |
+----+-------+----------------------+-------+--------------+----------------+----------------------------------+----+
|    |       | http://hotjasmine.su |       | uce-urls,uce |                |                                  |    |
| us | 45102 |     47.254.89.5      |   a   |     None     | hotjasmine.su  | a.dnspod.com.,b.dnspod.com.,c... |    |
| us | 45102 |     47.254.89.5      |   a   |     pdns     | hotjasmine.su  | a.dnspod.com.,b.dnspod.com.,c... |    |
| us | 45102 |     a.dnspod.com     |   a   |     None     | 58.251.121.110 |                                  |    |
| us | 45102 |    58.251.121.110    |   a   |     pdns     |  a.dnspod.com  |                                  |    |
| us | 45102 |     b.dnspod.com     |   a   |     None     | 119.28.48.232  |                                  |    |
| us | 45102 |    119.28.48.232     |   a   |     pdns     |  b.dnspod.com  |                                  |    |
| us | 45102 |     c.dnspod.com     |   a   |     None     | 180.163.8.114  |                                  |    |
| us | 45102 |    180.163.8.114     |   a   |     pdns     |  c.dnspod.com  |                                  |    |
| us | 45102 |    hotjasmine.su     |   a   |  suspicious  |  47.254.89.5   | a.dnspod.com.,b.dnspod.com.,c... |    |
+----+-------+----------------------+-------+--------------+----------------+----------------------------------+----+

```

## Python
```python
from csirtg_hunter import resolve
from multiprocessing import Pool, cpu_count
from pprint import pprint

DATA = [
    'google.com',
    '1.1.1.1',
    '8.8.8.8',
    'csirtgadets.com'
]

THREADS = (cpu_count() * 1.5)
pool = Pool(THREADS)


for output in pool.imap(resolve, DATA):
        pprint(output)

```