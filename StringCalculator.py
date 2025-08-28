import re

def stringCalculator(numbers: str) -> int | bool:
    if numbers is None or numbers.strip() == "":
        return 0

    delimiters, numbers = _get_delimiters(numbers)
    tokens = _split_numbers(numbers, delimiters)

    if not _validate_tokens(tokens):
        return False

    return _convert_and_sum(tokens)


def _get_delimiters(numbers: str) -> tuple[list[str], str]:
    delimiters = [",", "\n"]
    if numbers.startswith("//"):
        header, numbers = numbers.split("\n", 1)
        matches = re.findall(r"\[(.*?)\]", header)
        if matches:
            delimiters = [d for d in matches if d != ""]
        else:
            delimiters = [header[2:]]
    return delimiters, numbers


def _split_numbers(numbers: str, delimiters: list[str]) -> list[str]:
    pattern = _build_split_regex(delimiters)
    return re.split(pattern, numbers)


def _validate_tokens(tokens: list[str]) -> bool:
    return all(tok.strip() != "" for tok in tokens)


def _convert_and_sum(tokens: list[str]) -> int:
    nums = [int(tok) for tok in tokens]
    negatives = [n for n in nums if n < 0]
    if negatives:
        raise ValueError("negatives not allowed: " + ",".join(map(str, negatives)))
    return sum(n for n in nums if n < 1000)


def _build_split_regex(delimiters: list[str]) -> str:
    sorted_delims = sorted([d for d in delimiters if d != ""], key=len, reverse=True)
    escaped = [re.escape(d) for d in sorted_delims]
    return r'(?:' + "|".join(escaped) + r')'
