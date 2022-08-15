from __future__ import print_function
import requests

addr = 'http://127.0.0.1:5000'
test_url = addr + '/api/test'

# prepare headers for http request
content_type = 'image/jpeg'
headers = {'content-type': content_type}

#to create a multipart request, just send the blob as is on RAM
image = open('cat.jpg', 'rb')
files = {'picture': image}

# send http request with image and receive response
response = requests.post(test_url, files=files)

# decode response
print(response.text)
# expected output: {"message": "image received. size=800x500"}

image.close()