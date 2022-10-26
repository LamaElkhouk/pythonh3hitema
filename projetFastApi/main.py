from fastapi import FastAPI

app = FastAPI()

products = [
    {"id": 1, "name": "iPad", "price": 599},
    {"id": 2, "name": "iPhone", "price": 999},
    {"id": 3, "name": "iWatch", "price": 699},
]
#methode CRUD : Create Read Update Delete

#get
@app.get("/")
async def get_all():
    return products

@app.get("/products/{id}")
async def get_one_product(id: int):
    return products[id]

@app.get("products/{id}/{price}")
async def get_product_price(id:int):
    return products[price]

#post

@app.post("/")
async def add_product(id:int,name:str,price:float):
    new_product={"id":id,"name":name,"price":price}
    products.append(new_product)
    return products

#update

@app.put("/")
async def edit_product(id:int,name:str,price:float):
    products_field=products[id]
    products_field["name"]=name
    products_field["price"]=price

    products[id]=products_field
    return products[id]

#delete

@app.delete("/{id}")
async def delete_product(id:int):
    product=products[id]
    products.remove(product)
    return {"message":"delete product"}

