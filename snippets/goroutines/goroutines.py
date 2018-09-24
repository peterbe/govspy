import urllib2
import multiprocessing


def f(url):
    req = urllib2.urlopen(url)
    try:
        print(len(req.read()))
    finally:
        req.close()


urls = ("https://www.peterbe.com", "https://python.org", "https://golang.org")


if __name__ == "__main__":
    p = multiprocessing.Pool(3)
    p.map(f, urls)
