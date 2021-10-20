# **_Address Api_**

## **_Endpoints_**

* GET /api/address/

    This endpoint will return all the addresses saved in the database related to the logged in user.
    If successfull will return HTTP 200 OK.
    If unsuccessfull will return HTTP 404.

* GET /api/address/{address_id}
    
    This endpoint will return the address with the `id` specified in the url saved in the database related to the logged in user.
    If successfull will return HTTP 200 OK.
    If unsuccessfull will return HTTP 404.

* POST /api/address/

    This endpoint will save the new address created by the user to the database.
    If successfull will return HTTP 200 OK.
    If unsuccessfull will return HTTP 400 BAD REQUEST

* PATCH /api/address/{address_id}

    This endpoint will return the address with the `id` specified in the url to be edited.
    If successfull will return HTTP 200 OK.
    If unsuccessfull will return HTTP 400 BAD REQUEST

* DELETE /api/address/{address_id}

    This endpoint will return the address with the `id` specified in the url to be deleted.
    If successfull will return HTTP 200 OK.
    If unsuccessfull will return HTTP 404.

* LOGIN /rest-auth/login/

    This endpoint will allow the user to log in.
    If successfull will return HTTP 200 OK.
    If unsuccessfull will return HTTP 405.

* LOGOUT /rest-auth/logout/

    This endpoint will allow the user to logout.
    If successfull will return HTTP 200 OK.
    If unsuccessfull will return HTTP 405.


## **_Extra notes_**

To install all the packages to run this project I have created a requirements.txt file.
Please type "pip3 install -r requirements.txt" in your terminal.

To run the application please type "python3 manage.py runserver" in your terminal.

The log in details for the Admin section and browsable API are:

username = admin
password = qogita2021

Inside my model I have created the "location_name" field. I assumed that a business could have more then one address in the same city and this field may help to find the specific address quicker.

I have tried to implement the filtering at the end of the project and I have realised that instead of using the APIview I should have used the "generics.GenericAPIView". This would have allowed more detailed filtering with less code.

I have also left exposed the Django Secret Key as no sensitive information are present in the database.
