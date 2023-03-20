from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import RedirectResponse
import requests
from starlette.config import Config

app = FastAPI()

config = Config('.env')

# Define Facebook Login settings
APP_ID = config.__dict__['file_values']['FACEBOOK_APP_ID']
APP_SECRET = config.__dict__['file_values']['FACEBOOK_APP_SECRET']
REDIRECT_URI = "http://localhost:8000/auth/facebook/"
SCOPE = "public_profile,email,manage_pages"

# Define OAuth2 dependencies
def get_facebook_access_token(code: str):
    """
    Exchange Facebook authorization code for access token
    """
    print(APP_ID)
    response = requests.get(
        f"https://graph.facebook.com/v13.0/oauth/access_token?client_id={APP_ID}&redirect_uri={REDIRECT_URI}&client_secret={APP_SECRET}&code={code}"
    )
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())
    return response.json()["access_token"]

def get_facebook_user_info(access_token: str):
    """
    Retrieve Facebook user profile information
    """
    response = requests.get(
        f"https://graph.facebook.com/v13.0/me?fields=id,name,email&access_token={access_token}"
    )
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())
    return response.json()

def get_facebook_pages(access_token: str):
    """
    Retrieve Facebook Pages associated with user
    """
    response = requests.get(
        f"https://graph.facebook.com/v13.0/me/accounts?access_token={access_token}"
    )
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())
    return response.json()["data"]

def get_facebook_shop_page(pages):
    """
    Find Facebook Page with 'shop' page type
    """
    for page in pages:
        if page["category"] == "SHOP":
            return page
    return None


async def login():
    """
    Redirect user to Facebook Login page
    """
    return RedirectResponse(
        f"https://www.facebook.com/v13.0/dialog/oauth?client_id={APP_ID}&redirect_uri={REDIRECT_URI}&scope={SCOPE}"
    )


async def callback(code: str):
    """
    Handle Facebook Login callback and retrieve user data
    """
    access_token = get_facebook_access_token(code)
    user_info = get_facebook_user_info(access_token)
    pages = get_facebook_pages(access_token)
    shop_page = get_facebook_shop_page(pages)
    
    if shop_page is None:
        raise HTTPException(status_code=404, detail="User has no Facebook Shop page")
    
    # Do something with user data and return response
    return {"user_info": user_info, "shop_page": shop_page}
