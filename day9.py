import urllib.request  # python3中由urllib.request 替代 urllib2
# 爬虫


def test():
    resp = urllib.request.urlopen('http://www.baidu.com')
    print(resp)
    html = resp.read()
    # print(html)


if __name__ == '__main__':
    test()
