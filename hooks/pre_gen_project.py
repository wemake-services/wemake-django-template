import re
import sys


MODULE_REGEX = r'^[a-z][_a-z0-9]+$'
MODULE_NAME = '{{ cookiecutter.project_name }}'

if not re.match(MODULE_REGEX, MODULE_NAME):
    message = (
        'ERROR: The project slug {} is not a valid Python module name.'
        'Please do not use a - and use _ instead'
    )
    print(message.format(MODULE_NAME))

    sys.exit(1)  # exit to cancel project.
