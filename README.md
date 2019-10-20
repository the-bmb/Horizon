# Horizon
## INSTALL

    Clone o repositório.
    git clone https://github.com/the-bmb/Horizon.git
    cd Horizon
    Instale as dependências.
    pip install -r requirements.txt
    Construa o banco de dados.
    python manage.py migrate
    rode o servidor.
    python manage.py runserver

## Test

python manage.py test

Recomendável criar um ambiente virtual para desenvolvimento.

python3 -m venv venv

source venv/bin/activate
