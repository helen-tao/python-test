import requests
import json

def get_certificate():
    username='lifeadmin'
    password='Password1'
    headers={'user':username,'password':password}
    url = 'https://unitingcare-api.sabacloud.com/v1/login'

    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        data = response.json()
        certificate = data['certificate']
        return certificate
    else:
        print(f'请求失败，状态码: {response.status_code}')
    
certificate = get_certificate()
print(certificate)


url_get_user_link = 'https://unitingcare-api.sabacloud.com/v1/people?'
type = 'internal'
searchFields = 'started_on'
query = 'started_on=ge=2024-05-20'
count = '100'
startPage = '1'

url_get_user = url_get_user_link+'type='+type+'&f=('+searchFields+')&q=('+query+')&count='+count+'&startPage='+startPage+'&SabaCertificate='+certificate

url_get_detail_link='https://unitingcare-api.sabacloud.com/v1/people/'
searchFields_get_detail = 'person_type,started_on,job_title,lname,fname,person_no'

#print(url_get_user)
response_get_user = requests.get(url_get_user)
data_get_user = response_get_user.json()

user_num = data_get_user['totalResults']-1

for num in range(0,user_num):
    url_get_detail = url_get_detail_link+data_get_user['results'][num]['id']+':('+searchFields_get_detail+')?SabaCertificate='+certificate
    print(url_get_detail)
    response_get_detail = requests.get(url_get_detail)
    data_get_detail = response_get_detail.json()
    print(data_get_detail)


searchFields = 'terminated_on'
query = 'terminated_on=ge=2024-05-20'
count = '100'
startPage = '1'

url_get_user_delete = url_get_user_link+'type='+type+'&f=('+searchFields+')&q=('+query+')&count='+count+'&startPage='+startPage+'&SabaCertificate='+certificate

response_get_user_delete = requests.get(url_get_user_delete)
data_get_user_delete = response_get_user_delete.json()
user_num_delete = data_get_user_delete['totalResults']-1

for num in range(0,user_num_delete):
    url_get_detail = url_get_detail_link+data_get_user_delete['results'][num]['id']+':('+searchFields_get_detail+')?SabaCertificate='+certificate
    print(url_get_detail)
    response_get_detail = requests.get(url_get_detail)
    data_get_detail = response_get_detail.json()
    print(data_get_detail) 