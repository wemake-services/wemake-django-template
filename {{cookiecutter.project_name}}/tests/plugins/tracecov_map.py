import pytest
from tracecov import CoverageMap


@pytest.fixture(scope='session')
def tracecov_map() -> CoverageMap:
    """Provide the session ``tracecov`` coverage map for tests."""
    from server.urls import schema  # noqa: PLC0415

    return CoverageMap.from_dict(schema.convert())
