# django-template
<p>Django 1.9.2 template with webpack</p>

<ol>
    <li>
    Create virtual environment<br/>
    <code>virtualenv venv</code>
    </li>

    <li>
    Start virtual environment<br/>
    <code>source venv/bin/activate</code>
    </li>

    <li>
    Install all requirements<br/>
    <code>pip install -r requirements.txt</code>
    </li>
    
    <li>
    Apply migrations<br/>
    <code>python manage.py migrate</code>
    </li>

    <li>
    Run<br/>
    <code>python manage.py runserver</code>
    </li>
    
    <li>
    Another terminal! Install all npm dependencies<br/>
    <code>npm install</code>
    </li>
    
    <li>
    Start webpack watcher
    <code>webpack --watch</code>
    </li>
</ol>

<strong>TL;DR</strong><br/>
<code>virtualenv venv;source venv/bin/activate;pip install -r requirements.txt;python manage.py migrate;python manage.py runserver</code>

Change the remote origin.<br/>
<code>git remote set-url orgin [ADD_GIT_REPO_HERE]</code>
