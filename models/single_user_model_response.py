from pydantic import BaseModel, HttpUrl
from typing import List, Optional


class UserData(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: HttpUrl  # автоматически проверит, что это валидный URL


class SupportInfo(BaseModel):
    url: Optional[HttpUrl]
    text: Optional[str]


class MetaInfo(BaseModel):
    powered_by: Optional[str]
    upgrade_url: Optional[HttpUrl]
    docs_url: Optional[HttpUrl]
    template_gallery: Optional[HttpUrl]
    message: Optional[str]
    features: Optional[List[str]]
    upgrade_cta: Optional[str]


class GetUserResponse(BaseModel):
    data: UserData
    support: SupportInfo
    _meta: Optional[MetaInfo]