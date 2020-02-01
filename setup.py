import os
from setuptools import setup, find_packages
import versioneer
import sys

if sys.version_info < (3, 6):
    print("\n")
    print("This requires python 3.6 or higher")
    print("\n")
    raise SystemExit

# https://www.pydanny.com/python-dot-py-tricks.html
if sys.argv[-1] == 'test':
    test_requirements = [
        'pytest',
        'coverage',
        'pytest_cov',
    ]
    try:
        modules = map(__import__, test_requirements)
    except ImportError as e:
        err_msg = e.message.replace("No module named ", "")
        msg = "%s is not installed. Install your test requirements." % err_msg
        raise ImportError(msg)
    r = os.system('py.test test -v --cov=csirtg_hunter --cov-fail-under=50 '
                  '--pep8')
    if r == 0:
        sys.exit()
    else:
        raise RuntimeError('tests failed')

setup(
    name="csirtg-hunter",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="CSIRTG Hunter Framework",
    long_description="",
    url="https://github.com/csirtgadgets/csirtg-hunter-py",
    license='MPL2',
    classifiers=[
               "Topic :: System :: Networking",
               "Programming Language :: Python",
               ],
    keywords=['security'],
    author="Wes Young",
    author_email="wes@csirtgadgets.com",
    packages=find_packages(exclude=["test"]),
    install_requires=[
        'prettytable',
        'dnspython',
        'csirtg_indicator>=3.0a1,<4.0',
        'csirtg_dnsdb',
        'arrow',
    ],
    scripts=[],
    entry_points={
        'console_scripts': [
            'csirtg-hunter=csirtg_hunter:main',
        ]
    },
)
