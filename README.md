# Referral Management System with Performance Metrics

The Referral System API project aims to develop a robust API that facilitates user registration, retrieval of user details, and viewing of user referrals. This API provides endpoints for users to register with essential information such as name, email, and password. Additionally, users have the option to include a referral code, allowing them to be referred by existing users. Upon successful registration, users receive a unique user ID.

Authenticated users can access their details through a dedicated endpoint, requiring an Authorization header with a valid token. The user details include the user's name, email, referral code (if provided), and the timestamp of registration.

Furthermore, the API enables users to view their referrals via another endpoint, also requiring authentication. The referrals endpoint returns a paginated list of users who registered using the current user's referral code, along with the timestamp of registration for each referral.

By implementing this API, businesses can efficiently track user referrals, incentivize user engagement, and foster community growth through a structured referral system.



## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)

## Installation

1. Clone the repository:
   git clone https://github.com/ashikos/referal-system.git

## navigate to the project directory:
cd referral_ms


## Create a virtual environment and activate it:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


## Install the project dependencies:
pip install -r requirements.txt


## Apply database migrations:
python manage.py migrate


## Create a superuser to access the Django admin:
python manage.py createsuperuser


Start the development server:
python manage.py runserver



## Usage
The Referral Management System provides APIs to manage user profiles, track  user referals and activities. Detailed documentation for API endpoints and data models can be found in the API Endpoints section below


API Endpoints

    All the APIs except Singnup, login are secured by Jwt Authentication.
    User need to singup and login inorder to access all other Endpoints.
    A JWT token is received after the succefull login, these tokens sholud be saved in the cookies in order to 
    acccess other api Endpoints.
   
    Swagger: All apis are documented using swagger
        /api/swagger/ 
    
    Authentication:
        POST /api/accounts/signup/ : create a new user
        POST /api/accounts/login/ : login api which generates a jwt token which should be attached in cookies.
        GET /api/accounts/user/ : get details of logged user
        POST /api/accounts/logout/ : logout api 

    Users and Referrals:
        GET /api/accounts/users/ : get details of all users
        GET /api/accounts/referrals/ : Returns a list of users who registered using the current user's referral_code.

    





