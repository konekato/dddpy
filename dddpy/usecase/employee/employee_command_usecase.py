from abc import ABC, abstractmethod
from typing import Optional, cast

import shortuuid

from dddpy.domain.employee import (
    EmployeeRepository,
    Employee
)

from .employee_command_model import EmployeeCreateModel

from .employee_query_model import EmployeeReadModel


class EmployeeCommandUseCaseUnitOfWork(ABC):

    employee_repository: EmployeeRepository

    @abstractmethod
    def begin(self):
        raise NotImplementedError

    @abstractmethod
    def commit(self):
        raise NotImplementedError

    @abstractmethod
    def rollback(self):
        raise NotImplementedError


class EmployeeCommandUseCase(ABC):
    @abstractmethod
    def create_book(self, data: EmployeeCreateModel) -> Optional[EmployeeReadModel]:
        raise NotImplementedError


class EmployeeCommandUseCaseImpl(EmployeeCommandUseCase):

    def __init__(
        self,
        uow: EmployeeCommandUseCaseUnitOfWork,
    ):
        self.uow: EmployeeCommandUseCaseUnitOfWork = uow

    def create_book(self, data: EmployeeCreateModel) -> Optional[EmployeeReadModel]:
        try:
            uuid = shortuuid.uuid()
            employee = Employee(
                id=uuid,
                first_name=data.first_name,
                last_name=data.last_name,
                age=data.age,
                address=data.address,
                department_id=data.department_id,
                hire_date=data.hire_date,
                salary=data.salary,
            )

            self.uow.employee_repository.create(employee)
            self.uow.commit()

            created_employee = self.uow.employee_repository.find_by_id(uuid)
        except:
            self.uow.rollback()
            raise

        return EmployeeReadModel.from_entity(cast(Employee, created_employee))