# htsel - HTML selector utility

`htsel` is a command-line utility for extracting specific sub-trees from HTML
documents.

```
usage: htsel.py [-h] [-i INPUT] [-x] SELECTOR [SELECTOR ...]

Select HTML elements by CSS selector or XPath.

positional arguments:
  SELECTOR              CSS or XPath selectors to apply to input HTML.

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Input file. Default: stdin
  -x, --xpath           Selectors are XPath queries, not CSS selectors.
```

# Examples

Headings on FSF's home page (XPath selector):

```
cur -s https://www.fsf.org | ./htsel.py -x '//h2/text()[position() = 1]'
```

JavaScript files loaded by DuckDuckGo's home page (XPath selector):

```
curl -s https://duckduckgo.com | htsel.py -x '//script/@src'
```

All links with an `href` attribute:

```
curl -s https://en.wikipedia.org/wiki/Free_software | htsel.py 'a[href]'
```

# License

[GPLv3](./LICENSE.md)
