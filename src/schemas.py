from pydantic import BaseModel, Field


class RectangleInput(BaseModel):
    x: float
    y: float
    w: float
    h: float


class RectangleOutput(BaseModel):
    x: float
    y: float
    w: float
    h: float
