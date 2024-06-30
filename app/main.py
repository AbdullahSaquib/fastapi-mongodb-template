from bson import ObjectId
from fastapi import FastAPI, HTTPException
from app.db import db
from app.schema import Item


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    result = await db["items"].insert_one(item.model_dump())
    if result.inserted_id:
        return {"id": str(result.inserted_id)}
    raise HTTPException(status_code=400, detail="Item not inserted")


@app.get("/items/{item_id}")
async def read_item(item_id: str):
    item = await db["items"].find_one({"_id": ObjectId(item_id)})
    if item:
        item["_id"] = str(item["_id"])
        return item
    raise HTTPException(status_code=404, detail="Item not found")


@app.put("/items/{item_id}")
async def update_item(item_id: str, item: Item):
    result = await db["items"].update_one(
        {"_id": ObjectId(item_id)},
        {"$set": item.model_dump()}
    )
    if result.modified_count:
        return {"message": "Item updated successfully"}
    if result.matched_count:
        return {"message": "Item already updated!"}
    raise HTTPException(status_code=404, detail="Item not found")


@app.delete("/items/{item_id}")
async def delete_item(item_id: str):
    result = await db["items"].delete_one({"_id": ObjectId(item_id)})
    if result.deleted_count:
        return {"message": "Item deleted successfully"}
    raise HTTPException(status_code=404, detail="Item not found")


@app.get("/items/")
async def read_items():
    items = []
    cursor = db["items"].find()
    async for item in cursor:
        item["_id"] = str(item["_id"])
        items.append(item)
    # results = await cursor.to_list(10)
    return items


@app.get("/items/aggregate/")
async def aggregate_items():
    pipeline = [
        {"$match": {"name": {"$exists": True}}},
        {"$group": {"_id": "$name", "count": {"$sum": 1}}}
    ]
    cursor = db["items"].aggregate(pipeline)
    results = []
    async for doc in cursor:
        results.append(doc)
    # results = await cursor.to_list(10)
    return results
