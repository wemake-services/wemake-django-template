import logging

import pytest


@pytest.fixture(name='logger')
def _logger() -> logging.Logger:
    """Returns the current logger instance."""
    return logging.getLogger(__name__)


def test_logging_format(
    caplog: pytest.LogCaptureFixture,
    logger: logging.Logger,
) -> None:
    """This test ensures logging is done correctly."""
    message = 'Test message'

    logger.error(message)

    assert caplog.record_tuples == [()]
