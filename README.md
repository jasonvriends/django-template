# django-template

Starting a Django project from scratch is no easy task. Save yourself a significant amount of time by using this seed project. This is a ```batteries included``` project, covering common capabilities such as: authentication, authorization, custom user models, user profiles, and much more.

![GitHub Logo](/documentation/images/profile.png)

## Background

Django is a high-level Python web framework that enables rapid development of secure and maintainable websites. Built by experienced developers, Django takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel. It is free and open source, has a thriving and active community, great documentation, and many options for free and paid-for support.

## Features

- Custom user model (AbstractBaseUser)
- Local and social authentication (django-allauth)
  - Custom sign-up fields (i.e. name)
  - Minimum password complexity
    - Password length must be greater than 8 characters
    - Password must contain at least 1 digit
    - Password must contain at least 1 letter
    - Password must contain at least 1 special character
  - Account and data deletion
- Integrated with the [Tabler Dashboard UI Kit](https://github.com/tabler/tabler)
  - Templates for 400, 403, 404, 500, privacy policy, and maintenance pages
  - Dark and light themes
  - Dismissible Django messages
- User profiles
  - Last login date
  - Timezone
  - Theme
  - Avatar
- Settings for local and azure deployments

## Development Environment

The following system configuration was used for the development of django-template:
- Windows 11
  - Docker Desktop
    - PostgreSQL 14.6-alpine
    - pgAdmin 4.23
  - Windows Subsystem for Linux
    - AlmaLinux 8.4
      - Python: 3.10
      - Git
      - Docker
      - Docker-Compose
      - Azure CLI
- VS Code
  - Extensions
    - [Remote Development](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack)
    - [Code Spell Checker](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker)
    - [Django](https://marketplace.visualstudio.com/items?itemName=batisteo.vscode-django)
    - [djhtml-vscode](https://marketplace.visualstudio.com/items?itemName=TomUsher.djhtml-vscode)
    - [Run on Save](https://marketplace.visualstudio.com/items?itemName=emeraldwalk.RunOnSave)
  - Settings.json
    ```
      {
         "explorer.compactFolders": false,
         "workbench.startupEditor": "none",
         "workbench.sideBar.location": "right",
         "workbench.statusBar.visible": true,
         "workbench.editor.showTabs": true,
         "workbench.activityBar.visible": true,
         "editor.minimap.enabled": false,
         "editor.mouseWheelZoom": true,
         "zenMode.centerLayout": true,
         "explorer.confirmDragAndDrop": false,
         "terminal.integrated.enableMultiLinePasteWarning": false,
         "git.autofetch": true,
         "[python]": {
            "editor.defaultFormatter": "ms-python.black-formatter"
         },
         "files.exclude": {
            "**/__pycache__": true
         },
         "git.confirmSync": false,
         
         "files.associations": {
            "**/templates/*.html": "django-html",
         },

         "[django-html]": {
            "editor.formatOnSave": false
         },

         "emeraldwalk.runonsave": {
            "commands": [
                  {
                     "match": ".*/templates/.*\\.html$",
                     "cmd": "djhtml -i ${file} -t 2"
                  },
            ]
         },

      }
    ```

## Deployments

This project includes **Django settings** and **Python packages** for both **local** and **Microsoft Azure** deployments.

### Getting Started

- Create your own Git repository

- Clone this Git repository to your development environment
  ```
  git clone https://github.com/jasonvriends/django-template.git <new_project_name>
  ```

- Change the remote origin of the cloned Git repository to your Git repository
  ```
  git remote set-url origin http://github.com/YOU/YOUR_REPO
  ```

- Push the changes to your Git repository
  ```
  git push
  ```

- Change directory to source
   ```
   cd source
   ```

- Create a virtual environment
   ```
   python3 -m venv .venv
   ```

- Activate the virtual environment
   ```
   source .venv/bin/activate
   ```

- Update the Python ```pip``` package
   ```
   python -m pip install --upgrade pip
   ```

### Local

- Install the required Python packages
   ```
   pip install -r config/requirements/requirements-local.txt
   ```

- Generate a ```SECRET_KEY```
   ```
   SECRET_KEY=`python -c 'import secrets; print(secrets.token_urlsafe(38))'`
   ```

- Generate an environment (```.env```) file
   ```
   touch .env
   echo DJANGO_DEBUG=True >> .env
   echo DATABASE_URL=postgres://postgres:postgres@127.0.0.1:5432/postgres >> .env
   echo DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1 >> .env
   echo DJANGO_SETTINGS_MODULE=config.settings.local >> .env
   echo PROJECT_NAME=django-template >> .env
   echo PROJECT_PRIVACY_COUNTRY=Ontario, Canada >> .env
   echo PROJECT_PRIVACY_WEBSITE=http://mywebsite.com >> .env
   echo PROJECT_PRIVACY_EMAIL=your@email.com >> .env
   echo PROJECT_PRIVACY_SOCIALACCOUNTS=Google Facebook >> .env
   echo PROJECT_PRIVACY_MODIFIED=November 16, 2022 >> .env
   echo SECRET_KEY=$SECRET_KEY >> .env
   ```

- Tell django-environ to use the ```.env``` file instead of OS environmental variables
   ```
   export DJANGO_READ_DOT_ENV_FILE=True
   ```

- Stand up the PostgreSQL database using Docker-Compose (you need Docker and Docker-Compose already installed)
    ```
    cd ../deployment/docker
    docker-compose up -d
    cd ../../source
    ```

- Seed the database
    ```
    python3 manage.py migrate
    ```

- Create a superuser
    ```
    python3 manage.py createsuperuser
    ```

- Run the local webserver
    ```
    python3 manage.py runserver
    ```

- Login to the development server at http://127.0.0.1:8000/admin

- Configure social authentication
  - Under ```Sites``` select ```Sites```.
  - Select ```example.com```.
  - for ```domain name``` and ```display name``` specify ```http://127.0.0.1:8000```.
  - Under ```Social Accounts``` select add ```Social Application```.
  - Specify the ```provider```.
    - If you don't see your preferred provider, refer to [social providers](https://django-allauth.readthedocs.io/en/latest/providers.html) and ensure its listed inside the ```INSTALLED_APPS``` section of ```config/settings/base.py```.
      ```
      INSTALLED_APPS = [
         'allauth.socialaccount.providers.google',
      ]
      ```
  - Specify the ```name``` of your provider.
  - Specify the ```Client id``` and ```Secret key``` from your provider.
  - Select ```http://127.0.0.1:8000``` under ```Available Sites``` and move it to ```Chosen sites```.
  - Select Save.
    
- Modify the source files as appropriate

- Run pre-commit checks
  ```
  pre-commit run --all-files
  ```

### Azure

- Generate a ```SECRET_KEY```
   ```
   SECRET_KEY=`python -c 'import secrets; print(secrets.token_urlsafe(38))'`
   ```

#### Deploy via the Azure CLI

- Authenticate to Azure CLI
  ```
  az login
  ```

- Set a subscription to be the current active subscription
  ```
  az account set --subscription <subscription id>
  ```

- Deploy the required components. Note this is a demo deployment and not secure. **Do Not Use In Production**.
  ```
  # Variables
  location="canadaeast"
  resourceGroup="emptyflame47"
  databaseName="emptyflame47"
  databaseUsername=emptyflame47
  databasePassword=emptyflame47
  databaseSku=Standard_B1ms
  webappName=emptyflame47
  storageName=emptyflame47
  ipAddress=$(curl ifconfig.me)

  # Create Resource Group
  az group create --name $resourceGroup --location $location
  
  # Deploy Storage Account
  az storage account create --name $storageName --resource-group $resourceGroup --location $location --kind StorageV2
  storageKey=$(az storage account keys list -g $resourceGroup -n $storageName --query '[0].[value]' -o tsv)
  
  # Create Storage Containers
  az storage container create --name static --account-name $storageName --auth-mode key --public-access blob --account-key $storageKey
  az storage container create --name media --account-name $storageName --auth-mode key --public-access blob --account-key  $storageKey

  # Deploy Flexible Server
  az postgres flexible-server create --name $databaseName --resource-group $resourceGroup --location $location --tier Burstable --sku-name $databaseSku --admin-user $databaseUsername --admin-password $databasePassword --public-access 0.0.0.0-$ipAddress --storage-size 32
  
  # Deploy Azure App Service Plan
  az appservice plan create --name $webappName --resource-group $resourceGroup --sku B1 --is-linux
  
  # Deploy Web App
  az webapp create --name $webappName --resource-group $resourceGroup --plan $webappName --runtime PYTHON:3.10
  
    # Configure appsettings
  az webapp config appsettings set -g $resourceGroup -n $webappName --settings \
  DJANGO_DEBUG="False" \
  DATABASE_URL="postgres://$databaseUsername:$databasePassword@$databaseName.postgres.database.azure.com:5432/postgres" \
  DJANGO_ALLOWED_HOSTS="$webappName.azurewebsites.net" \
  DJANGO_CSRF_TRUSTED_ORIGINS="https://$webappName.azurewebsites.net" \
  DJANGO_AZURE_ACCOUNT_NAME="$storageName" \
  DJANGO_AZURE_ACCOUNT_KEY="$storageKey" \
  DJANGO_AZURE_MEDIA_CONTAINER="media" \
  DJANGO_AZURE_STATIC_CONTAINER="static" \
  DJANGO_EMAIL_BACKEND="django.core.mail.backends.smtp.EmailBackend" \
  DJANGO_EMAIL_HOST_USER="your-email-username" \
  DJANGO_EMAIL_HOST_PASSWORD="your-email-password" \
  DJANGO_EMAIL_HOST="your-email-smtp" \
  DJANGO_EMAIL_PORT="587" \
  DJANGO_EMAIL_USE_TLS="True" \
  DJANGO_DEFAULT_FROM_EMAIL="do-not-reply@domain.com" \
  DJANGO_SETTINGS_MODULE="config.settings.azure" \
  PROJECT_NAME="django-template" \
  PROJECT_PRIVACY_COUNTRY="Ontario, Canada" \
  PROJECT_PRIVACY_WEBSITE="https://$webappName.azurewebsites.net" \
  PROJECT_PRIVACY_EMAIL="your@email.com" \
  PROJECT_PRIVACY_SOCIALACCOUNTS="Google Facebook" \
  PROJECT_PRIVACY_MODIFIED="November 16, 2022" \
  SECRET_KEY="$SECRET_KEY" \
  SCM_DO_BUILD_DURING_DEPLOYMENT="1"
  ```

- Deploy to Azure
  ```
  # Package source for zip deployment 
  cp config/requirements/requirements-azure.txt requirements.txt
  zip --exclude=*venv* -r azuredeployment.zip .
  
  # Deploy zip to the Azure App Service
  az webapp deployment source config-zip -g $resourceGroup -n $webappName --src azuredeployment.zip --timeout 3600

  # Cleanup
  rm azuredeployment.zip
  rm requirements.txt
  ```

- SSH into the App Service on Linux
   ```
   # Change to the wwwroot directory
   cd site/wwwroot
   
   # Activate default virtual environment in App Service container
   source antenv/bin/activate
   
   # Upgrade Pip
   python -m pip install --upgrade pip
   
   # Run database migrations
   python manage.py migrate
   
   # Create the super user (follow prompts)
   python manage.py createsuperuser
   ```

- Login to the Admin console and configure socialauthentication ```https://webappName/admin```


#### Deploy via Hashicorp Terraform

Coming soon
