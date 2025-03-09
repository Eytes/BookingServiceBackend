from fastapi import FastAPI
from contextlib import asynccontextmanager
from routers.admin import router as admin_router
from config import db

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Connected to MongoDB")
    yield
    db.client.close()
    print("Disconnected from MongoDB")

app = FastAPI(title="BookingService Backend", lifespan=lifespan)

@app.get("/")
async def root():
    return {"message": "BookingService Backend is running!"}

app.include_router(admin_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)