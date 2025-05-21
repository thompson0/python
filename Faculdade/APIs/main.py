from fastapi import FastAPI
from controllers import example_controller

app = FastAPI()

app.include_router(example_controller.router, prefix="/api", tags=["Examples"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)


#pip install fastapi uvicorn
