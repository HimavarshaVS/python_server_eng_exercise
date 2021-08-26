import uvicorn
from app.main import create_app
from fastapi_pagination import Page, add_pagination
app = create_app()
add_pagination(app)

if __name__ == "__main__":
    uvicorn.run("run:app", host="0.0.0.0", port=5081, log_level="info", reload=True)