import requests
import json


class APIS:
    def __init__(self):
        with open("data/test_data.json") as f:
            data=json.load(f)

        self.BASE_URL=data["base_url"]
        self.header={"Content-type":"application/json","Authorization": f"Bearer {data['token']}"}


    def get(self,endpoint):
        url=f"{self.BASE_URL}/{endpoint}"
        response=requests.get(url,headers=self.header)
        return response

    def post(self, endpoint,new_data):
        url = f"{self.BASE_URL}/{endpoint}"
        response = requests.post(url, headers=self.header,json=new_data)
        return response

    def patch(self, endpoint,updated_data):
        url = f"{self.BASE_URL}/{endpoint}"
        response = requests.patch(url, headers=self.header,json=updated_data)
        return response

    def delete(self, endpoint):
        url = f"{self.BASE_URL}/{endpoint}"
        response = requests.delete(url, headers=self.header)
        return response


