#!/bin/bash

echo "Get all projects"
curl --header "Content-Type: application/json" --request GET http://127.0.0.1:5000/projects

echo "Create a project with id 1"
curl --header "Content-Type: application/json" --request POST --data '{"project_name": "que taaal"}' http://127.0.0.1:5000/projects

echo "Get project 1 metadata"
curl --header "Content-Type: application/json" --request GET http://127.0.0.1:5000/projects/1

echo "Modify project 1"
curl --header "Content-Type: application/json" --request PUT --data '{"project_name": "NAMEEE"}' http://127.0.0.1:5000/projects/1