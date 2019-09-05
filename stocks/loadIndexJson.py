import sys
import pycurl

ticker = str(sys.argv[1])


class ContentCallback:
        def __init__(self):
                self.contents = ''

        def content_callback(self, buf):
                self.contents = self.contents + buf

t = ContentCallback()
curlObj = pycurl.Curl()
curlObj.setopt(curlObj.URL, 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=' + ticker + '&outputsize=full&apikey=IRIMIPS587M95R42')
curlObj.setopt(curlObj.WRITEFUNCTION, t.content_callback)
curlObj.perform()
curlObj.close()

print(t.contents)

