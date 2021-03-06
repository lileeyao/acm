import redis
import hashlib
import base64

class UrlShortener (object):
    """
        @class: UrlShortener
        Use safe hashing.

    """
    def __init__(self):
        # initialize a redis storage.
        #self.r = redis.StrictRedis(host="localhost", port=6379, db=0)
        # use a simple hashmap instead of redis.
        self.r = {}
        self.s = {}
        # google style
        self.head = "goo.gl/"
        # string hashing using md5
        self.md = hashlib.md5()

    def redirect(self, id):
        # get url from redis by id.
        url = self.r.get(id)
        return url

    def shorten(self, req):
        # shorten a requested url and save it in redis.
        self.md.update(req)
        #TODO safe hashing
        #can use a random seed to avoid collision.
        id = self.head + self.md.hexdigest()[:6]
        #TODO use base64 encoding
        #id = self.head + base64.b64encode(req)
        if id not in self.r:
            self.r[id] = req
        else:
            return 'ERROR: DUP_REQUEST'

        return id

# can also use two hash maps
# long url -> short url
# short url -> long url
    def shorten2(self, req):
        if req in self.s:
            return self.s[req]
        else:
            self.md.update(req)
            id = self.head + self.md.hexdigest()[:6]
            self.r[id] = req
            self.s[req] = id

        return id


sol = UrlShortener()
url1 = sol.shorten2("https://www.google.pl/search?q=tomasz+nurkiewicz")
print url1
url2 = sol.shorten2("https://www.uber.com/cities/beijing")
print url2
print sol.redirect(url1)
print sol.redirect(url2)
