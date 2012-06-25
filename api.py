#!/usr/bin/env python3

import urllib.request, json, os, sys

from key import API_KEY

from urllib.error import HTTPError,URLError

class API(object):
    
    """ Simple Python 3 Interface to the Rotten Tomatoes Film API """
    
    def __init__(self, k):
        
        self.api_key = k
        self.base_url = "http://api.rottentomatoes.com/api/public/v1.0"
        self.params = '.json?apikey=' + self.api_key
       
    def __request__(self, req):
        
        """ Makes an API request and returns a JSON response """
        try:    
            data = urllib.request.urlopen(req).read()
        except HTTPError as e:
            print("HTTP Error:", e.code, url)
        except URLError as e:
            print("URL Error:", e.reason, url)
        
        return json.loads(bytes.decode(data))
        
    def generate_search_url(self, query):
        
        query = urllib.parse.quote_plus(query)
        return "&q=%s&page=1&limit=100" % (query)
        
    def search(self, query):
        
        """ Performs a search for a given movie """
        
        q = self.generate_search_url(query)
        url = self.base_url + '/movies' + self.params + q
        return self.__request__(url)

    def box_office(self):
        
        req = self.base_url + '/lists/movies/box_office' + self.params
        return self.__request__(req)['movies']
        
    def list_box_office(self):
        
        """ 
            Return a list of the most recent box office movies with the following params
            [[id, title, audience_score, critics_score]]
        
        """
        results = []
        for res in self.box_office():
            try:
                results.append([res['id'], 
                                res['title'], 
                                res['ratings']['audience_score'], 
                                res['ratings']['critics_score']])
            except KeyError: print("Exception parsing movie: %s" (res))
        return results
        
    def get_ratings(self, movie):
        
        """ 
            Return movie review data for a given movie id 
            @param movie [Integer] Movie ID
        """
        
        extra_params = "&review_type=top_critic&page_limit=20&country=us&page=1"
        req = self.base_url + '/movies/' + str(movie) + '/reviews' + self.params + extra_params
        return self.__request__(req)
        
if __name__ == '__main__':
   
    api = API(API_KEY)
    
    # Exploring the data
    for result in api.box_office():
    
        print("%s: %s" % (result['title'], result['mpaa_rating']))