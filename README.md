virtuasi-sgq
============

Sistema de Gestão da Qualidade


Como executar o projeto
------------------------

### Montando o ambiente


#### Unix

No temrinal, execute:

    sudo easy_install pip
    pip install virtualenv virtualenvwrapper
    source /usr/local/bin/virtualenvwrapper.sh
    mkvirtualenv --distribute sgq
    
Set WORKON_HOME to your virtualenv dir (Ubuntu)

    export WORKON_HOME=~/.virtualenvs

Add this line to the end of ~/.bashrc so that the virtualenvwrapper commands are loaded.

    . /usr/local/bin/virtualenvwrapper.sh
    
### Executanto o projeto

Ative o ambiente.
    
    workon sgq

Se estiver rodando o projeto pela primeira vez, crie um settings_local.py, instale as dependências e sincronize o banco de dados.
    
    pip install -r sgq/requirements/development.txt
    cp sgq/settings_local_sample.py sgq/settings_local.py
    python manage.py syncdb

Execute o projeto
    
    python manage.py runserver

Agora abra o projeto em [http://localhost:8000/](http://localhost:8000/ "development server").
