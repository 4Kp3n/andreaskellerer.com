# andreaskellerer.com
The structure of the project was created with the [Cookiecutter](https://github.com/cookiecutter/cookiecutter) project.

## 🔧 Tech-Stack

- **Django 5.2**
- **Tailwind CSS** über `django-tailwind`
- **PostgreSQL**, Redis (über Docker)
- Deployment via `Docker Compose`

## 📁 Project structur

- `compose/` – Dockerfiles (local + production)
- `config/` - Django settings
- `scripts/` - Setup and test scripts
- `website/` – Django Apps: blog, contact, reviews, users, etc.
    - `theme/` – Tailwind + Templates
    - `static/` – Static Assets
    - `templates/` – HTML-Templates
- `requirements/` – seperate base.txt, local.txt, production.txt
- `local.yml` - local Docker Compose 
- `production.yml` - production Docker Compose 