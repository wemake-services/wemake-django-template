import pytest


@pytest.fixture
def main_heading() -> str:
    """An example fixture containing some html fragment."""
    return 'data-testid="wemake-django-template"'
