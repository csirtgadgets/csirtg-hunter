from argparse import ArgumentParser
import pkgutil

from csirtg_hunter.constants import VERSION


def get_argument_parser():
    BasicArgs = ArgumentParser(add_help=False)
    BasicArgs.add_argument('-d', '--debug', dest='debug', action="store_true")
    BasicArgs.add_argument('-v', '--verbose', action='store_true')
    BasicArgs.add_argument('-V', '--version', action='version',
                           version=VERSION)

    return ArgumentParser(parents=[BasicArgs], add_help=False)


def load_plugins(path):
    p = []
    for loader, modname, is_pkg in pkgutil.iter_modules(path):
        p.append(loader.find_module(modname).load_module(modname))

    return p
