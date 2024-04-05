import requests

username = 'loidtayag'
token = '67f1ec962818d92f11f3794e6077fc75fcc689d8'
domain_name = 'https://loidtayag.pythonanywhere.com/'

response = requests.get(
    'https://www.pythonanywhere.com/api/v0/user/{username}/webapps/{domain_name}/reload/'.format(
        username=username
    ),
    headers={'Authorization': 'Token {token}'.format(token=token)}
)
if response.status_code == 200:
    print('CPU quota info:')
    print(response.content)
else:
    print('Got unexpected status code {}: {!r}'.format(response.status_code, response.content))