from typing import final

import msgspec


@final
class IntIdPath(msgspec.Struct):
    """Common structure to use where APIs need to use ``id`` as a path param."""

    id: int
