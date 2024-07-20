
#### Get all users

```http
  GET /users
```


#### Get user by id

```http
  GET /users/id
```
#### Create a user

```http
  POST /users/
```
#### Update a user

```http
  PUT /users/id
```
#### Delete a user

```http
  DELETE /users/id
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `userid`      | `string` | **Required**. Id of user |
| `name`      | `string` | **Required**. name of user |
| `email`      | `string` | **Required**. email of user |
| `password`      | `string` | **Required**. password of user |

## Run Locally

Clone the project

```bash
  git clone https://github.com/Vikrant-Khedkar/Flask-CRUD
```
Crate a Docker Image

```bash
 docker build -t flask_app .
```
Run the Docker Image

```bash
 docker run -p 5000:5000 flask_app 
```
Now use the api 
