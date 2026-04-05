import tomllib
from typing import Any, cast

from dmr.openapi import OpenAPIConfig
from dmr.settings import Settings

from server.settings.components import BASE_DIR, config


def _get_project_meta() -> dict[str, str]:  # lying about return type
    pyproject = BASE_DIR / 'pyproject.toml'
    return cast(
        dict[str, str],
        tomllib.loads(pyproject.read_text())['project'],
    )


# django-modern-rest
# https://django-modern-rest.readthedocs.io

DMR_SETTINGS: Any = {
    # Default OpenAPI config:
    Settings.openapi_config: OpenAPIConfig(
        title='wemake-django-template',
        version=_get_project_meta()['version'],
    ),
    # Generate fake examples in OpenAPI:
    Settings.openapi_examples_seed: 1,
}


# django-cors-headers
# https://github.com/adamchainz/django-cors-headers

CORS_ALLOWED_ORIGINS = [
    f'https://{config("DOMAIN_NAME")}',
]
CORS_ALLOW_ALL_ORIGINS = False
