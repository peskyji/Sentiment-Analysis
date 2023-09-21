# web: uvicorn fastapi_app:app --host 0.0.0.0 --port $PORT
gunicorn -w 2 -k uvicorn.workers.UvicornWorker fastapi_app:app

