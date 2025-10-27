from pydantic import BaseModel, HttpUrl
from typing import List, Optional


class user_data(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: HttpUrl  # автоматически проверит, что это валидный URL


class support_info(BaseModel):
    url: Optional[HttpUrl]
    text: Optional[str]


class meta_info(BaseModel):
    powered_by: Optional[str]
    upgrade_url: Optional[HttpUrl]
    docs_url: Optional[HttpUrl]
    template_gallery: Optional[HttpUrl]
    message: Optional[str]
    features: Optional[List[str]]
    upgrade_cta: Optional[str]


class get_user_response(BaseModel):
    data: user_data
    support: support_info
    _meta: Optional[meta_info]