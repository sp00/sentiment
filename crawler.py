#
# Pull down a selection of random tweets and store them in a Redis DB
#

import urllib.request, json, os, sys

from urllib.error import HTTPError,URLError

class TwitterCrawler(object):
  
    def __init__(self):
      
        self.api_base = "http://search.twitter.com/search.json"
    
    def gen_query(self, query, per_page):
      
        return "%s?q=%s&rpp=%d" % (self.api_base, query, per_page)

    # Make an API request
    def fetch(self, search_term, pp=100):
      
        url = self.gen_query(search_term, pp)
        
        try:    
            data = urllib.request.urlopen(url).read()
            results = json.loads(data.decode())
            return results['results']
        except HTTPError as e:
            print("HTTP Error:", e.code, url)
        except URLError as e:
            print("URL Error:", e.reason, url)
            
    def collect_text(self, search_term):
      
      """ Collect only the tweet text and normalize it """
      data = []
      for result in self.fetch(search_term):
          text = result['text'].strip().lower()
          data.append(text)
      return data
          
if __name__ == '__main__':
  
    print(TwitterCrawler().collect_text('basketball'))