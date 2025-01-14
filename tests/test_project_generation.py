"""
Does some basic tests on the generated project.

Almost completely taken from (you guys rock!):
https://github.com/pydanny/cookiecutter-django/blob/master/tests
"""

import os
import re
from pathlib import Path
from typing import Final

import pytest
import tomli
from binaryornot.check import is_binary
from cookiecutter.exceptions import FailedHookException
from pytest_cookies.plugin import Cookies

_RE_OBJ: Final = re.compile(r'{{(\s?cookiecutter)[.](.*?)}}')


def _build_files_list(root_dir: Path) -> list[Path]:
    """Build a list containing absolute paths to the generated files."""
    return [
        Path(dirpath) / file_path
        for dirpath, _subdirs, files in os.walk(str(root_dir))
        for file_path in files
    ]


def assert_variables_replaced(paths: list[Path]) -> None:
    """Method to check that all paths have correct substitutions."""
    assert paths, 'No files are generated'

    for path in paths:
        if is_binary(str(path)):
            continue

        file_contents = path.read_text()

        match = _RE_OBJ.search(file_contents)
        msg = 'cookiecutter variable not replaced in {0} at {1}'

        # Assert that no match is found:
        assert match is None, msg.format(path, match.start())


def test_with_default_configuration(
    cookies: Cookies,
    context: dict[str, str],
) -> None:
    """Tests project structure with default prompt values."""
    baked_project = cookies.bake(extra_context=context)

    assert baked_project.exit_code == 0
    assert baked_project.exception is None
    assert baked_project.project_path.name == context['project_name']
    assert baked_project.project_path.is_dir()


def test_variables_replaced(
    cookies: Cookies,
    context: dict[str, str],
) -> None:
    """Ensures that all variables are replaced inside project files."""
    baked_project = cookies.bake(extra_context=context)
    paths = _build_files_list(baked_project.project_path)

    assert_variables_replaced(paths)


def test_pyproject_toml(
    cookies: Cookies,
    context: dict[str, str],
) -> None:
    """Ensures that all variables are replaced inside project files."""
    baked_project = cookies.bake(extra_context=context)
    path = baked_project.project_path / 'pyproject.toml'

    pyproject = tomli.loads(path.read_text())
    project = pyproject['project']
    poetry = pyproject['tool']['poetry']

    assert project['name'] == context['project_name']
    assert project['description'] == context['project_verbose_name']
    assert poetry


@pytest.mark.parametrize(
    ('prompt', 'entered_value'),
    [
        ('project_name', 'myProject'),
        ('project_name', 'my_project'),
        ('project_name', '43project'),
        ('project_name', '_test'),
        ('project_name', 'test_'),
        ('project_name', '1_test'),
        ('project_name', 'test@'),
        ('project_name', '0123456'),
        ('project_domain', 'https://wemake.services'),
        ('project_domain', 'wemake.services?search=python'),
        ('project_domain', ''),
    ],
)
def test_validators_work(
    prompt: str,
    entered_value: str,
    cookies: Cookies,
    context: dict[str, str],
) -> None:
    """Ensures that project can not be created with invalid name."""
    context.update({prompt: entered_value})
    baked_project = cookies.bake(extra_context=context)

    assert isinstance(baked_project.exception, FailedHookException)
    assert baked_project.exit_code == -1
