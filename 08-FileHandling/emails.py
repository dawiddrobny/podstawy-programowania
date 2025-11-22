import re
import os


def _get_email_file_path():
    module_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(module_dir, "email.txt")


def email_sender():
    with open(_get_email_file_path(), "r", encoding="utf-8") as file:
        content = file.read()

    pattern = r"From:\s*(?:[^<]+<)?([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})"
    match = re.search(pattern, content)

    if match:
        return match.group(1)
    return None


def email_recipient():
    with open(_get_email_file_path(), "r", encoding="utf-8") as file:
        content = file.read()

    pattern = r"To:\s*(?:[^<]+<)?([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})"
    match = re.search(pattern, content)

    if match:
        return match.group(1)
    return None


def email_subject():
    with open(_get_email_file_path(), "r", encoding="utf-8") as file:
        content = file.read()

    pattern = r"Subject:\s*(.+?)(?:\n|$)"
    match = re.search(pattern, content, re.MULTILINE)

    if match:
        return match.group(1).strip()
    return None


def email_body():
    with open(_get_email_file_path(), "r", encoding="utf-8") as file:
        content = file.read()

    pattern = r"\n\n(.*)$"
    match = re.search(pattern, content, re.DOTALL)

    if match:
        return match.group(1).strip()
    return None
