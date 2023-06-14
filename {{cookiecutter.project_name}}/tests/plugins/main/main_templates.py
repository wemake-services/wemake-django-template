import pytest


@pytest.fixture()
def main_heading() -> str:
    """An example fixture containing some html fragment."""
    return '<h1>wemake-django-template</h1>'
