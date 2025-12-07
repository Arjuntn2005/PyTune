from pathlib import Path
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from pytune import generate_scale, get_available_scales

BASE_DIR = Path(__file__).resolve().parent.parent

app = FastAPI(title="PyTune API")

FRONTEND_DIR = BASE_DIR / "frontend"
if FRONTEND_DIR.exists():
    app.mount("/", StaticFiles(directory=str(FRONTEND_DIR), html=True), name="frontend")


class RunRequest(BaseModel):
    key: str
    scale_type: str


@app.post("/api/generate")
def generate(req: RunRequest):
    try:
        result = generate_scale(req.key, req.scale_type)
        return JSONResponse(content={"success": True, "data": result})
    except Exception as e:
        return JSONResponse(status_code=400, content={"success": False, "error": str(e)})


@app.get("/api/scales")
def list_scales():
    return {"scales": get_available_scales()}
