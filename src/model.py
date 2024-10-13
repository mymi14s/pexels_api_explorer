from pydantic import BaseModel, Field
from base_model import *


class PageLengthModel(BaseModel):
    page: int | None = Field(None, ge=1)
    per_page:  int | None = Field(None, ge=1)

class SearchMediaModel(PageLengthModel):
    query: str
    orientation: Orientation | None = None
    size: Size | None = None
    color: str | None = Field(None, pattern="^(red|orange|yellow|green|turquoise|blue|violet|pink|brown|black|gray|white|#[0-9A-Fa-f]{6})$")
    locale: Locale | None = None

class MediaID(BaseModel):
    id: int

class PopularVideoModel(PageLengthModel):
    min_width: int | None = Field(None, ge=1)
    min_height: int | None = Field(None, ge=1)
    min_duration: int | None = Field(None, ge=1)
    max_duration: int | None = Field(None, ge=1)

class CollectionModel(PageLengthModel):
    type: Type | None = None
    sort: Sort | None = None