#!/usr/bin/env sh
#
# Compare a command exit status to some given number(s) for a period of time.

# Created by https://github.com/ettore26/wait-for-command

CMD_NAME="${0##*/}"
CMD=""
STATUS=0
TIME=10
TIME_START=0
QUIET=0
EXIT_STATUS=1

usage() {
  cat << EOF >&2
Usage: ${CMD_NAME} [-c 'COMMAND']
       ${CMD_NAME} [OPTION]... [-c 'COMMAND']
       ${CMD_NAME} [-c 'COMMAND'] [OPTION]...

${CMD_NAME} compares a command exit status to some given number(s)
for a period of time. If comparison is successfully
${CMD_NAME} returns 0, otherwise 1.

Example: ${CMD_NAME} -c 'echo > /dev/tcp/127.0.0.1/5432'
     ${CMD_NAME} -s 0 57 -c 'curl 127.0.0.1:5432'
     ${CMD_NAME} -c 'nc -z 127.0.0.1 5432' -s 0 -t 20 -q

Options:
  -c, --command ['COMMAND']   execute a COMMAND.
  -s, --status [NUMBER]...    target exit status of COMMAND, default 0.
  -t, --time [NUMBER]         max time to wait in seconds, default 10.
  -q, --quiet                 do not make any output, default false.
      --help                  display this help.

Notice that quotes are needed after -c/--command for multi-argument
COMMANDs.

Specifying a same OPTION more than once overrides the previews.
So "${CMD_NAME} -c 'nothing' -c 'curl 127.0.0.1:5432'" will be
the same as "${CMD_NAME} -c 'curl 127.0.0.1:5432'".
It does not apply to option -q/--quiet.
EOF
  exit 0
}

output() {
  if [ "${QUIET}" -ne 1 ]; then
    printf "%s\n" "$*" 1>&2;
  fi
}

process_command() {
  while [ "$#" -gt 0 ]; do
    case "$1" in
      -c | --command)
    # allow one shift when no arguments
    if [ -n "$2" ]; then
      CMD="$2"
          shift 1
    fi
    shift 1
    ;;
      -s | --status)
    # ensure that a number is provided
    if ([ "$2" -eq "$2" ]) >/dev/null 2>&1; then
      unset STATUS
      # ensure that a number is provided
      while ([ "$2" -eq "$2" ]) >/dev/null 2>&1; do
        if [ -z "${STATUS}" ]; then
          STATUS="$2"
          shift 1
            else
          STATUS="${STATUS} $2"
          shift 1
        fi
          done
    fi
    shift 1
    ;;
      -t | --time)
    # ensure that a number is provided
    if ([ "$2" -eq "$2" ]) >/dev/null 2>&1; then
      TIME="$2"
      shift 1
    fi
    shift 1
    ;;
      -q | --quiet)
    QUIET=1
    shift 1
    ;;
      --help)
    usage
    ;;
      *)
    output "Unknown argument: $1"
    output "Try '${CMD_NAME} --help' for more information."
    exit "${EXIT_STATUS}"
    ;;
    esac
  done

  if [ -z "${CMD}" ]; then
    output "Missing command: -c, --command ['COMMAND']"
    output "Try '${CMD_NAME} --help' for more information."
    exit "${EXIT_STATUS}"
  fi
}

main() {
  message="failed"

  process_command "$@"

  TIME_START=$(date +%s)

  while [ $(($(date +%s)-TIME_START)) -lt "${TIME}" ]; do

    ($CMD) >/dev/null 2>&1 &
    pid="$!"

    # while both ps and time are running sleep 1s
    while kill -0 "${pid}" >/dev/null 2>&1 &&
          [ $(($(date +%s)-TIME_START)) -lt "${TIME}" ]; do
      sleep 1
    done

    # gets CMD status
    kill "${pid}" >/dev/null 2>&1
    wait "${pid}" >/dev/null 2>&1
    cmd_exit_status="$?"

    # looks for equlity in CMD exit status and one of the given status
    for i in $STATUS; do
      if ([ "${cmd_exit_status}" -eq "${i}" ]) >/dev/null 2>&1; then
        message="finished successfully"
    EXIT_STATUS=0
    break 2
      fi
    done

  done

  output "${CMD_NAME} ${message} after $(($(date +%s)-TIME_START)) second(s)."
  output "cmd:                 ${CMD}"
  output "target exit status:  ${STATUS}"
  output "exited status:       ${cmd_exit_status}"

  exit "${EXIT_STATUS}"
}

main "$@"
