import json
from fastapi import FastAPI
from starlette.config import Config
from starlette.requests import Request
from starlette.middleware.sessions import SessionMiddleware
from starlette.responses import HTMLResponse, RedirectResponse
from authlib.integrations.starlette_client import OAuth, OAuthError
import json

config = Config('.env')
oauth = OAuth(config)

CONF_URL = 'https://accounts.google.com/.well-known/openid-configuration'
oauth.register(
    name='google',
    server_metadata_url=CONF_URL,
    client_kwargs={
        'scope': 'openid email profile'
    }
)

async def logout(request: Request):
    request.session.pop('user', None)
    return RedirectResponse(url='/')

async def callback(request: Request):
    user = request.session.get('user')
    if user:
        data = json.dumps(user)
        print(data)
        return HTMLResponse((f'{data}'))
    else:    
        return HTMLResponse((f'Need authentication')) 

async def auth(request: Request):
    try:
        token = await oauth.google.authorize_access_token(request)
    except OAuthError as error:
        return HTMLResponse(f'<h1>{error.error}</h1>')
    user = token.get('userinfo')
    if user:
        request.session['user'] = dict(user)
    return RedirectResponse(url='/')

async def login(request: Request):
    redirect_uri = request.url_for('auth')
    print(redirect_uri)
    return await oauth.google.authorize_redirect(request, redirect_uri)

async def homepage(request: Request):
    user = request.session.get('user')
    if user:
        data = json.dumps(user)
        html = (
            f'<pre>{data}</pre>'
            '<a href="/logout">logout</a>'
        )
        return HTMLResponse(html)
    return HTMLResponse('<a href="/login">login</a>')
