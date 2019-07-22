#!/usr/bin/env python3

import argparse
import sys
from collections import Iterable

from lxml import html


def listify(x):
    if isinstance(x, list):
        return x
    if x is None:
        return []
    if isinstance(x, Iterable):
        return [x]
    return list(x)


def html_select(infile, selectors, xpath_selectors=False):
    parsed = html.fromstring(infile.read())
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
    parser = argparse.ArgumentParser(description='HTML CSS/XPath selector.')
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

        print(result)

    exit(ret_code)


if __name__ == "__main__":
    main()
