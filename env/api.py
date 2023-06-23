from fastapi import FastAPI
from rooter import router


app = FastAPI()
app.include_router(router)
@app.get("/")
async def home():
    return {"message": "Bonjour Genie Logiciel"}

app.include_router(router)