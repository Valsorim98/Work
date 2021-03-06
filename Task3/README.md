# **This is documentation file for Task3**

For Task3 every file in the folder acts as a different method which can be run separately. The names of the files equals the function that each method does.

> Environment:

* The scripts are written in Python 3.9.2.

> Required modules to run the programs:

* pymongo - install with command in cmd:
```py
pip install pymongo
```

* requests - install with command in cmd:
```py
pip install requests
```

---
To make a HTTP request we must first install the requests module. In 'cmd' type "pip install requests" to install the module.

* The GET method indicates that you’re trying to get or retrieve data from a specified resource. To make a GET request, invoke requests.get().

* POST method requests that a web server accepts the data enclosed in the body of the request message, most likely for storing it.

* The PUT method requests that the enclosed entity be stored under the supplied URI. If the URI refers to an already existing resource, it is modified and if the URI does not point to an existing resource, then the server can create the resource with that URI.

* PATCH is used for modify capabilities. The PATCH request only needs to contain the changes to the resource, not the complete resource.

* The DELETE method deletes the specified resource.
---
With the following code we send a **GET** request to the url:

```py
import requests

url = "https://httpbin.org/get"

payload = {"key1": "value1", "key2": "value2"}

r = requests.get(url, params=payload)

print(f"That is the url: {r.url}")

print(f"That is the status code: {r.status_code}")
```
---
HTTP Status Codes:

200: OK

400: Bad Request

403: Forbidden

404: Not found

---
With the following code we send a **POST** request to the url:

```py
import requests

url = "https://httpbin.org/post"

payload = {"FirstName": "John", "LastName": "Smith"}

r = requests.post(url, data=payload)
```
---
With the following code we send a **PUT** request to the url:

```py
import requests

url = "https://httpbin.org/put"

payload = {"FirstName": "John", "LastName": "Smith"}

r = requests.put(url, data=payload)
```
* When using the **PUT** method if the Request-URI refers to an already existing resource then the **PATCH** method will be used. Otherwise if the Request-URI is not existing, then the **POST** method will be used.

---
With the following code we send a **PATCH** request to the url:

```py
import requests

url = "https://httpbin.org/patch"

payload = {"FirstName": "John", "LastName": "Smith"}

r = requests.patch(url, data=payload)
```
---
With the following code we send a **DELETE** request to the url:

```py
import requests

url = "https://httpbin.org/delete"

payload = {"FirstName": "John", "LastName": "Smith"}

r = requests.delete(url, data=payload)
```
---
With the following code we send a **GET** request to download images from the urls:

```py
import requests

# That's for downloading an image from xkcd.com

receive = requests.get("https://imgs.xkcd.com/comics/history_department.png")

with open(r"C:\Users\PC\Desktop\downloaded_img.png","wb") as f:

    f.write(receive.content)


# That's for downloading an image from httbin.org

receive = requests.get("https://httpbin.org/image/png")

with open (r"C:\Users\PC\Desktop\image1.png", "wb") as f:

    f.write(receive.content)
```
---
With the following code we **create a new database and a collection in MongoDB and save documenents** in the collection:

```py
# Save the document with the content from https://httpbin.org/get :

import pymongo

from pymongo import MongoClient

import requests

import json

client = MongoClient()

db = client["test_db"]

url = "https://httpbin.org/get"

payload = {"key1": "value1", "key2": "value2"}

response = requests.get(url, params=payload)

test_collection = db.test_collection

content = response.text

json_content = json.loads(content)

result = test_collection.insert_one(json_content)

# Save another document with the content of headers from https://www.bloomberg.com/europe :

url = "https://www.bloomberg.com/europe"

response_2 = requests.get(url)

result = test_collection.insert_one(response_2.headers)
```
