import re

def stringCalculator(numbers: str) -> int:
    if not numbers:
        return 0

    delimiter, numbers_part = _extract_delimiter(numbers)
    tokens = re.split(delimiter, numbers_part)

    nums = [int(t) for t in tokens if t.strip()]

    negatives = [n for n in nums if n < 0]
    if negatives:
        raise Exception(f"negatives not allowed: {','.join(map(str, negatives))}")

    return sum(n for n in nums if n <= 1000)


def _extract_delimiter(numbers: str) -> tuple[str, str]:
    if numbers.startswith("//"):
        header, body = numbers.split("\n", 1)
        delimiters = _parse_delimiters(header[2:])
        regex = "|".join(map(re.escape, delimiters))
        return regex, body
    else:
        return r"[,\n]", numbers

def _parse_delimiters(delim_decl: str) -> list[str]:
    if delim_decl.startswith("[") and delim_decl.endswith("]"):
        return re.findall(r"\[(.*?)\]", delim_decl)
    return [delim_decl]
