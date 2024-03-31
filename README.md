# Casting Agency

## rOverview

Casting Agency project heps you to get the details of the Actors and Movies. Also, we have Role Based permissions which lets you to play around the different roles and check what all actions could be performed by different users.

## Getting Started

## Tools needed
    - VS Code
    - Postman

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)


#### PIP Dependencies

Once you have your environment setup and running, install dependencies by naviging to the `casting` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) are libraries to handle the lightweight sqlite database. Since we want you to focus on auth, we handle the heavy lift for you in `./src/database/models.py`. We recommend skimming this code first so you know how to interface with the Drink model.

- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

## Overview of the Project:

The Application is for Casting agency to organise Actors and Movies.

## Models

Create 2 models
   - Actors model with name, age and gender attribute
   - Movies model with title and release_date attribute

This application uses below endpoints
----------------------------
- GET /movies
- GET /actors
- GET /movies/id
- GET /actors/id

- POST /movies
- POST /actors

- PATCH /movies/id
- PATCH /actors/id

- DELETE /movies/id
- DELETE /actors/id

----------------------------


### Setup Auth0

1. Create a new Auth0 Account

2. Select a unique tenant domain

3. Create a new, single page web application

4. Create a new API "casting"
   - in API Settings:
     - Enable RBAC
     - Enable Add Permissions in the Access Token

5. Create new API permissions
-----------------------------------------
   - `get:movies`
   - `post:movies`
   - `patch:movies`
   - `delete:movies`
----------------------------------------
   - `get:actors`
   - `post:actors`
   - `patch:actors`
   - `delete:actors`
----------------------------------------

6. Create new roles for:
   - Casting Assistant
        -  `get:movies`
        -  `get:actors`

   - Casting Director
        -  `get:movies`
        -  `get:actors`
        -  `post:actors`
        -  `patch:actors`
        -  `delete:movies`
        -  `patch:movies`

    - Executive Director
        -  `get:movies`
        -  `get:actors`
        -  `post:actors`
        -  `patch:movies`
        -  `patch:actors`
        -  `patch:movies`
        -  `delete:movies`
        -  `delete:actors`
        - can perform all actions

7. Test your endpoints with [Postman](https://getpostman.com).
   - Register 3 users
        - Assign Casting Assitant Role to one user
        - Assign Casting Director Role to Another User
        - Assign Executive Director Role to one more user
   - Sign into each account and make note of the JWT.

   - Import the postman collection `Casting.postman_collection.json`

   - Right-clicking the collection folder for casting assistant, casting director and executive producer, navigate to the authorization tab, and including the JWT in the token field (you should have noted these JWTs).
   
   - Run the collection and correct any errors.
   
   - Export the collection overwriting the one we've included so that we have your proper JWTs during review!

## Application Login URL
    [casting agency login]
    https://kavyasrik.us.auth0.com/authorize?audience=casting&response_type=token&client_id=QwwLST9BrD7VoeyhM773l2sT7o1v4Ljg&redirect_uri=https://127.0.0.1:8080/Casting 

## Render Steps

    - Connect your repository with Render Dashboard
    - Create a Web service and deploy in in the repository connect by adding DATABASE_URL

## Deployment Link for the Application 

https://casting-2tvr.onrender.com

Below curl to execute the APIs via CURL or Postman. For example:
```bash
Returns the list of all the movies along with the title and release date of the movie.

Sample Curl:
$ curl -X GET 'https://casting-2tvr.onrender.com/movies' \ --header 'Authorization: Bearer <access-token>'

Sample Response:
{
    "movies": [
        {
            "id": 1,
            "release_date": "2023-04-17",
            "title": "Thangamagan"
        },
        {
            "id": 2,
            "release_date": "2021-01-09",
            "title": "Bigil"
        }
    "success": true
}
```
```bash
Returns the specific movie based on the ID provided.

Sample Curl:
$ curl -X GET 'https://casting-2tvr.onrender.com/movies/1' \ --header 'Authorization: Bearer <access-token>'

Sample Response:
{
    "movies": {
        "id": 1,
        "release_date": "2023-04-17",
        "title": "Thangamagan"
    },
    "success": true
}
```
```bash
Returns the newly created movie along with the success message.

Sample Curl:
$ curl -X POST 'https://casting-2tvr.onrender.com/movies' \ --header 'Authorization: Bearer <access-token>'

Sample Request:
{
    "title": "Jawan",
    "release_date": "2021-01-01"
}

Sample Response:
{
    "movies": "Jawan",
    "success": true
}
```
```bash
Returns the updated movie details along with the success message.

Sample Curl:
$ curl -X PATCH --request PATCH 'https://casting-2tvr.onrender.com/movies/1' \ --header 'Authorization: Bearer <access-token>'

Sample Request:
{
    "title": "Viswasam",
    "release_date": "2021-01-09"
}

Sample Response:
{
    "movie": "Viswasam",
    "success": true
}
```
```bash
Returns the ID of the deleted movies along with the success message.

Sample Curl:
$ curl -X DELETE --request DELETE 'https://casting-2tvr.onrender.com/movies/1' \
--header 'Authorization: Bearer <access-token>'

Sample Response:
{
    "deleted_movie": 5,
    "success": true
}
```
```bash
Returns the list of all the actors along with the ID, name, age and gender of the actor.

Sample Curl:
$ curl -X GET 'https://casting-2tvr.onrender.com/actors' \ --header 'Authorization: Bearer <access-token>'

Sample Response:
{
    "actors": [
        {
            "id": 1,
            "age": "35",
            "gender": "Male",
            "name": "Vijay"
        },
        {
            "id": 2,
            "age": "37",
            "gender": "Male",
            "name": "Karthik"
        }
    ],
    "success": true
}
```
```bash
Returns the details of the specified actors along with the ID, name, age, gender of the actor and the success message.

Sample Curl:
$ curl -X GET 'https://casting-2tvr.onrender.com/actors/1' \ --header 'Authorization: Bearer <access-token>' 

Sample Response:
{
    "movies": {
        "id": 1,
        "age": "35",
        "gender": "Male",
        "name": "Vijay"
    },
    "success": true
}
```
```bash
Returns the newly created actor details along with the ID, name, age, gender of the actor and the success message.

Sample Curl:
$ curl -X POST 'https://casting-2tvr.onrender.com/actors' \ --header 'Authorization: Bearer <access-token>'

Sample Request:
{
    "name": "Jo",
    "age": 39,
    "gender": "Female"
}

Sample Response:
{
    "age": "39",
    "gender": "Female",
    "name": "Jo",
    "success": true
}
```
```bash
Returns the updated actor details along with the ID, name, age, gender of the actor and the success message.

Sample Curl:
$ curl -X PATCH --request PATCH 'https://casting-2tvr.onrender.com/actors/1' \ --header 'Authorization: Bearer <access-token>'

Sample Request:
{
    "name": "Vijay",
    "age": 35,
    "gender": "Male"
}

Sample Response:
{
    "actor": {
        "age": "35",
        "gender": "Male",
        "id": 1,
        "name": "Vijay"
    },
    "success": true
}
```
```bash
Returns the deleted actor ID along with the success message.

Sample Curl:
$ curl -X DELETE --request DELETE 'https://casting-2tvr.onrender.com/actors/1' \
--header 'Authorization: Bearer <access-token>'

Sample Response:
{
    "deleted_actor": 1,
    "success": true
}
```

## TEST and PostMan Collection

Attach the casting api file 
- Update the Postman token and run the collections

### Error Handling

Errors are returned as JSON objects in the following format:
```json
{
    "success": False, 
    "error": 400,
    "message": "bad request"
}
```
The API will return three error types when requests fail:
- 400: Bad Request
- 401: Unauthorized
- 403: Forbidden
- 404: Resource Not Found
- 422: Not Processable 
- 500: Internal Server Error