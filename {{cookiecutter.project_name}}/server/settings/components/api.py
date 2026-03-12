import tomllib
from typing import Any, cast

from dmr.openapi import OpenAPIConfig
from dmr.settings import Settings

from server.settings.components import BASE_DIR


def _get_project_meta() -> dict[str, str]:  # lying about return type
    pyproject = BASE_DIR / 'pyproject.toml'
    return cast(
        dict[str, str],
        tomllib.loads(pyproject.read_text())['project'],
    )


DMR_SETTINGS: Any = {
    Settings.openapi_config: OpenAPIConfig(
        title='wemake-django-template',
        version=_get_project_meta()['version'],
    ),
}
