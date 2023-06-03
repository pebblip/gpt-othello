from pydantic import BaseModel, Field


class GptAnswerResponse(BaseModel):
    position: tuple[int, int] = Field(..., title="最善手", description="次の指し手を表す座標位置", example="(0, 0)")
    answer: str = Field(..., title="最善手の説明", description="次の指し手の説明", example="左上に置く")
