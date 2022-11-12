from data import employees, employees_map


def find_employee_by_id(employee_id: int):

    for employee in employees:
        if employee["id"] == employee_id:
            return employee


def fast_find_employee_by_id(id_of_employee: int):
    if id_of_employee is None:
        return None
    return employees_map[id_of_employee]









