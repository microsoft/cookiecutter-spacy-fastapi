from typing import Dict, List, Optional
from pydantic import BaseModel, Schema


class AzureSearchDocumentDataRequest(BaseModel):
    text: str
    language: str = "en"


class AzureSearchDocumentRequest(BaseModel):
    recordId: str
    data: AzureSearchDocumentDataRequest


class AzureSearchDocumentsRequest(BaseModel):
    values: List[AzureSearchDocumentRequest]


class AzureSearchDocumentDataResponse(BaseModel):
    entities: List[str]


class AzureSearchDocumentResponse(BaseModel):
    recordId: str
    data: AzureSearchDocumentDataResponse
    errors: Optional[List[str]]
    warnings: Optional[List[str]]


class AzureSearchDocumentsResponse(BaseModel):
    values: List[AzureSearchDocumentResponse]
