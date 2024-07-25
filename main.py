from fastapi import FastAPI
import uvicorn

app = FastAPI(
    title="ZAL"
)

@app.get('/')
def main():
    return "ZAL"

if __name__ == '__main__':
    uvicorn.run('main:app',reload=True)