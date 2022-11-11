from dotenv import load_dotenv
from fastapi import FastAPI, Body

from data import employees, Item, Year
from database import session, Session
from models import Employee
from utils import fast_find_employee_by_id, find_employee_by_id

load_dotenv('.env')

app = FastAPI()


@app.get("/all_employees/")
def employee_details():
    return employees


@app.get("/employee/")
def employe_details(id: int = None):
    if id is None:
        return None
    return find_employee_by_id(id)


@app.get("/ping")
def ping():
    return "pong"


@app.get("/v2/employee")
def get_employee_rec_fast(id: int = None):
    if id is None:
        return None
    return fast_find_employee_by_id(id)


@app.post("/update_employee_data/")
def update_employee_data(data: Item):
    employees.append(data.dict())
    return {"updated list": employees}


@app.get("/v2/all_employee/")
def get_employee_details():
    return session.query(Employee).all()


@app.get("/v2/employee_/")
def employe_details(id: int = None):
    if id is None:
        return None
    return session.query(Employee).filter(Employee.id == id).one()


@app.post("/v2/update_employee")
def update_data(yob=Body(..., embed=True)):
    db = Session()
    db.query(Employee).filter(Employee.yob == 1900). \
            update({Employee.yob: yob}, synchronize_session='evaluate')
    return db.query(Employee).filter(Employee.yob == yob).all()
