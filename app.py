from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from database import Base, engine, SessionLocal
from models import User
from auth import AuthManager

from routes import patients, visits, prescriptions, labs

# Create database tables
Base.metadata.create_all(bind=engine)

# Create default admin user
with SessionLocal() as db:
    existing = db.query(User).filter(User.username == "admin").first()
    if not existing:
        admin = User(
            username="admin",
            password_hash=AuthManager.hash_password("admin123"),
            role="admin",
        )
        db.add(admin)
        db.commit()

app = FastAPI(title="EMR Starter Project")

templates = Jinja2Templates(directory="templates")

# Include routers
app.include_router(patients.router)
app.include_router(visits.router)
app.include_router(prescriptions.router)
app.include_router(labs.router)


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/health")
def health_check():
    return {"status": "ok", "message": "EMR system is running"}
