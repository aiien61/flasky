from my_app import app
from flask import current_app
from termcolor import colored

try:
    app_ctx = app.app_context()
    app_ctx.push()
    print(current_app.name)

    print(app.url_map)
    
    app_ctx.pop()
    print(current_app.name)
except RuntimeError as e:
    print(colored(e, 'red'))
