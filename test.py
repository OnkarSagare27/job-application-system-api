import requests

headers = {"Authorization": f"Bearer b1"}
res_post = requests.post('http://127.0.0.1:8000/post_job', json={"companyName": "Daily Lancer", "type": "remote"}, headers=headers)

print(res_post.json())
import time 
time.sleep(5)
headers = {"Authorization": f"Bearer a1"}
res_get = requests.get('http://127.0.0.1:8000/get_jobs', headers=headers)
print(res_get.json())