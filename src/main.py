from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from UniversityController import university_router, authenticator_router, student_router, teacher_router, course_router
from Init import init

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(university_router)
app.include_router(authenticator_router)
app.include_router(student_router)
app.include_router(teacher_router)
app.include_router(course_router)

init()

@app.get("/")
async def root():
    return {"message": "Hello World"}