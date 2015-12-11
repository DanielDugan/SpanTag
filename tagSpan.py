import urllib
import re
from BeautifulSoup import *

url = 'http://python-data.dr-chuck.net/comments_205719.html'
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

# Retrieve all of the span tags
tag = soup('span')
count = 0
sum = 0
for i in tag:
    # Look at the parts of a tag
   count += 1
   sum += int(tag.replace("Content: ", ""))
   
print count
print sum
