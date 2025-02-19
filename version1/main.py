import os
from pydantic import BaseModel
from fastapi import FastAPI, Request, HTTPException, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# In-memory storage for issues
issues = []

# Templates for HTML rendering
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

# Models
class Issue(BaseModel):
    id: int  # Fixed: id should be an integer
    title: str
    description: str

# Generate next id for new issues
def get_next_id():
    return max((issue.id for issue in issues), default=0) + 1

# Endpoints
@app.get("/", response_class=HTMLResponse)
async def root(req: Request):
    return templates.TemplateResponse("index.html", {"request": req, "issues": issues})

@app.post("/create_issue/")
async def create_issue(title: str = Form(...), description: str = Form(...)):
    new_issue = Issue(id=get_next_id(), title=title, description=description)
    issues.append(new_issue)
    return RedirectResponse(url="/", status_code=303)

@app.get("/issue/{issue_id}")
async def get_issue(issue_id: int, request: Request):
    issue = next((i for i in issues if i.id == issue_id), None)
    if not issue:
        raise HTTPException(status_code=404, detail="Issue not found!")
    return templates.TemplateResponse("issue_details.html", {"request": request, "issue": issue})

# api endpoints
@app.post("/api/v1/create_issue/")
async def create_issue(title: str = Form(...), description: str = Form(...)):
    new_issue = Issue(id=get_next_id(), title=title, description=description)
    issues.append(new_issue)
    return {"message": "Issue created!", "issue": new_issue.id} # API Testing

@app.get("/api/v1/issue/{issue_id}")
async def get_issue(issue_id: int, request: Request):
    issue = next((i for i in issues if i.id == issue_id), None)
    if not issue:
        raise HTTPException(status_code=404, detail="Issue not found!")
    return issue

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
