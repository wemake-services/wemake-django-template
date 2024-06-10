import logging

import pytest


@pytest.fixture
def logger() -> logging.Logger:
    """Returns the current logger instance."""
    return logging.getLogger(__name__)


def test_logging_format(
    caplog: pytest.LogCaptureFixture,
    logger: logging.Logger,
) -> None:
    """This test ensures logging is done correctly."""
    message = 'Test message'

    logger.error(msg)

    assert caplog.record_tuples == []
