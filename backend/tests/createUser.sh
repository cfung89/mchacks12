#! /bin/bash

curl -X POST http://127.0.0.1:5000/user/create -H "Content-Type: application/json" -d '{"user_id": "1234", "username": "John", "email": "test@gmail.com"}'
