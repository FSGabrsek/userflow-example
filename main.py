import requests
from os import getenv

## Local only, remove in function app
from dotenv import load_dotenv
load_dotenv()
##

client_id = getenv("CLIENT_ID")
client_secret = getenv("CLIENT_SECRET")

app_principal_id = getenv("APP_PRINCIPAL_ID")
role_id = getenv("ROLE_ID")

# request a token for an application client with User.ReadWrite.All permissions
def client_credentials() -> str:
    r = requests.post(
        "https://login.microsoftonline.com/myhmb2c.onmicrosoft.com/oauth2/v2.0/token",
        headers={ "Content-Type": "application/x-www-form-urlencoded" },
        data={
            "client_id": client_id,
            "scope": "https://graph.microsoft.com/.default",
            "client_secret": client_secret,
            "grant_type": "client_credentials"
        })

    return r.json()["access_token"]

# POST a new appRoleAssigment for the app resource principal on the user
def grant_assignment(user_id: str) -> dict:
    r = requests.post(
        f"https://graph.microsoft.com/v1.0/users/{user_id}/appRoleAssignments",
        headers={ 
            "Authorization": f"Bearer {client_credentials()}",
            "Content-Type": "application/json",
        },
        json={
            "principalId": user_id,
            "resourceId": app_principal_id,
            "appRoleId": role_id
        })
    
    return r.json()

# GET appRoleAssignments filtered for the app resource and return the first assignment
def get_assignment(user_id: str) -> dict:
    r = requests.get(
        f"https://graph.microsoft.com/v1.0/users/{user_id}/appRoleAssignments?$filter=resourceId eq {app_principal_id}",
        headers={ "Authorization": f"Bearer {client_credentials()}" })
    
    return r.json()

# DELETE the appRoleAssignment for the user on the app resource principal
def revoke_assignment(user_id: str) -> bool:
    r = requests.delete(
        f"https://graph.microsoft.com/v1.0/users/{user_id}/appRoleAssignments/{get_assignment(user_id)["value"][0]["id"]}",
        headers={ "Authorization": f"Bearer {client_credentials()}" })
    
    return r.ok