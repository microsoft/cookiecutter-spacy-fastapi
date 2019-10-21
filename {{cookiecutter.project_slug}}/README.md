# {{cookiecutter.project_name}}

{{cookiecutter.project_short_description}}

---

## Azure Search Cognitive Skills
For instructions on adding your API as a Custom Cognitive Skill in Azure Search see:
https://docs.microsoft.com/en-us/azure/search/cognitive-search-custom-skill-interface

## Resources
This project uses FastAPI built on top of Starlette.

FastAPI documenation:

https://fastapi.tiangolo.com

---

## Run Locally
To run locally in debug mode run:

```
cd ./{{cookiecutter.project_slug}}
uvicorn app.api:app --reload
```
Open your browser to http://localhost:8000/docs to view the SwaggerUI.

For an alternate view of the docs navigate to http://localhost:8000/redoc

---

