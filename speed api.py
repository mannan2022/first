import requests
api_url='https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=https://developers.google.com'
res=requests.get(api_url)
if res.status_code ==200:
    print(res.json())