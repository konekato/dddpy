from pydantic import BaseModel, Field


class EmployeeCreateModel(BaseModel):

    first_name:     str = Field(example="太郎")
    last_name:      str = Field(example="山田")
    age:            int = Field(ge=18, example=22)
    address:        str = Field(example="東京都港区")
    department_id:  int = Field(ge=1, example=999)
    hire_date:      int = Field(ge=0, example=1680680058)
    salary:         int = Field(ge=1, example=300000)