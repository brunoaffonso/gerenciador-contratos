# Gerenciador de Contratos
![Badge em Desenvolvimento](https://img.shields.io/badge/Status-Development-yellow)

## Description
This project is a simple dashboard, builded in Django. 

This application was made to managemente of contracts.

## Installation
Building and running the project in your local dev environment is very easy. Be sure you have [Git](https://git-scm.com/downloads) and [Node.js](https://nodejs.org/) installed, then follow the directions below.

1. Clone the source code. 

    `https://github.com/brunoaffonso/gerenciador-contratos.git  gerenciadorContratos`
    
    `cd gerenciadorContratos`


2. Create virtualenv.

    `python -m venv .venv`
	

3. Activate virtualenv.

    `source .venv/bin/activate`


4. Install dependencies.

    `pip install -r requirements-dev.txt`


5. Config .env instance.

    `cp contrib/env-sample .env`


## Deploy
Deploy App on Heroku.

1. Create Heroku instance. 
    
    `heroku create minhainstancia`


2. Push configs to Heroku.
    
    `heroku config:push`
	

3. Generate a SECRET_KEY to instance.

    heroku config:set SECRET_KEY=`python contrib/secret_gen.py`


4. Install dependencies.

    `pip install -r requirements-dev.txt`


5. Config .env instance.

    `cp contrib/env-sample .env`


## Project pendences
- `Authentication`
- `Refactoring`
- `Login page`
- `bugs`
- `Design`

## Technologies
<div>
<a href="#" target="_blank"> <img src="https://cdn.worldvectorlogo.com/logos/python-5.svg" alt="Material UI" width="40" height="40"/></a>
<a href="#" target="_blank"> <img src="https://cdn.worldvectorlogo.com/logos/django.svg" alt="React" width="40" height="40"/></a>
</div>

## License
![Badge em Desenvolvimento](https://img.shields.io/badge/Licence-MIT-green)

**Project developed for learning purposes.**
	
