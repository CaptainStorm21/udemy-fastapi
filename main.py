from fastapi import FastAPI

app = FastAPI()


# static pathes must be ahead of dynamic path
@app.get('/user/admin')
def admin():
    return {'This is admin page'}


# dynamic path
@app.get('/user/{username}')
def profile(username):
    return {f'This is a profile page for {username}'}

