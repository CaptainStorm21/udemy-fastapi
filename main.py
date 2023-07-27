from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return 'Hello world!'

@app.get('/property')
def property():
    return 'this is a property page'

@app.get('/movies')
def  movies():
    return {'movie list': {'movie 1', 'movie2', 'movie3'}}