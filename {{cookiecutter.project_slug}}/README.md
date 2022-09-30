# {{cookiecutter.project_name}}

{{cookiecutter.short_description}}

---

## Azure Search Cognitive Skills
For instructions on adding your API as a Custom Cognitive Skill in Azure Search see:
https://docs.microsoft.com/en-us/azure/search/cognitive-search-custom-skill-interface

## Resources
This project has two key dependencies:

| Dependency Name | Documentation                | Description                                                                            |
|-----------------|------------------------------|----------------------------------------------------------------------------------------|
| spaCy           | https://spacy.io             | Industrial-strength Natural Language Processing (NLP) with Python and Cython           |
| FastAPI         | https://fastapi.tiangolo.com | FastAPI framework, high performance, easy to learn, fast to code, ready for production |
---

## Run Locally
To run locally in debug mode run:

```
cd ./{{cookiecutter.project_slug}}
bash ./create_virtualenv.sh
uvicorn app.api:app --reload
```
Open your browser to http://localhost:8000/docs to view the OpenAPI UI.

![Open API Image](./images/cookiecutter-docs.png)


For an alternate view of the docs navigate to http://localhost:8000/redoc

---

## Deploy with Azure Pipelines
Follow this guide to setup an Azure Resource Group with instances of Azure Kubernetes Service and Azure Container Registry and setup CI / CD with Azure Pipelines.

https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/kubernetes/aks-template?view=azure-devops
