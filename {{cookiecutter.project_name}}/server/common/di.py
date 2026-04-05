from typing import Any, final

import punq

from server import implemented


class HasContainer:
    """
    Base class for all parts that use ``resolve()`` function.

    Must be the first base class.
    """

    __slots__ = ('_container',)

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Create container with dependencies for this class."""
        super().__init__(*args, **kwargs)
        self._container = implemented.populate_dependencies(punq.Container())

    @final
    def resolve[Thing](self, thing: type[Thing]) -> Thing:
        """Resolve a dependency."""
        return self._container.resolve(thing)  # type: ignore[no-any-return]
