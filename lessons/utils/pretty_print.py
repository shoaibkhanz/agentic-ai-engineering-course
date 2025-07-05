import json
from typing import Iterable


class Color:
    YELLOW = "\033[93m"
    RESET = "\033[0m"


def wrapped_print(text: Iterable[str] | dict | str, title: str = "", indent: int = 0, width: int = 100) -> None:
    header = (
        f"{Color.YELLOW}{'-' * ((width - len(title)) // 2 - 1)} {title} {'-' * ((width - len(title)) // 2 - 1)}{Color.RESET}"  # noqa: E501
        if title
        else f"{Color.YELLOW}{'-' * width}{Color.RESET}"  # noqa: E501
    )
    separator = f"{Color.YELLOW}{'-' * width}{Color.RESET}"

    if isinstance(text, str):
        text = [text]
    elif isinstance(text, dict):
        text = [json.dumps(text, indent=indent)]

    print(header)
    for line in text:
        print(f"{' ' * indent}{line}")
        print(separator)
