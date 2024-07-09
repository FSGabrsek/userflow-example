import requests

client_id = ""
client_secret = ""

app_id = ""
role_id = ""

def client_credentials():
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

def post_assignment(user_id: str):
    r = requests.post(
        f"https://graph.microsoft.com/v1.0/users/{user_id}/appRoleAssignments",
        headers={ 
            "Authorization": f"Bearer {client_credentials()}",
            "Content-Type": "application/json",
        },
        json={
            "principalId": user_id,
            "resourceId": app_id,
            "appRoleId": role_id
        })
    
    return r.json()

def get_assignment(user_id: str):
    r = requests.get(
        f"https://graph.microsoft.com/v1.0/users/{user_id}/appRoleAssignments?$filter=resourceId eq {app_id}",
        headers={ "Authorization": f"Bearer {client_credentials()}" })
    
    return r.json()

def revoke_assignment(user_id):
    r = requests.delete(
        f"https://graph.microsoft.com/v1.0/users/{user_id}/appRoleAssignments/{get_assignment(user_id)["value"][0]["id"]}",
        headers={ "Authorization": f"Bearer {client_credentials()}" })
    
    return r.ok

