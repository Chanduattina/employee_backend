from dotenv import load_dotenv
from fastapi import FastAPI, Body
from starlette.responses import Response
from datetime import date

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
def employee_details(id: int = None):
    if id is None:
        return None
    elif id > 4:
        return Response("Id does not exist", status_code=404)
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
def employee_details(id: int = None):
    if id is None:
        raise Exception("Enter the id")
    elif id > 3 or id < 1:
        raise Exception("id does not exist")
    else:
        return session.query(Employee).filter(Employee.id == id).one()


@app.post("/v2/update_employee/")
def update_yob(yob=Body(..., embed=True)):
    current_date = date.today()
    if yob <= current_date.year:
        db = Session()
        db.query(Employee).filter(Employee.yob == 1900). \
            update({Employee.yob: yob}, synchronize_session='evaluate')
        return db.query(Employee).filter(Employee.yob == yob).all()
    else:
        return Response("Check Year", status_code=404)


@app.post("/v2/update_employees/")
def update_yob_by_user(old_yob: int = Body(..., embed=True), new_yob: int = Body(..., embed=True)):
    current_date = date.today()
    if new_yob > current_date.year:
        raise Exception("Year does not exceed this year")
    db = Session()
    db.query(Employee).filter(Employee.yob == old_yob). \
        update({Employee.yob: new_yob}, synchronize_session=False)
    return db.query(Employee).filter(Employee.yob == new_yob).all()
