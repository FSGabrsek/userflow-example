# Userflow example
Python userflow for registering users to the myHolmatroPortal application.

__Requires:__ Python >=3.8 

## Initialize project
1. run `make install` to create a venv in the current working directory and install the project.
2. activate the venv and start the `python` interactive shell.
3. import the main file and run the `grant_assignment` or `revoke_assignment` methods.
```python
(venv) \userflow-example> python
Python 3.12.2 (tags/v3.12.2:6abddd9, Thu  1 1970, 00:00:00) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> from main import grant_assignment, revoke_assignment
>>> grant_assignment("00000000-0000-0000-0000-000000000000")
{'@odata.context': "https://graph.microsoft.com/v1.0/$metadata#users('00000000-0000-0000-0000-000000000000')/appRoleAssignments/$entity", 'id': '00000000-0000-0000-0000-000000000000', 'deletedDateTime': None, 'appRoleId': '00000000-0000-0000-0000-000000000000', 'createdDateTime': '1970-01-01T00:00:00.0000000Z', 'principalDisplayName': 'FSGabrsek', 'principalId': '00000000-0000-0000-0000-000000000000', 'principalType': 'User', 'resourceDisplayName': 'myHolmatroPortal', 'resourceId': '00000000-0000-0000-0000-000000000000'}
>>> revoke_assignment("00000000-0000-0000-0000-000000000000")
True
>>> exit()
(venv) \userflow-example>
```

### Final steps
* run `make clean` to delete the venv and clean up any cache files