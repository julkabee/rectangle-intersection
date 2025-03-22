from typing import Optional

from fastapi import FastAPI, HTTPException

from src.geometry import Rectangle, calculate_intersection
from src.schemas import RectangleInput, RectangleOutput

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)    

app = FastAPI(
    title="Rectangle Intersection API",
    description="API для вычисления пересечения прямоугольников",
    version="1.0.0",
)

@app.post("/intersect", response_model=Optional[RectangleOutput])
async def intersect_rectangles(rect_b: RectangleInput):
    """Вычисляет пересечение прямоугольника A(0, 0, 1000, 500)
    с входным прямоугольником B"""
    logger.info(f"Received request with rect_b: {rect_b}")
    try:
        rectangle_b = Rectangle(rect_b.x, rect_b.y, rect_b.w, rect_b.h)
        result = calculate_intersection(rectangle_b)
        if result is None:
            logger.info("No intersection found")
            return None

        if result is None:
            return None

        x, y, w, h = result
        logger.info(f"Intersection found: x={x}, y={y}, w={w}, h={h}")
        return {"x": x, "y": y, "w": w, "h": h}
    except ValueError as e:
        logger.error(f"Invalid input: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
