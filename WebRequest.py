
import requests 
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
