#
# @lc app=leetcode id=535 lang=python
#
# [535] Encode and Decode TinyURL
#
import string
import random

longToShort = {}
shortToLong = {}
valid = string.ascii_letters+ string.digits

class Codec:

    def encode(self, longUrl):
        prefix = "http://tinyurl.com/"
        if longUrl in longToShort:
            return  prefix + longToShort[longUrl]
        else:
            shortUrl = ""
            for i in range(0,6):
                shortUrl += valid[random.randint(0, 10000) % 62]
            shortToLong[shortUrl] = longUrl
            longToShort[longUrl] = shortUrl
            return prefix+shortUrl
        

    def decode(self, shortUrl): 
        shortUrl = shortUrl.split('/')[-1]
        if shortUrl in shortToLong:
            return shortToLong[shortUrl]
        else:
            return None
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
# @lc code=end

