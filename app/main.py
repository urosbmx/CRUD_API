from fastapi import FastAPI, HTTPException
from fastapi_sqlalchemy import DBSessionMiddleware, db
from pydantic import BaseModel
from model import Item,Base
from sqlalchemy import create_engine

DATABASE_URL = "sqlite:///item.db"

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(DBSessionMiddleware, db_url=DATABASE_URL)


class ItemCreate(BaseModel):
    name: str
    description: str


class ItemResponse(BaseModel):
    id: int
    name: str
    description: str



@app.get("/items", response_model=list[ItemResponse], status_code=200)
async def get_items():
    items = db.session.query(Item).all()
    return items

@app.get("/item/{id}",response_model=ItemResponse,status_code=200)
async def get_item_by_id(id):
    if not isinstance(id, int):
        raise HTTPException(status_code=400, detail="ID must be Integer")
    db_item = db.session.get(Item, id)
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@app.get("/item_name/{name}",response_model=list[ItemResponse],status_code=200)
async def get_item_by_name(name:str):
    db_item = db.session.query(Item).filter(Item.name == name).all()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item doesn't exist")
    return db_item

@app.post("/items", response_model=ItemResponse)
async def create_item(item: ItemCreate):
    new_item = Item(name=item.name, description=item.description)
    db.session.add(new_item)
    db.session.commit()
    db.session.refresh(new_item)
    return new_item

@app.put("/items/{item_id}", response_model=ItemResponse)
async def update_item(item_id: int, item: ItemCreate):
    db_item = db.session.get(Item, item_id)
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")

    db_item.name = item.name
    db_item.description = item.description
    db.session.commit()
    db.session.refresh(db_item)
    return db_item


@app.delete("/items/{item_id}", status_code=204)
async def delete_item(item_id: int):
    db_item = db.session.get(Item, item_id)
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")

    db.session.delete(db_item)
    db.session.commit()
