#!/usr/bin/env python

import os
import codecs
from glob import glob

from time import time
import pygments
from pygments import lexers
from pygments.formatters import HtmlFormatter

import markdown
import cssmin
import click
import jinja2
# env = Environment(loader=PackageLoader('templates'))
# env = Environment()
_here = os.path.dirname(__file__)
template_dir = os.path.join(_here, 'templates')


env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(template_dir),
    autoescape=True
)

class SnippetError(Exception):
    pass


@click.command()
@click.option('--out', '-o', help="defaults to stdout")
def run(out):
    snippets = []

    py_lexer = lexers.PythonLexer()
    go_lexer = lexers.GoLexer()
    html_formatter = HtmlFormatter()

    for snippet_dir in _dirs():
        try:
            go_code = codecs.open(
                glob(os.path.join(snippet_dir, '*.go'))[0], 'r', 'utf8'
            ).read()
        except IndexError:
            print snippet_dir, "has no .go code"
            continue
        try:
            py_code = codecs.open(
                glob(os.path.join(snippet_dir, '*.py'))[0], 'r', 'utf8'
            ).read()

        except IndexError:
            print snippet_dir, "has no .py code"
            continue

        id = os.path.basename(snippet_dir)
        title = id.replace('_', ' ').title()
        readme = None
        for f in glob(os.path.join(snippet_dir, '*.md')):
            if readme is not None:
                raise SnippetError('%s contains multiple .md files')
            with codecs.open(f, 'r', 'utf-8') as reader:
                readme = markdown.markdown(reader.read())
        snippets.append({
            'id': id,
            'title': title,
            'readme': readme,
            'go_code': pygments.highlight(go_code, go_lexer, html_formatter),
            'py_code': pygments.highlight(py_code, py_lexer, html_formatter),
        })

    template = env.get_template('build.html')
    html = template.render(
        snippets=snippets,
        highlight_css=html_formatter.get_style_defs('.highlight'),
        foundation_css=env.get_template('foundation.min.css').render()
    )
    if out:
        codecs.open(out, 'w', 'utf-8').write(html)
    else:
        print html


def _dirs():
    indexed = [
        x.strip()
        for x in open('snippets/index.txt').read().splitlines()
        if not x.strip().startswith('#')
    ]
    for name in indexed:  # because this sort order is important
        yield os.path.join('snippets', name)


if __name__ == '__main__':
    run()
