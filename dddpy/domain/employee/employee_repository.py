from abc import ABC, abstractmethod
from typing import Optional

from dddpy.domain.employee import Employee


class EmployeeRepository(ABC):
    """Employee エンティティのリポジトリインターフェースを定義。"""

    @abstractmethod
    def create(self, employee: Employee) -> Optional[Employee]:
        raise NotImplementedError

    @abstractmethod
    def find_by_id(self, id: str) -> Optional[Employee]:
        raise NotImplementedError