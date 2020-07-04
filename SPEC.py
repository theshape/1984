##

import http.client
import mimetypes
conn = http.client.HTTPSConnection("imdb-api.com", 443)
payload = ''
headers = {}

## https://imdb-api.com/en/API/SearchMovie/k_16w9K5sV/(1984)

conn.request("GET", "/en/API/SearchMovie/k_16w9K5sV/1984", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))


