# hack 1
import requests
from requests import Request, Session
from bs4 import BeautifulSoup
from WebRequest import web_request


class love_calcz_hack:
    link = ''
    source = None
    posturl = ''
    formdata = {}
    headers = {}
    Email = ''

    def __init__(self, link):
        self.link = link    

    def get_source(self):
        web = web_request(self.link,'get')
        self.source = web.open_request()

    def fill_form(self, name, crush):
        soup = BeautifulSoup(self.source, features="lxml")
        form = soup.find('form', attrs = {'method' : 'post' })
        self.posturl = form.get('action')
        fields = form.find_all('input')
        for field in fields:
            self.formdata[field.get('name')] = field.get('value')

        self.Email = self.formdata['myemailsss']

        self.formdata['nameField'] = name
        self.formdata['crushField'] = crush
        self.headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686)"

    def send_response(self):
        # Using Requests Library to Send a Post Request
        print('Sending Response')
        s = requests.Session()
        try:
            r = s.post(self.posturl, data=self.formdata, headers=self.headers)
        except Exception:
            pass

if __name__ == "__main__":
    
    # Enter the Link that your Friend has shared with you
    link = 'https://lovecalczone.com/calculator/c352fae7/'

    # What you want to send, Fill the below 2 fields
    name = 'N'
    crush = 'C'

    # How many times you want to send the response
    # Set Value for the 'count' 
    count = 1

    love = love_calcz_hack(link)
    love.get_source()
    love.fill_form(name, crush)

    # Email used by your Friend
    print( '\n Email Used: ', love.Email, '\n' )

    for i in range(count):
        love.send_response()

    