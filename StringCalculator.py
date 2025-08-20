import re

def stringCalculator(numbers: str) -> int | bool:
    if numbers is None or numbers.strip() == "":
        return 0

    delimiters = [",", "\n"]

    if numbers.startswith("//"):
        delimiter_part, numbers = numbers.split("\n", 1)
        delimiters = []
        matches = re.findall(r"\[(.*?)\]", delimiter_part)
        if matches:
            delimiters.extend(matches)
        else:
            delimiters.append(delimiter_part[2:])  # single char delimiter

    regex_pattern = "|".join(map(re.escape, delimiters))
    tokens = re.split(regex_pattern, numbers)

    # return False for malformed input
    if any(tok.strip() == "" for tok in tokens):
        return False

    nums = [int(tok) for tok in tokens]

    negatives = [n for n in nums if n < 0]
    if negatives:
        raise ValueError("negatives not allowed: " + ",".join(map(str, negatives)))

    return sum(n for n in nums if n < 1000)





# ---------- small helpers (procedural, single responsibility) ----------

def _extract_delimiter(numbers):
    """
    Returns (split_regex, numbers_part).
    Uses non-capturing groups in the regex so re.split returns only tokens.
    """
    if numbers.startswith("//"):
        header, body = numbers.split("\n", 1)
        decl = header[2:]  # after //
        # find bracketed delimiters like [***] or [*][%]
        bracketed = re.findall(r'\[(.*?)\]', decl)
        if bracketed:
            delims = [d for d in bracketed if d != ""]
        else:
            # single-char (or unbracketed multi-char) delimiter declaration
            delims = [decl] if decl != "" else []

        # keep default separators as well (comma and newline)
        all_delims = [d for d in delims] + [",", "\n"]
        return _build_split_regex(all_delims), body
    else:
        return _build_split_regex([",", "\n"]), numbers


def _build_split_regex(delimiters):
    """
    Build a non-capturing alternation regex to be used with re.split.
    Sort by length descending so longer delimiters are matched first.
    E.g. ['***', ',', '\n'] -> r'(?:\*\*\*|,|\n)'
    """
    # keep empty delimiters out
    delimiters = [d for d in delimiters if d is not None and d != ""]
    sorted_delims = sorted(delimiters, key=len, reverse=True)
    escaped = [re.escape(d) for d in sorted_delims]
    pattern = r'(?:' + "|".join(escaped) + r')'
    return pattern
