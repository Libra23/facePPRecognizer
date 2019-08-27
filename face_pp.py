import requests
import pprint


class FacePP:
    def __init__(self, api_key, api_secret):
        self.API_KEY = api_key
        self.API_SECRET = api_secret

    def create_faceset(self):
        create_url = 'https://api-us.faceplusplus.com/facepp/v3/faceset/create'
        payload = {'api_key': self.API_KEY,
                   'api_secret': self.API_SECRET
                   }
        res = requests.post(create_url, data=payload)
        # print('Create')
        # pprint.pprint(res.json())
        return res.json()['faceset_token']

    def add_face(self, faceset_token, face_image, face_id):
        # get face token
        detect_url = 'https://api-us.faceplusplus.com/facepp/v3/detect'
        payload = {'api_key': self.API_KEY,
                   'api_secret': self.API_SECRET,
                   'image_base64': face_image
                   }
        res = requests.post(detect_url, data=payload)
        # print('Detect')
        # pprint.pprint(res.json())
        token = res.json()['faces'][0]['face_token']
        # set face id
        set_url = 'https://api-us.faceplusplus.com/facepp/v3/face/setuserid'
        payload = {'api_key': self.API_KEY,
                   'api_secret': self.API_SECRET,
                   'face_token': token,
                   'user_id': face_id
                   }
        res = requests.post(set_url, data=payload)
        # print('Set')
        # pprint.pprint(res.json())
        # add face token to faceset
        add_url = 'https://api-us.faceplusplus.com/facepp/v3/faceset/addface'
        payload = {'api_key': self.API_KEY,
                   'api_secret': self.API_SECRET,
                   'faceset_token': faceset_token,
                   'face_tokens': token
                   }
        res = requests.post(add_url, data=payload)
        # print('Add')
        # pprint.pprint(res.json())

    def search_face(self, face_image, faceset_token):
        search_url = 'https://api-us.faceplusplus.com/facepp/v3/search'
        payload = {'api_key': self.API_KEY,
                   'api_secret': self.API_SECRET,
                   'image_base64': face_image,
                   'faceset_token': faceset_token
                   }
        res = requests.post(search_url, data=payload)
        # print('Search')
        # pprint.pprint(res.json())
        return res.json()['results'][0]['confidence'], res.json()['results'][0]['user_id']
