#
# Pull down a selection of random tweets and store them in a Redis DB
#

import urllib.request, json, os, sys
from urllib.error import HTTPError,URLError

class Twitter(object):
  
    def __init__(self):
        self.api_base = "http://search.twitter.com/search.json"
    
    def gen_query(self, query, per_page=20):
        return "%s?q=%s&rpp=%d" % (self.api_base, query, per_page)

    # Make an API request
    def request(self, req):
        url = self.gen_query(req)
        try:    
            data = urllib.request.urlopen(url).read()
            return json.loads(data.decode())
        except HTTPError as e:
            print("HTTP Error:", e.code, url)
        except URLError as e:
            print("URL Error:", e.reason, url)

if __name__ == '__main__':
    results = Twitter().request('clojure')
    for result in results['results']:
        print(result['text'])