# Estoque
Controle de estoque com Django, inclui fluxo de caixa completo com estoque, e importação/exportação de planilha de registros.

## Como rodar o projeto:

* Clone este repositório.
* Crie uma virtualenv com python 3.
* Ative a virtualEnv.
* Instale as dependencias.
* Rode as migrações.
* Crie um superusuario para editar configurações do sistema.

```
git clone git@github.com:ryaMarks/ControleEstoque.git
python -m venv .venv
source .venv/Scripts/activate
pip install -r requirements.txt
python contrib/env_gen.py
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### Links de consulta:


* [python-decouple](https://github.com/henriquebastos/python-decouple)
* [deploy no PythonAnywhere](https://tutorial.djangogirls.org/pt/deploy/)
* [Carregando arquivos estaticos no deploy](https://pt.stackoverflow.com/questions/262043/problemas-carregar-static-files-no-django-em-deploy-no-heroku)
