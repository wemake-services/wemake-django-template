# -*- coding: utf-8 -*-

"""
Does some basic tests on the generated project.

Almost completely taken from (you guys rock!):
https://github.com/pydanny/cookiecutter-django/blob/master/tests
"""

import os
import re

import pytest
import tomlkit
from binaryornot.check import is_binary
from cookiecutter.exceptions import FailedHookException

PATTERN = r'{{(\s?cookiecutter)[.](.*?)}}'
RE_OBJ = re.compile(PATTERN)


def build_files_list(root_dir):
    """Build a list containing absolute paths to the generated files."""
    return [
        os.path.join(dirpath, file_path)
        for dirpath, _subdirs, files in os.walk(root_dir)
        for file_path in files
    ]


def assert_variables_replaced(paths):
    """Method to check that all paths have correct substitutions."""
    assert paths, 'No files are generated'

    for path in paths:
        if is_binary(path):
            continue

        with open(path, 'r') as template_file:
            file_contents = template_file.read()

        match = RE_OBJ.search(file_contents)
        msg = 'cookiecutter variable not replaced in {0} at {1}'

        # Assert that no match is found:
        assert match is None, msg.format(path, match.start())


def test_with_default_configuration(cookies, context):
    """Tests project structure with default prompt values."""
    baked_project = cookies.bake(extra_context=context)

    assert baked_project.exit_code == 0
    assert baked_project.exception is None
    assert baked_project.project.basename == context['project_name']
    assert baked_project.project.isdir()


def test_variables_replaced(cookies, context):
    """Ensures that all variables are replaced inside project files."""
    baked_project = cookies.bake(extra_context=context)
    paths = build_files_list(str(baked_project.project))

    assert_variables_replaced(paths)


def test_pyproject_toml(cookies, context):
    """Ensures that all variables are replaced inside project files."""
    baked_project = cookies.bake(extra_context=context)
    path = os.path.join(str(baked_project.project), 'pyproject.toml')

    with open(path) as pyproject:
        poetry = tomlkit.parse(pyproject.read())['tool']['poetry']

    assert poetry['name'] == context['project_name']
    assert poetry['description'] == context['project_verbose_name']


@pytest.mark.parametrize(('prompt', 'entered_value'), [
    ('project_name', 'myProject'),
    ('project_name', '43prject'),
    ('project_name', '_test'),
    ('project_name', 'test_'),
    ('project_name', '1_test'),
    ('project_name', 'test@'),
    ('project_name', '0123456'),
    ('project_domain', 'https://wemake.services'),
    ('project_domain', 'wemake.services?search=python'),
    ('project_domain', ''),
])
def test_validators_work(prompt, entered_value, cookies, context):
    """Ensures that project can not be created with invalid name."""
    context.update({prompt: entered_value})
    baked_project = cookies.bake(extra_context=context)

    assert isinstance(baked_project.exception, FailedHookException)
    assert baked_project.exit_code == -1
