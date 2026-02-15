#!/usr/bin/env python3
"""
Push Changes to GitHub - Updates parampateldev.github.io
Usage: python pushChanges.py [commit message]
If no message is provided, prompts for one.
"""

import subprocess
import sys
import os


def run(cmd: list[str], cwd: str | None = None) -> subprocess.CompletedProcess:
    """Run a shell command and return the result."""
    return subprocess.run(cmd, cwd=cwd or os.getcwd(), capture_output=True, text=True)


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)

    # Check for uncommitted changes
    status = run(["git", "status", "--porcelain"])
    if not status.stdout.strip():
        print("Nothing to commit. Working tree is clean.")
        return

    # Get commit message
    if len(sys.argv) > 1:
        msg = " ".join(sys.argv[1:])
    else:
        msg = input("Commit message: ").strip() or "Update site"

    # Add all changes
    add = run(["git", "add", "."])
    if add.returncode != 0:
        print("Error adding files:")
        print(add.stderr)
        sys.exit(1)

    # Commit
    commit = run(["git", "commit", "-m", msg])
    if commit.returncode != 0:
        if "nothing to commit, working tree clean" in commit.stdout + commit.stderr:
            print("Nothing to commit (working tree clean).")
        else:
            print("Error committing:")
            print(commit.stderr)
        sys.exit(1)

    # Push to GitHub
    push = run(["git", "push", "origin", "main"])
    if push.returncode != 0:
        print("Error pushing to GitHub:")
        print(push.stderr)
        sys.exit(1)

    print("\n✅ Pushed to GitHub successfully!")
    print("   Site will update at https://parampateldev.github.io (may take 1–2 minutes)")


if __name__ == "__main__":
    main()
