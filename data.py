from pydantic import BaseModel

geetha_record = {"details": "Geetha", "id": 1, "yob": 2002}
chandu_record = {"details": "Chandu", "id": 2, "yob": 2002}
ravin_record = {"name": "Ravin", "id": 3, "yob": 1982}
sudharsan_record = {"name": "sudar", "id": 4, "yob": 2002}

employees = [geetha_record, chandu_record, ravin_record,sudharsan_record]

employees_map = dict()
for each_employee in employees:
    employees_map[each_employee["id"]] = each_employee


# test comment
class Item(BaseModel):
    id: int
    name: str
    yob: str


class Year(BaseModel):
    yob = int
