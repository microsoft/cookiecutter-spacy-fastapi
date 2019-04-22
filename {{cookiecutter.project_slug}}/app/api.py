# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

from dotenv import load_dotenv, find_dotenv
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse
import spacy
import uvicorn

from app.models import AzureSearchDocumentsRequest, AzureSearchDocumentsResponse


load_dotenv(find_dotenv())
prefix = os.environ.get("CLUSTER_ROUTE_PREFIX")
if not prefix:
    prefix = ""
prefix = prefix.rstrip("/")


app = FastAPI(
    title="{{cookiecutter.project_name}}",
    version="1.0",
    description="{{cookiecutter.project_short_description}}",
    openapi_prefix=prefix
)

nlp = spacy.load('en_core_web_sm')


def extract_from_text(text: str):
    """Extract Spacy Named Entities from raw text"""
    entities = []
    for ent in nlp(text).ents:
        match = {
            "text": ent.text,
            "label": ent.label_,
            "start": ent.start_char,
            "end": ent.end_char,
        }
        entities.append(match)
    return entities


@app.get('/', include_in_schema=False)
def docs_redirect():
    return RedirectResponse(f'{prefix}/docs')


@app.post(
    "/spacy_entities",
    response_model=AzureSearchDocumentsResponse,
    tags=["NER", "Azure Search"],
)
async def extract_for_azure_search(body: AzureSearchDocumentsRequest):
    """Extract Named Entities from a batch of Azure Search Document Records.
        This route can be used directly as a Cognitive Skill in Azure Search
        For Documentation on integration with Azure Search, see here:
        https://docs.microsoft.com/en-us/azure/search/cognitive-search-custom-skill-interface"""

    res = []
    for val in body.values:
        ents = set([e["text"] for e in extract_from_text(val.data.text)])
        ents = sorted(list(ents), key=lambda s: s.lower())
        res.append(
            {
                "recordId": val.recordId,
                "data": {
                    "entities": ents
                }
            }
        )
    return {
        "values": res
    }
