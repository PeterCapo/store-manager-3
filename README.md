# store-manager
Store Manager is a web application that helps store owners manage sales and product inventory records. This application is meant for use in a single store

[![Build Status](https://travis-ci.com/PeterCapo/store-manager.svg?branch=API-V1)](https://travis-ci.com/PeterCapo/store-manager)
[![Coverage Status](https://coveralls.io/repos/github/PeterCapo/store-manager/badge.svg?branch=API-V1)](https://coveralls.io/github/PeterCapo/store-manager?branch=API-V1)
[![Maintainability](https://api.codeclimate.com/v1/badges/c3d3f3ab02e80bbcce6f/maintainability)](https://codeclimate.com/github/PeterCapo/store-manager/maintainability)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/a5b21ac3ecd2406f965a177c8c6c5d31)](https://www.codacy.com/app/PeterCapo/store-manager?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=PeterCapo/store-manager&amp;utm_campaign=Badge_Grade)
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
| POST   | /api/v1/products                | Create a product                      |
| POST   | /api/v1/sales                   | Create a sale record                  |
| GET    | /api/v1/products                | Get all products                      |
| GET    | /api/v1/sales                   | Get all sales                         |
| GET    | /api/v1/products/<int:id>       | Get a specific product                |
| GET    | /api/v1/sales/<int:id>          | Get a specific sale record            |
| PUT    | /api/v1/products/<int:id>       | Update products                       |
| DELETE | /api/v1/products/<int:id>       | Get a specific product                |
| POST   | /api/v1/login                   | Sign in                               | 
| POST   | /api/v1/signup                  | Register                              | 

Test on Postman 

# Run Test
- python -m unittest