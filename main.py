from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return 'Hello world!'

@app.get('/property')
def property():
    return 'this is a property page'

# id here is a path paramter
@app.get('/property/{id}')
def property(id):
    return {f'this is a property {id}'}

@app.get('/vacation/1')
def property():
    return 'this is a vacation page for user1'


@app.get('/movies')
def  movies():
    return {'movie list': {'movie 1', 'movie2', 'movie3'}}