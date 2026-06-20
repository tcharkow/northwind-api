import os
import psycopg2
import pandas as pd
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_connection():
    return psycopg2.connect(os.environ.get("DATABASE_URL"))

@app.get("/")
def health_check():
    return {"status": "ok"}

@app.get("/api/revenue-by-month")
def revenue_by_month():
    conn = get_connection()
    df = pd.read_sql("SELECT * FROM public.revenue_by_month", conn)
    conn.close()
    return df.to_dict(orient="records")

@app.get("/api/product-performance")
def product_performance():
    conn = get_connection()
    df = pd.read_sql("SELECT * FROM public.product_performance", conn)
    conn.close()
    return df.to_dict(orient="records")

@app.get("/api/customer-ltv")
def customer_ltv():
    conn = get_connection()
    df = pd.read_sql("SELECT * FROM public.customer_ltv", conn)
    conn.close()
    df = df.where(pd.notnull(df), None)
    return df.to_dict(orient="records")