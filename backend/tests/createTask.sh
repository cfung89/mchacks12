#! /bin/bash

curl -X POST http://127.0.0.1:5000/task/create -H "Content-Type: application/json" -d "{\"task_id\": ${1}, \"user_id\": \"1234\", \"task_content\": \"Hello World\", \"date_due\": \"01/01/2000\", \"task_tag\": \"school\", \"status\": true, \"xp_cost\": 200}"
