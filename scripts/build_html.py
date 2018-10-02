#!/usr/bin/env python

import os
import re
from glob import glob

import pygments
from pygments import lexers
from pygments.formatters import HtmlFormatter

import markdown
import click
import jinja2


_here = os.path.dirname(__file__)
template_dir = os.path.join(_here, "templates")

env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=True)


class SnippetError(Exception):
    """Something wrong with one of the snippets."""


class CheckBuiltFailed(Exception):
    """When the --check-built option fails."""


@click.command()
@click.option("--out", "-o", help="defaults to stdout", default="dist/index.html")
@click.option("--dry-run", "-d", help="Checks that it can be built.", is_flag=True)
@click.option("--check-built", help="Checks that it was already built.", is_flag=True)
def run(out, dry_run=False, check_built=False):
    snippets = []

    py_lexer = lexers.PythonLexer()
    go_lexer = lexers.GoLexer()
    html_formatter = HtmlFormatter()

    for snippet_dir in _dirs():
        go_codes = []
        for fn in glob(os.path.join(snippet_dir, "*.go")):
            with open(fn) as f:
                go_codes.append((fn, f.read()))
        if not go_codes:
            print(snippet_dir, "has no .go code")
            continue

        py_codes = []
        for fn in glob(os.path.join(snippet_dir, "*.py")):
            with open(fn) as f:
                py_codes.append((fn, f.read()))
        if not py_codes:
            print(snippet_dir, "has no .py code")
            continue

        id = os.path.basename(snippet_dir)
        if os.path.isfile(os.path.join(snippet_dir, "title")):
            with open(os.path.join(snippet_dir, "title")) as f:
                title = f.read().strip()
        else:
            title = id.replace("_", " ").title()

        readme = None
        for fn in glob(os.path.join(snippet_dir, "*.md")):
            if readme is not None:
                raise SnippetError("%s contains multiple .md files")
            with open(fn) as f:
                readme = special_markdown(f.read())
        snippets.append(
            {
                "id": id,
                "title": title,
                "readme": readme,
                "go_codes": [
                    (filename, pygments.highlight(code, go_lexer, html_formatter))
                    for filename, code in go_codes
                ],
                "py_codes": [
                    (filename, pygments.highlight(code, py_lexer, html_formatter))
                    for filename, code in py_codes
                ],
            }
        )

    template = env.get_template("build.html")
    html = template.render(
        snippets=snippets,
        highlight_css=html_formatter.get_style_defs(".highlight"),
        bootstrap_css=env.get_template("bootstrap.min.css").render(),
    )
    if dry_run:
        # Everything worked!
        return 0
    if check_built:
        # Raise an error if the newly created HTML isn't the same as what
        # was created before.
        with open(out) as f:
            before = f.read()
        if before != html:
            raise CheckBuiltFailed(
                "The generated HTML is different from what it was before. "
                "That means that the HTML made from the snippets doesn't match "
                "the build HTML. Run this script without --check-built and check "
                "in the changes to the dist HTML."
            )
    elif out:
        with open(out, "w") as f:
            f.write(html)
    else:
        print(html)


_codesyntax_regex = re.compile("```(python|go)")
_markdown_pre_regex = re.compile("```([^`]+)```")


def special_markdown(text):
    def _get_lexer(codesyntax):
        if codesyntax == "python":
            return lexers.PythonLexer()
        elif codesyntax == "go":
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
        found = _codesyntax_regex.sub("```", found)
        if codesyntax:

            def highlighter(m):
                lexer = _get_lexer(codesyntax)
                code = m.group().replace("```", "")
                return pygments.highlight(code, lexer, HtmlFormatter())

            found = _markdown_pre_regex.sub(highlighter, found)
        found = found.replace("```", "<pre>", 1)
        found = found.replace("```", "</pre>")
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
        for x in open("snippets/index.txt").read().splitlines()
        if not x.strip().startswith("#")
    ]
    for name in indexed:  # because this sort order is important
        yield os.path.join("snippets", name)


if __name__ == "__main__":
    run()
