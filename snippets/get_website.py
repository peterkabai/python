import urllib.request

def get_page(url):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    request = urllib.request.Request(url, headers = {'User-Agent': user_agent})
    page = urllib.request.urlopen(request).read().decode('utf-8')
    return(page)
  
def test():
    url = 'https://www.yahoo.com'
    page = get_page(url)
    print(page)
