from fastapi import FastAPI, APIRouter
import uvicorn

from Init import init
from University import university_router

app = FastAPI()
app.include_router(university_router)

init()

@app.get("/")
def read_root():
    return {"Hello": "World 2"}

if __name__ == "__main__":
    init()
    PORT = 8088
    uvicorn.run(app, host="0.0.0.0", port=PORT)