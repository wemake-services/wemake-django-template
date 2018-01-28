# -*- coding: utf-8 -*-

"""
Does some basic tests on the generated project.

Almost completely taken from (you guys rock!):
https://github.com/pydanny/cookiecutter-django/blob/master/tests
"""

import os
import re

import pytest
from binaryornot.check import is_binary
from cookiecutter.exceptions import FailedHookException

PATTERN = r'{{(\s?cookiecutter)[.](.*?)}}'
RE_OBJ = re.compile(PATTERN)


@pytest.fixture
def context():
    return {
        'project_name': 'test_project',
        'project_verbose_name': 'Test Project',
        'project_domain': 'myapp.com',
        'organization': 'wemake.services',
        'docker': 'y',
    }


@pytest.fixture
def no_docker_context(context):
    context.update({'docker': 'n'})
    return context


def build_files_list(root_dir):
    """Build a list containing absolute paths to the generated files."""
    return [
        os.path.join(dirpath, file_path)
        for dirpath, subdirs, files in os.walk(root_dir)
        for file_path in files
    ]


def assert_variables_replaced(paths):
    """Method to check that all paths have correct substitutions."""
    for path in paths:
        if is_binary(path):
            continue

        with open(path, 'r') as f:
            contents = f.read()

        match = RE_OBJ.search(contents)
        msg = 'cookiecutter variable not replaced in {} at {}'

        # Assert that no match is found:
        assert match is None, msg.format(path, match.start())


def test_with_default_configuration(cookies, context):
    result = cookies.bake(extra_context=context)
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.basename == context['project_name']
    assert result.project.isdir()


def test_with_no_docker(cookies, no_docker_context):
    result = cookies.bake(extra_context=no_docker_context)
    assert result.exit_code == 0
    assert result.exception is None

    files = (
        'docker-compose.yml',
        'docker-compose.override.yml',
        '.gitlab-ci.yml',
        '.dockerignore',
        'docs/_pages/template/docker.rst',
        'docs/_pages/template/pycharm.rst',
        'docs/_pages/template/gitlab-ci.rst',
        'docs/_pages/template/going-to-production.rst',
        'docs/_pages/template/production.rst',
    )

    for f in files:
        assert not os.path.isfile(result.project.join(f))

    folders = (
        'docker',
        '.idea',
    )

    for f in folders:
        assert not os.path.isdir(result.project.join(f))


def test_variables_replaced(cookies, context):
    result = cookies.bake(extra_context=context)
    paths = build_files_list(str(result.project))

    assert paths
    assert_variables_replaced(paths)


@pytest.mark.parametrize('prompt,entered_value', [
    ('project_name', 'myProject'),
    ('project_name', '43prject'),
    ('project_name', '_test'),
    ('project_domain', 'https://wemake.services'),
    ('project_domain', 'wemake.services?search=python'),
])
def test_validators_work(prompt, entered_value, cookies, context):
    context.update({prompt: entered_value})
    result = cookies.bake(extra_context=context)

    assert isinstance(result.exception, FailedHookException)
    assert result.exit_code == -1
