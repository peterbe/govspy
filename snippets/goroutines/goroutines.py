import urllib2
import multiprocessing


def f(url):
    req = urllib2.urlopen(url)
    try:
        print len(req.read())
    finally:
        req.close()


urls = (
    "http://www.peterbe.com",
    "http://peterbe.com",
    "http://htmltree.peterbe.com",
    "http://tflcameras.peterbe.com",
)

if __name__ == '__main__':
    p = multiprocessing.Pool(3)
    p.map(f, urls)
