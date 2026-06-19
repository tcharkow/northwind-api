# Northwind API

FastAPI backend serving Northwind ELT pipeline analytics — revenue trends, product performance, and customer LTV.

## Overview

REST API that queries dbt mart models from a PostgreSQL database and serves analytics results as JSON endpoints, consumed by a React + Plotly dashboard.

## Endpoints

- `GET /` — Health check
- `GET /api/revenue-by-month` — Monthly revenue trends (1996–1998)
- `GET /api/product-performance` — Revenue and units sold per product
- `GET /api/customer-ltv` — Lifetime value and order count per customer

## Tech Stack

- Python 3.11
- FastAPI
- Pandas
- psycopg2
- Uvicorn
- PostgreSQL 16

## Setup

1. Clone this repository
2. Create a virtual environment: `python -m venv venv`
3. Activate it: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Run the server: `uvicorn main:app --reload`

## Deployment

Deployed on Render.