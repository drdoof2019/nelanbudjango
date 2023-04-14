# # This code is based on the post of the user smaffulli @ https://discussion.dreamhost.com/t/how-to-post-content-to-wordpress-using-python-and-rest-api/65166

# import requests
# import json
# import base64

# user = "admin" # the user in which the auth. token is given
# pythonapp = "zpxx nXsZ AHLs S0n1 CgwZ i03h" # paste here your auth. token from Wordpress (plugin used: https://wordpress.org/plugins/application-passwords/)
# url = 'http://www.suleatac.com/wp-json/wp/v2' # the url of the wp access loc
# token = base64.standard_b64encode((user + ':' + pythonapp).encode('utf-8')) # we have to encode the usr and pw
# headers = {'Authorization': 'Basic ' + token.decode('utf-8')} # here we define which the auth. type used

# media = {'file': open('image.jpg','rb')} # 'picture.jpg' path to the image, we load it as a binary file

# image = requests.post(url + '/media', headers=headers, files=media) # create a post request with the file
# link = json.loads(image.content.decode('utf-8'))['link'] # get the link to the image out of the response
# postid =json.loads(image.content.decode('utf-8'))['id'] # get the post-id of the image out of the response (we will use it further down to change the wp-image parameters)
# print('Your image is published on {} with ID {}'.format(link, postid))

# # now we change the parameters of the image for a complete list you can check back at the link to your media-post like this:
# # http://www.mypage.com/wp-json/wp/v2/media/MYIMAGEPOSTID
# # here we just change the caption and description; You can also use html here:
# post = {'caption': 'My great demo picture',
#         'description': 'my great descrition'
#         }
# r = requests.post(url + '/media/'+str(postid), headers=headers, json=post) # make now a standard post request this time with the json 'post' as content
# print('Your image is updated on {} with ID {}'.format(link, postid))

# # for publishing a simple post you can use the following:

# post = {'date': '2023-02-19T20:00:35',
#         'title': 'First REST API post',
#         'slug': 'rest-api-1',
#         'status': 'publish',
#         'author': '1',
#         'excerpt': 'Exceptional post!',
#         'format': 'standard'
#         }
# r = requests.post(url + '/posts', headers=headers, json=post)
# print('Your post is published on ' + json.loads(r.content)['link'])

import requests
from requests.auth import HTTPBasicAuth
import json

# Set the WordPress credentials and URL
url = 'https://suleatac.com/wp-json/wp/v2/'
username = 'onur'
password = 'iU09 Y0h2 kt00 7szx 3qOS ZcE9'

# Set the authentication headers
headers = {
    # 'Authorization': f'Application Password {username}:{password}',
    'Content-Type': 'application/json',
}


# media = {
#     'file' : open('cag_kebap.jpg', 'rb'),
#     'caption' : "Cağ Kebap",
#     'description' : "Cağ Kebabı resmi"
# }
# print(url)
# image = requests.post(url + 'media', auth = HTTPBasicAuth(username, password), 
#                       headers=headers, files=media)


# Set the post data
post_data = {
    'title': 'First api post without image',
    'content': 'This is my new post content. <br> <p>Şuliş Seni Seviyorum</p><br><h1>Merhaba Dünya!</h1>',
    'status': 'publish',
}


# Create the post
response = requests.post(url + 'posts', auth = HTTPBasicAuth(username, password), 
                         headers=headers, json=post_data)

# Print the response status code and text
print(f'Response status code: {response.status_code}')
print(f'Response text: {response.text}')
