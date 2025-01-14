import logging
import re
from typing import Final

import pytest

_LOGGING_FORMAT_RE: Final = re.compile(
    r"timestamp='.+' level='error' event='Test message' logger='django'",
)


@pytest.fixture(name='logger')
def logger_fixture() -> logging.Logger:
    """Returns the current logger instance."""
    return logging.getLogger('django')


@pytest.fixture(autouse=True)
def _redact_caplog_handlers(
    caplog: pytest.LogCaptureFixture,
    logger: logging.Logger,
) -> None:
    """Pytest inserts custom formatter, we need to reset it back."""
    caplog.handler.setFormatter(logger.handlers[0].formatter)


def test_logging_format(
    caplog: pytest.LogCaptureFixture,
    logger: logging.Logger,
) -> None:
    """This test ensures logging is done correctly."""
    message = 'Test message'

    logger.error(message)

    assert _LOGGING_FORMAT_RE.match(caplog.text)
