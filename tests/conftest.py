
import pytest


@pytest.fixture()
def context():
    """Creates default prompt values."""
    return {
        'project_name': 'test-project',
        'project_verbose_name': 'Test Project',
        'project_domain': 'myapp.com',
        'organization': 'wemake.services',
    }
