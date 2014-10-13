import tornado
try:
    import mistune as markdown
except ImportError:
    import markdown  # py implementation

import tornado.ioloop
import tornado.web


class MarkdownHandler(tornado.web.RequestHandler):
    def get(self):
        body = self.get_argument('body')
        self.write(markdown.markdown(body))


application = tornado.web.Application([
    (r"/markdown", MarkdownHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
