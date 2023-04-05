from typing import Optional

from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.session import Session

from dddpy.domain.employee import EmployeeRepository, Employee
from dddpy.usecase.employee import EmployeeCommandUseCaseUnitOfWork
from .employee_dto import EmployeeDTO


class EmployeeRepositoryImpl(EmployeeRepository):

    def __init__(self, session: Session):
        self.session: Session = session

    def create(self, employee: Employee):
        employee_dto = EmployeeDTO.from_entity(employee)

        try:
            self.session.add(employee_dto)
        except:
            raise
    
    def find_by_id(self, id: str) -> Optional[Employee]:
        try:
            employee_dto: EmployeeDTO = self.session.query(EmployeeDTO).filter_by(id=id).one()
        except NoResultFound:
            return None
        except:
            raise

        return employee_dto.to_entity()


class EmployeeCommandUseCaseUnitOfWorkImpl(EmployeeCommandUseCaseUnitOfWork):
    def __init__(
        self,
        session: Session,
        employee_repository: EmployeeRepository
    ):
        self.session: Session = session
        self.employee_repository: EmployeeRepository = employee_repository

    def begin(self):
        self.session.begin()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()