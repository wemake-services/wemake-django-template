import pytest


@pytest.fixture
def context() -> dict[str, str]:
    """Creates default prompt values."""
    return {
        'project_name': 'test-project',
        'project_verbose_name': 'Test Project',
        'project_domain': 'myapp.com',
        'organization': 'wemake.services',
    }
