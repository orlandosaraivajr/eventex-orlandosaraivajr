# Eventex

Sistema de eventos desenvolvido no curso "Welcome to the Django"

[![Build Status](https://travis-ci.org/orlandosaraivajr/eventex-orlandosaraivajr.svg?branch=master)](https://travis-ci.org/orlandosaraivajr/eventex-orlandosaraivajr)
[![Code Health](https://landscape.io/github/orlandosaraivajr/eventex-orlandosaraivajr/master/landscape.svg?style=flat)](https://landscape.io/github/orlandosaraivajr/eventex-orlandosaraivajr/master)

### Como desenvolver ?

1. Clone o repositório
2. Crie um virtualenv 
3. Ative a virtualenv
4. Instale as dependências
5. Configure a instância com o .env 
6. Execute os testes

```console
git clone https://github.com/orlandosaraivajr/eventex-orlandosaraivajr.git
cd eventex-orlandosaraivajr/
virtualenv venv -p python3
source venv/bin/activate
pip install -r requirements.txt 
cp contrib/env-sample .env
python manage test
python manage runserver
```
### Como fazer o deploy ?

1. Crie um instância no heroku.
2. Envie as configuraçōes para o heroku.
3. Define una SECRET_KEY segura para instância.
4. Defina DEBUG=False
5. Configure o serviço de email.
6. Envie o código para o heroku.

```console
 heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
# configuro o email
git push heroku master --force
 ```