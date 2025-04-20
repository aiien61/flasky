from hello import app
from flask import current_app
from icecream import ic

try:
    print("before application context is activated")
    ic(current_app.name)
except RuntimeError as e:
    ic(e)


try:
    print("after application context has been activated")
    app_ctx = app.app_context()
    app_ctx.push()
    
    ic(current_app.name)
    ic(app.url_map)
    
    app_ctx.pop()
except RuntimeError as e:
    ic(e)