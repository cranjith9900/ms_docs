from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

# ------------------ APP ------------------
app = FastAPI(
    title="FastAPI Backend",
    description="Backend API for Next.js frontend",
    version="1.0.0"
)

# ------------------ CORS ------------------
# Allow Next.js frontend to call this API
# (Later replace "*" with your deployed frontend URL)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ------------------ MODELS ------------------
class HelloRequest(BaseModel):
    name: str = Field(..., min_length=1, example="Ranjith")


class HelloResponse(BaseModel):
    message: str
    success: bool


# ------------------ ROUTES ------------------

# Health check (used by Azure & monitoring)
@app.get("/", tags=["Health"])
async def health():
    return {"status": "ok", "service": "fastapi-backend"}


# Main API endpoint (called from Next.js)
@app.post("/hello", response_model=HelloResponse, tags=["Greeting"])
async def say_hello(payload: HelloRequest):
    name = payload.name.strip()

    if not name:
        raise HTTPException(status_code=400, detail="Name cannot be empty")

    return HelloResponse(
        message=f"Hello {name} 👋",
        success=True
    )


# Example extra endpoint (good practice)
@app.get("/api/time", tags=["Utility"])
async def get_server_time():
    from datetime import datetime
    return {"server_time": datetime.utcnow().isoformat() + "Z"}

