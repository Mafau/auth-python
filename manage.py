import os
from app.main import create_app
from flask import request, escape

app = create_app(os.getenv('ENVIRONMENT') or 'dev')


@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

