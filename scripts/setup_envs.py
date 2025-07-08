"""Create default ``.env`` files for local and production environments."""

import secrets
import string
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
ENV_DIR = BASE_DIR / ".envs"
LOCAL_DIR = ENV_DIR / ".local"
PROD_DIR = ENV_DIR / ".production"


ALPHABET = string.ascii_letters + string.digits


def random_string(length: int) -> str:
    """Return a cryptographically secure random string."""
    return "".join(secrets.choice(ALPHABET) for _ in range(length))


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def write_file(path: Path, content: str) -> None:
    if not path.exists():
        path.write_text(content)
        print(f"Created {path}")
    else:
        print(f"Skip {path}, already exists")


def main() -> None:
    ensure_dir(LOCAL_DIR)
    ensure_dir(PROD_DIR)

    local_secret = random_string(64)
    prod_secret = random_string(64)
    admin_url = random_string(30)
    local_db_user = random_string(30)
    prod_db_user = random_string(30)
    local_db_password = random_string(64)
    prod_db_password = random_string(64)

    write_file(
        LOCAL_DIR / ".django",
        "\n".join(
            [
                f"DJANGO_SECRET_KEY={local_secret}\n",
                "USE_DOCKER=no",
            ]
        )
    )
    write_file(
        LOCAL_DIR / ".postgres",
        "\n".join(
            [
                f"POSTGRES_USER={local_db_user}",
                f"POSTGRES_PASSWORD={local_db_password}",
                "POSTGRES_DB=website",
                "POSTGRES_HOST=postgres",
                "POSTGRES_PORT=5432",
            ]
        )
        + "\n",
    )
    write_file(
        PROD_DIR / ".django",
        (
            "\n".join(
                [
                    "DJANGO_SETTINGS_MODULE=config.settings.production",
                    f"DJANGO_SECRET_KEY={prod_secret}",
                    f"DJANGO_ADMIN_URL={admin_url}",
                    "DJANGO_ALLOWED_HOSTS=.yourwebsite.com",
                ]
            )
            + "\n\n"
            + """# Security
# ------------------------------------------------------------------------------
# TIP: better off using DNS, however, redirect is OK too
DJANGO_SECURE_SSL_REDIRECT=False

# Email
# ------------------------------------------------------------------------------
DJANGO_SERVER_EMAIL=

MAILGUN_API_KEY=
MAILGUN_DOMAIN=


# django-allauth
# ------------------------------------------------------------------------------
DJANGO_ACCOUNT_ALLOW_REGISTRATION=True

# Gunicorn
# ------------------------------------------------------------------------------
WEB_CONCURRENCY=4


# Redis
# ------------------------------------------------------------------------------
REDIS_URL=redis://redis:6379/0"""
            + "\n"
        ),
    )
    write_file(
        PROD_DIR / ".postgres",
        "\n".join(
            [
                f"POSTGRES_USER={prod_db_user}",
                f"POSTGRES_PASSWORD={prod_db_password}",
                "POSTGRES_DB=website",
                "POSTGRES_HOST=postgres",
                "POSTGRES_PORT=5432",
            ]
        )
        + "\n",
    )


if __name__ == "__main__":
    main()
