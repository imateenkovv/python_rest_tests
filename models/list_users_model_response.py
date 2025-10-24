from pydantic import BaseModel, HttpUrl
from typing import List, Optional


class Data(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str


class Support(BaseModel):
    url: Optional[str]
    text: Optional[str]


class Meta(BaseModel):
    powered_by: Optional[str]
    upgrade_url: Optional[str]
    docs_url: Optional[str]
    template_gallery: Optional[str]
    message: Optional[str]
    features: Optional[List[str]]
    upgrade_cta: Optional[str]


class AllObject(BaseModel):
    page: int
    per_page: int
    total: int
    total_pages: int
    data: List[Data]
    support: Support
