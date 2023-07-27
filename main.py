from fastapi import FastAPI
from pydantic import BaseModel

class Profile(BaseModel):
    name: str
    email: str
    age: int
    
class Product (BaseModel):
    name: str
    price: int
    discount: int
    discounted_price: float
    

app = FastAPI()

@app.post('/addProduct')
def addProduct(product:Product):
    product.discounted_price = product.price-\
    (product.price * product.discount)/100
    return product

@app.get('/user/admin')
def admin():
    return {'This is admin page'}



@app.get('/user/{username}')
def profile(username):
    return {f'This is a profile page for {username}'}

# http://127.0.0.1:8000/cities?id=paris
@app.get('/cities')
def profile(id:str):
    return {f'This is a profile page for {id}'}

# http://127.0.0.1:8000/province?province=tuscany&&hours=20
@app.get('/province')
def province(province:str, hours:int):
    return {f'This is a province page for {province} and it takes to get there {hours}hours '}

# request body
# post api
# go to the 127.0.0.1:8000/docs
@app.post  ('/addUser')
def addUser(profile:Profile):
    return profile

