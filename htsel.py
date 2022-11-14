#!/usr/bin/env python3

__title__ = 'htsel'
__version__ = '0.0.2'
__license__ = 'GPLv3'
__summary__ = 'Select HTML elements by CSS selector or XPath'
__author__ = 'Walter Leibbrandt'
__email__ = 'htsel_wrl_co_za'
__uri__ = 'https://github.com/walterl/htsel'

import argparse
import sys


def isiterable(x):
    try:
        iter(x)
        True
    except TypeError:
        False


def listify(x):
    if isinstance(x, list):
        return x
    if x is None:
        return []
    if isiterable(x):
        return [x]
    return list(x)


def html_select(infile, selectors, xpath_selectors=False):
    from lxml import html

    parsed = html.fromstring(infile.read().encode())
    if xpath_selectors:
        fn_select = parsed.xpath
    else:
        fn_select = parsed.cssselect

    for selector in selectors:
        try:
            for found in listify(fn_select(selector)):
                yield found
        except Exception as exc:
            yield exc


def create_arg_parser():
    parser = argparse.ArgumentParser(
        description='Select HTML elements by CSS selector or XPath.',
    )

    parser.add_argument(
        'SELECTOR', nargs='+',
        help='CSS or XPath selectors to apply to input HTML.',
    )
    parser.add_argument(
        '-i', '--input', type=argparse.FileType('r'), default=sys.stdin,
        help='Input file. Default: stdin',
    )
    parser.add_argument(
        '-x', '--xpath', action='store_true', default=False,
        help='Selectors are XPath queries, not CSS selectors.',
    )

    return parser


def main():
    from lxml import html

    options = create_arg_parser().parse_args()
    ret_code = 0
    for result in html_select(
        options.input, options.SELECTOR, xpath_selectors=options.xpath,
    ):
        if isinstance(result, Exception):
            print(f'Error: {type(result).__name__}: ', end='')
            ret_code = 1

        if isinstance(result, html.HtmlElement):
            result = html.tostring(result, pretty_print=True).decode()

        if isinstance(result, str):
            result = result.strip()

        print(result)

    exit(ret_code)


if __name__ == "__main__":
    main()
