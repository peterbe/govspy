#!/usr/bin/env python

import os
import re
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


_here = os.path.dirname(__file__)
template_dir = os.path.join(_here, 'templates')

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(template_dir),
    autoescape=True
)


class SnippetError(Exception):
    pass


@click.command()
@click.option('--out', '-o', help="defaults to stdout", default='dist/index.html')
def run(out):
    snippets = []

    py_lexer = lexers.PythonLexer()
    go_lexer = lexers.GoLexer()
    html_formatter = HtmlFormatter()

    for snippet_dir in _dirs():
        go_codes = []
        for f in glob(os.path.join(snippet_dir, '*.go')):
            go_codes.append(
                (f, codecs.open(f, 'r', 'utf8').read())
            )
        if not go_codes:
            print snippet_dir, "has no .go code"
            continue

        py_codes = []
        for f in glob(os.path.join(snippet_dir, '*.py')):
            py_codes.append(
                (f, codecs.open(f, 'r', 'utf8').read())
            )
        if not py_codes:
            print snippet_dir, "has no .py code"
            continue

        id = os.path.basename(snippet_dir)
        title = id.replace('_', ' ').title()
        readme = None
        for f in glob(os.path.join(snippet_dir, '*.md')):
            if readme is not None:
                raise SnippetError('%s contains multiple .md files')
            with codecs.open(f, 'r', 'utf-8') as reader:
                readme = special_markdown(reader.read())
        snippets.append({
            'id': id,
            'title': title,
            'readme': readme,
            'go_codes': [
                (
                    filename,
                    pygments.highlight(code, go_lexer, html_formatter)
                )
                for filename, code in go_codes
            ],
            'py_codes': [
                (
                    filename,
                    pygments.highlight(code, py_lexer, html_formatter)
                )
                for filename, code in py_codes
            ],
        })

    template = env.get_template('build.html')
    html = template.render(
        snippets=snippets,
        highlight_css=html_formatter.get_style_defs('.highlight'),
        bootstrap_css=env.get_template('bootstrap.min.css').render()
    )
    if out:
        codecs.open(out, 'w', 'utf-8').write(html)
    else:
        print html


_codesyntax_regex = re.compile('```(python|go)')
_markdown_pre_regex = re.compile('```([^`]+)```')

def special_markdown(text):

    def _get_lexer(codesyntax):
        if codesyntax == 'python':
            return lexers.PythonLexer()
        elif codesyntax == 'go':
            return lexers.GoLexer()
        elif codesyntax:
            raise NotImplementedError(codesyntax)
        else:
            return lexers.TextLexer()

    def matcher(match):
        found = match.group()
        try:
            codesyntax = _codesyntax_regex.findall(found)[0]
        except IndexError:
            codesyntax = None
        found = _codesyntax_regex.sub('```', found)
        if codesyntax:
            def highlighter(m):
                lexer = _get_lexer(codesyntax)
                code = m.group().replace('```', '')
                return pygments.highlight(code, lexer, HtmlFormatter())
            found = _markdown_pre_regex.sub(highlighter, found)
        found = found.replace('```', '<pre>', 1)
        found = found.replace('```', '</pre>')
        return found

    text = _markdown_pre_regex.sub(matcher, text)

    # html = markdown.markdown(gfm(text))
    html = markdown.markdown(text)
    return html


def xspecial_markdown(text):
    # regular markdown but format the ```<syntax>  blocks differently
    md = markdown.markdown(text)

    return md

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
