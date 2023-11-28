from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
import uvicorn

app = FastAPI()

jobApplications = []

tokens = ['a1', 'a2', 'a3']

outh  = OAuth2PasswordBearer(tokenUrl="token")

from fastapi import Depends

class CurrentUserModel:
    def __init__(self, token: str):
        self.token = token

def getCurrentUser(token: str = Depends(outh)) -> CurrentUserModel:
    print(token)
    if token not in tokens:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return CurrentUserModel(token)


@app.post('/post_job')
def postJob(job: dict, currentUser: str = Depends(getCurrentUser)):
    jobApplications.append(job)
    return {"message": "Job posted successfully"}

@app.get('/get_jobs')
def getJobs(currentUser: str = Depends(getCurrentUser)):
    return jobApplications

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)