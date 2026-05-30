from pydantic import BaseModel

class CreditRequest(BaseModel):
    EXT_SOURCE_2: float
    EXT_SOURCE_3: float
    AMT_CREDIT: float
    DEBT_TO_INCOME: float
    EMPLOYMENT_LEN: int
    AGE: int