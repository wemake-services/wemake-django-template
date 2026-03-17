import pytest
import schemathesis as st
from django.urls import reverse
from schemathesis.specs.openapi.schemas import OpenApiSchema

from server.wsgi import application


@pytest.fixture
def api_schema(transactional_db: None) -> 'OpenApiSchema':
    """Load OpenAPI schema as a pytest fixture."""
    return st.openapi.from_wsgi(reverse('openapi'), application)


schema = st.pytest.from_fixture('api_schema')


@schema.parametrize()
def test_schemathesis(case: st.Case) -> None:
    """Ensure that API implementation matches the OpenAPI schema."""
    case.call_and_validate()
