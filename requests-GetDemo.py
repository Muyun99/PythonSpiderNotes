import requests


def getInfo1():
    headers = {
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
    }
    keyword = {'wd': '长城'}
    response = requests.get(
        "http://baidu.com/s?", params=keyword, headers=headers)
    print(response.encoding)
    print(response.text.encode('utf-8'))
    print(response.content)
    print(response.url)
    print(response.status_code)
    print(response.encoding)


def getInfo2():
    response = requests.get('http://www.sina.com')
    print(response.request.headers)
    print(response.content.decode())


def getInfoFromTieba():
    headers = {
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
    }
    keyword = {'kw': '中超'}
    response = requests.get(
        "https://tieba.baidu.com/f?", params=keyword, headers=headers)
    print(response.url)


if __name__ == '__main__':
    # getInfo1()
    # getInfo2()
    getInfoFromTieba()