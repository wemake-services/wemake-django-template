import subprocess

import _pytest.config


def pytest_addoption(parser):
    group = parser.getgroup("picked")
    group.addoption(
        "--picked",
        action="store_true",
        dest="picked",
        help="Run the tests related to the changed files",
    )


def pytest_collection_modifyitems(items, config):
    picked_plugin = config.getoption("picked")
    if not picked_plugin:
        return

    picked_files, picked_folders = _affected_tests()
    _display_affected_tests(config, picked_files, picked_folders)

    to_be_tested = []
    for item in items:
        location = item.location[0]
        if location in picked_files:
            to_be_tested.append(item)
        else:
            for folder in picked_folders:
                if location.startswith(folder):
                    to_be_tested.append(item)
                    break
    items[:] = to_be_tested


def _display_affected_tests(config, files, folders):
    writer = _pytest.config.create_terminal_writer(config)
    writer.line()
    message = "Changed test {}... {}. {}"
    files_msg = message.format("files", len(files), files)
    folders_msg = message.format("folders", len(folders), folders)
    writer.line(files_msg)
    writer.line(folders_msg)


def _affected_tests():
    """
    Parse affected tests from `git status --short`.

    The command output would look like this:
    A  setup.py
     U tests/test_pytest_picked.py
    ?? .pylintrc

    The first two digits are M, A, D, R, C, U, ? or !
    The third is a white-space and the left is the path of
    the file.
    If the file was renamed, it will look like this:
    R  school/migrations/from-school.csv -> new-things-from-school.csv

    Reference:
    https://git-scm.com/docs/git-status#git-status---short
    """
    raw_output = _get_git_status()

    folders, files = [], []
    for candidate in raw_output.splitlines():
        file_or_folder = _extract_file_or_folder(candidate)

        if "test" in file_or_folder:
            if file_or_folder.endswith("/"):
                folders.append(file_or_folder)
            elif file_or_folder.endswith(".py"):
                files.append(file_or_folder)
    return files, folders


def _extract_file_or_folder(candidate):
    start_path_index = 3
    rename_indicator = "-> "

    if rename_indicator in candidate:
        indicator_index = candidate.find(rename_indicator)
        start_path_index = indicator_index + len(rename_indicator)
    return candidate[start_path_index:]


def _get_git_status():
    command = ["git", "status", "--short"]
    output = subprocess.run(command, stdout=subprocess.PIPE)
    return output.stdout.decode("utf-8")


# TODO branch changed files git diff --name-only master
