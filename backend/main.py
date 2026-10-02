from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from routes.auth import router as auth_router
from routes.home import router as home_router
from routes.party import router as party_router
from routes.jewelry import router as jewelry_router
from routes.history import router as history_router
app = FastAPI(title="PocketSmart AI")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount("/static", StaticFiles(directory="../frontend/static"), name="static")
templates = Jinja2Templates(directory="../frontend/templates")
app.include_router(auth_router)
app.include_router(home_router)
app.include_router(party_router)
app.include_router(jewelry_router)
app.include_router(history_router)
@app.get("/")
def home_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"request": request}
    )
@app.get("/dashboard")
def dashboard_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="dashboard.html",
        context={"request": request}
    )
@app.get("/home-planner")
def home_planner(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="home_planner.html",
        context={"request": request}
    )
@app.get("/party-planner")
def party_planner(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="party_planner.html",
        context={"request": request}
    )
@app.get("/jewelry-planner")
def jewelry_planner(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="jewelry_planner.html",
        context={"request": request}
    )
@app.get("/login")
def login_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="login.html",
        context={"request": request}
    )
@app.get("/register")
def register_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="register.html",
        context={"request": request}
    )
@app.get("/history-page")
def history_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="history.html",
        context={"request": request}
    )
