import requests

url = 'https://api.github.com/repos/kennethreitz/requests/issues'
res = requests.get(url)

print(res.status_code)
print(res.headers)
print(res.text)
