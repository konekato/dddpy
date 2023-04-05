from typing import cast

from pydantic import BaseModel, Field

from dddpy.domain.employee import Employee


class EmployeeReadModel(BaseModel):

    id:             str = Field(example="vytxeTZskVKR7C7WgdSP3d")
    first_name:     str = Field(example="太郎")
    last_name:      str = Field(example="山田")
    age:            int = Field(ge=18, example=22)
    address:        str = Field(example="東京都港区")
    department_id:  int = Field(ge=1, example=999)
    hire_date:      int = Field(ge=0, example=1680680058000)
    salary:         int = Field(ge=1, example=300000)
    created_at:     int = Field(example=1136214245000)
    updated_at:     int = Field(example=1136214245000)

    class Config:
        orm_mode = True

    @staticmethod
    def from_entity(employee: Employee) -> "EmployeeReadModel":
        return EmployeeReadModel(
            id=employee.id,
            first_name=employee.first_name,
            last_name=employee.last_name,
            age=employee.age,
            address=employee.address,
            department_id=employee.department_id,
            hire_date=employee.hire_date,
            salary=employee.salary,
            created_at=cast(int, employee.created_at),
            updated_at=cast(int, employee.updated_at),
        )