from fastapi import FastAPI
from typing import List

# 建立 FastAPI 應用
app = FastAPI()

# 商品資料
products = [
    {"id": 1, "name": "筆記型電腦", "price": 30000},
    {"id": 2, "name": "智慧型手機", "price": 15000},
    {"id": 3, "name": "耳機", "price": 2000},
]

# 定義路由來獲取所有商品的名稱與價格
@app.get("/products", response_model=List[dict])
async def get_products():
    # 僅回傳名稱與價格
    return [{"name": product["name"], "price": product["price"]} for product in products]

    