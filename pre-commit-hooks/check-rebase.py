#!/usr/bin/env python3
from pathlib import Path
import subprocess
import sys

WARNING_MSG_1 = (
    "Your branch is not up to date with upstream/master. \n"
    "SHA of the last commit of upstream/master: {upstream}\n"
    "Please, rebase! \n"
)

WARNING_MSG_2 = (
    "Zuul merged the master, which means your branch is not up to date with upstream/master.\n"
    "Please, rebase! \n"
)


def main():
    path = str(Path.cwd().absolute())

    last_commit_subject = subprocess.run(
        ["git", "log", "--format=%s", "-1"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        cwd=path,
    ).stdout.decode()
    print(f"Last commit subject: {last_commit_subject}")

    if "Merge commit" in last_commit_subject:
        print(WARNING_MSG_2)
        return 2

    local_hashes = (
        subprocess.run(
            ["git", "log", "--max-count=100", "--format=%H"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            cwd=path,
        )
        .stdout.decode()
        .split()
    )

    upstream_hash = (
        subprocess.run(
            ["git", "ls-remote", str(sys.argv[1]), "HEAD"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            cwd=path,
        )
        .stdout.decode()
        .split()[0]
    )

    print(f"Upstream hash: {upstream_hash}\n" f"Local hashes: {local_hashes[:3]}\n")

    if upstream_hash in local_hashes:
        return 0
    print(WARNING_MSG_1.format(upstream=upstream_hash))
    return 1


if __name__ == "__main__":
    exit(main())
