# model-management-server

## to run the server

```bash
uvicorn main:app --reload
```

## to fetch all required dependencies

```bash
pip install -r requirements.txt
```

## to generate the requirements.txt file

```bash
pipreqs . --ignore ".venv" --force
```

## to run the tests

```bash
pytest
```
