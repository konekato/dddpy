from datetime import datetime
from typing import Union

from sqlalchemy import Column, Integer, String

from dddpy.infrastructure.sqlite.database import Base
from dddpy.domain.employee import Employee


def unixtimestamp() -> int:
    return int(datetime.now().timestamp() * 1000)


class EmployeeDTO(Base):

    __tablename__ = "employee"
    id:             Union[str, Column] = Column(String, primary_key=True, autoincrement=False)
    first_name:     Union[str, Column] = Column(String, nullable=False)
    last_name:      Union[str, Column] = Column(String, nullable=False)
    age:            Union[int, Column] = Column(Integer, nullable=False)
    address:        Union[str, Column] = Column(String, nullable=False)
    department_id:  Union[int, Column] = Column(Integer, nullable=False)
    hire_date:      Union[int, Column] = Column(Integer, nullable=False)
    salary:         Union[int, Column] = Column(Integer, nullable=False)
    created_at:     Union[int, Column] = Column(Integer, index=True, nullable=False)
    updated_at:     Union[int, Column] = Column(Integer, index=True, nullable=False)

    def to_entity(self) -> Employee:
        return Employee(
            id=self.id,
            first_name=self.first_name,
            last_name=self.last_name,
            age=self.age,
            address=self.address,
            department_id=self.department_id,
            hire_date=self.hire_date,
            salary=self.salary,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )

    @staticmethod
    def from_entity(employee: Employee) -> "EmployeeDTO":
        now = unixtimestamp()
        return EmployeeDTO(
            id=employee.id,
            first_name=employee.first_name,
            last_name=employee.last_name,
            age=employee.age,
            address=employee.address,
            department_id=employee.department_id,
            hire_date=employee.hire_date,
            salary=employee.salary,
            created_at=now,
            updated_at=now,
        )

    