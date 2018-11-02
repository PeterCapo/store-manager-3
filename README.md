# store-manager
Store Manager is a web application that helps store owners manage sales and product inventory records. This application is meant for use in a single store

[![Build Status](https://travis-ci.com/PeterCapo/store-manager-3.svg?branch=master)](https://travis-ci.com/PeterCapo/store-manager-3)
[![Coverage Status](https://coveralls.io/repos/github/PeterCapo/store-manager-3/badge.svg?branch=master)](https://coveralls.io/github/PeterCapo/store-manager-3?branch=master)

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/d5f401cef57bce99e752)

# Heroku Link

https://store-managerv1.herokuapp.com/

# Installation and Setup

Clone the repository & CD into it 

# Create a virtual environment

    virtualenv venv --python=python3.7

# Activate virtual environment

    source venv/bin/activate
    or for windows OS
    venv\scripts\activate

# Install required Dependencies

    pip install -r requirements.txt



# API Endpoints 

| Method | Endpoint                        | Description                           |
| ------ | ------------------------------- | ------------------------------------- |
| POST   | /api/v2/products                | Create a product                      |
| POST   | /api/v2/sales                   | Create a sale record                  |
| GET    | /api/v2/products                | Get all products                      |
| GET    | /api/v2/sales                   | Get all sales                         |
| GET    | /api/v2/products/<int:id>       | Get a specific product                |
| GET    | /api/v2/sales/<int:id>          | Get a specific sale record            |
| PUT    | /api/v2/products/<int:id>       | Update products                       |
| DELETE | /api/v2/products/<int:id>       | Get a specific product                |
| POST   | /api/v2/login                   | Sign in                               | 
| POST   | /api/v2/signup                  | Register                              | 

Test on Postman 

# Run Test
- python -m unittest