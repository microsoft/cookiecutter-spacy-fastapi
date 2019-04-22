# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from typing import Dict, List, Optional
from pydantic import BaseModel, Schema


class RecordDataRequest(BaseModel):
    text: str
    language: str = "en"


class RecordRequest(BaseModel):
    recordId: str
    data: RecordDataRequest


class RecordsRequest(BaseModel):
    values: List[RecordRequest]


class RecordDataResponse(BaseModel):
    entities: List[str]


class RecordResponse(BaseModel):
    recordId: str
    data: RecordDataResponse
    errors: Optional[List[str]]
    warnings: Optional[List[str]]


class RecordsResponse(BaseModel):
    values: List[RecordResponse]
