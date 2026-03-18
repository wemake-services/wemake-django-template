import logging
from collections.abc import Iterator

import pytest
import schemathesis as st
from django.conf import LazySettings
from django.urls import reverse
from schemathesis.specs.openapi.schemas import OpenApiSchema

from server.wsgi import application


@pytest.fixture(autouse=True)
def _disable_logging(settings: LazySettings) -> Iterator[None]:
    # django-query-counter produces tons of output for no reason:
    settings.DQC_ENABLED = False
    # Logging has too much output with schemathesis:
    logging.disable(logging.CRITICAL)
    yield
    logging.disable(logging.NOTSET)


# NOTE: The `db` fixture is required to enable database access.
# When `st.openapi.from_wsgi()` makes a WSGI request, Django's request
# lifecycle triggers database operations.
@pytest.fixture
def api_schema(
    transactional_db: None,
) -> 'OpenApiSchema':
    """Load OpenAPI schema as a pytest fixture."""
    return st.openapi.from_wsgi(reverse('openapi'), application)


schema = st.pytest.from_fixture('api_schema')


@pytest.mark.timeout(60)  # increase the default timeout for this test
@schema.parametrize()
def test_schemathesis(settings: LazySettings, *, case: st.Case) -> None:
    """Ensure that API implementation matches the OpenAPI schema."""
    case.call_and_validate()
