from unittest.mock import patch

from pytest_picked import _affected_tests


def test_shows_affected_tests(testdir):
    result = testdir.runpytest("--picked")

    assert "Changed test files..." in result.stdout.str()
    assert "Changed test folders..." in result.stdout.str()


def test_help_message(testdir):
    result = testdir.runpytest("--help")

    result.stdout.fnmatch_lines(
        ["picked:", "*--picked*Run the tests related to the changed files"]
    )


def test_filter_items_according_with_git_status(testdir, tmpdir):
    with patch("pytest_picked.subprocess.run") as subprocess_mock:
        output = b" M test_flows.py\n M test_serializers.py\n A tests/\n"
        subprocess_mock.return_value.stdout = output

        result = testdir.runpytest("--picked")
        testdir.makepyfile(
            ".py",
            test_flows="""
            def test_sth():
                assert True
            """,
            test_serializers="""
            def test_sth():
                assert True
            """,
        )
        tmpdir.mkdir("tests")
        result.stdout.fnmatch_lines(
            [
                "Changed test files... 2. "
                + "['test_flows.py', 'test_serializers.py']",
                "Changed test folders... 1. ['tests/']",
            ]
        )


def test_return_nothing_if_does_not_have_changed_test_files(testdir):
    with patch("pytest_picked.subprocess.run") as subprocess_mock:
        subprocess_mock.return_value.stdout = b""

        result = testdir.runpytest("--picked")

        result.stdout.fnmatch_lines(["Changed test files... 0. []"])


def test_return_error_if_not_git_repository(testdir):
    o = b"fatal: Not a git repository (or any of the parent directories): .git"
    with patch("pytest_picked.subprocess.run") as subprocess_mock:

        subprocess_mock.return_value.stdout = o

        result = testdir.runpytest("--picked")

        result.stdout.fnmatch_lines(["Changed test files... 0. []"])


def test_dont_call_the_plugin_if_dont_find_it_as_option(testdir):
    result = testdir.runpytest()

    assert "Changed test files..." not in result.stdout.str()


def test_filter_file_when_is_either_modified_and_not_staged(testdir):
    with patch("pytest_picked.subprocess.run") as subprocess_mock:
        output = b"MM test_picked.py\nM  tests/test_pytest_picked.py"
        subprocess_mock.return_value.stdout = output

        result = testdir.runpytest("--picked")
        testdir.makepyfile(
            ".py",
            test_flows="""
            def test_sth():
                assert True
            """,
            test_serializers="""
            def test_sth():
                assert True
            """,
        )
        result.stdout.fnmatch_lines(
            [
                "Changed test files... 2. "
                + "['test_picked.py', 'tests/test_pytest_picked.py']",
                "Changed test folders... 0. []",
            ]
        )


def test_handle_with_white_spaces(testdir):
    with patch("pytest_picked.subprocess.run") as subprocess_mock:
        output = (
            b" M school/tests/test_flows.py\n"
            + b"A  school/tests/test_serializers.py\n M sales/tasks.py"
        )
        subprocess_mock.return_value.stdout = output

        result = testdir.runpytest("--picked")
        testdir.makepyfile(
            ".py",
            test_flows="""
            def test_sth():
                assert True
            """,
            test_serializers="""
            def test_sth():
                assert True
            """,
        )
        result.stdout.fnmatch_lines(
            [
                "Changed test files... 2. "
                + "['school/tests/test_flows.py', "
                + "'school/tests/test_serializers.py']",
                "Changed test folders... 0. []",
            ]
        )


def test_check_parser():
    with patch("pytest_picked.subprocess.run") as subprocess_mock:
        output = (
            b"R  school/migrations/from-school.csv -> test_new_things.py\n"
            + b"D  school/migrations/0032_auto_20180515_1308.py\n"
            + b"?? Pipfile\n"
            + b"!! school/tests/test_rescue_students.py\n"
            + b"C  tests/\n"
            + b" M .pre-commit-config.yaml\n"
            + b" M picked.py\n"
            + b"A  setup.py\n"
            + b" U tests/test_pytest_picked.py\n"
            + b"?? random/tests/"
        )

        subprocess_mock.return_value.stdout = output
        files, folders = _affected_tests()

        expected_files = [
            "test_new_things.py",
            "school/tests/test_rescue_students.py",
            "tests/test_pytest_picked.py",
        ]
        expected_folders = ["tests/", "random/tests/"]

        assert files == expected_files
        assert folders == expected_folders


def test_should_match_with_the_begin_of_path(testdir, tmpdir, tmpdir_factory):
    with patch("pytest_picked.subprocess.run") as subprocess_mock:
        output = b" A tests/\n"
        subprocess_mock.return_value.stdout = output

        result = testdir.runpytest("--picked")
        tmpdir.mkdir("tests")
        tmpdir.mkdir("othertests")

        result.stdout.fnmatch_lines([
            "Changed test files... 0. []",
            "Changed test folders... 1. ['tests/']"
        ])
