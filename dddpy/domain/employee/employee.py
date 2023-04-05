from typing import Optional


class Employee:
    """Employee はエンティティとして社員の集合を表す。"""

    def __init__(
        self,
        id:             str,
        first_name:     str,
        last_name:      str,
        age:            int,
        address:        str,
        department_id:  int,
        hire_date:      int,
        salary:         int,
        created_at:     Optional[int] = None,
        updated_at:     Optional[int] = None,
    ):
        self.id: str = id
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.age: int = age
        self.address: str = address
        self.department_id: int = department_id
        self.hire_date: int = hire_date
        self.salary: int = salary
        self.created_at: Optional[int] = created_at
        self.updated_at: Optional[int] = updated_at

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Employee):
            return self.id == o.id

        return False