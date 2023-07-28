from fastapi import FastAPI
from pydantic import BaseModel, Field

class Profile(BaseModel):
    name: str = Field(title ="Name of your User", description="Please enter the name of the User")
    email: str
    age: int
    
class Product (BaseModel):
    name: str
    price: int
    discount: int
    discounted_price: float
    
class User (BaseModel):
    name: str
    email: str

tags_metadata = [
    {
        "name": "buy",
        "description": "Post **User** and **Item price** information",
    },
]

app = FastAPI(
        title="FASTAPI Management System",
    description="API to get and create users.",
    version="1.1.2",
    openapi_tags=tags_metadata,
)



#passing multiple models
@app.post('/purchase', tags=["purchase"])
def purchase(user:User, product:Product):
    return{'user': user, 'product':product}

# passing path and query  paramerters to request
# go to 127.0.0.1:800/docs
# response body will product the number product_id
# you should see  product and category as requered in  docs
	
# Response body
# Download
# {
#   "product_id": 324,
#   "product": {
#     "name": "string",
#     "price": 0,
#     "discount": 0,
#     "discounted_price": 0
#   },
#   "category": "phone"
# }

@app.post('/addProduct/{product_id}')
def addProduct(product:Product, product_id:int, category:str):
    product.discounted_price = product.price-\
    (product.price * product.discount)/100
    return {"product_id":product_id, "product":product, "category":category }

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

