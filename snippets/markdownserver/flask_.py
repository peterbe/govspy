import logging

try:
    import mistune as markdown
except ImportError:
    import markdown  # py implementation

from flask import Flask, request

app = Flask(__name__)


log = logging.getLogger("werkzeug")
log.setLevel(logging.ERROR)


@app.route("/markdown")
def markdown_view():
    return markdown.markdown(request.args["body"])


if __name__ == "__main__":
    app.run()
