# LinkedIn Learning Python course by Joe Marini
# Example file for parsing and processing JSON
#

import urllib.request 
import json

# Open the URL and read the data
weurl=urllib.request.urlopen("https://uselessfacts.jsph.pl/api/v2/facts/random")
print("result code: ", weurl.getcode())


# Read the JSON data from the source
data = weurl.read()
#print(data)

# Print the content of the 'text' field
thejson = json.loads(data)
print(thejson['text'])