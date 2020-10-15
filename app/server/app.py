from fastapi import FastAPI

from server.routes.student import router as student_router


app = FastAPI()


app.include_router(student_router, tags=["Student"], prefix="/student")


@app.get("/", tags=["Root"])
async def read_root():
    return {'message': 'Testing fastapi'}
