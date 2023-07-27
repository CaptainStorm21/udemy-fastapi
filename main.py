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
# assign id to a number type
def property(id:int):
    return {f'this is a property {id}'}

@app.get('/vacation/1')
def property():
    return 'this is a vacation page for user1'

# assign id to a string
@app.get('/profile/{country}')
def profile(country: str):
    return {f'You are visiting {country}'}


@app.get('/movies')
def  movies():
    return {'movie list': {'movie 1', 'movie2', 'movie3'}}