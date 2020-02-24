from typing import Dict


def format_output(
    header: str,
    d: Dict[str, float],
    width: int = 50,
    precision: int = 5,
    key_value_ratio: float = 0.8,
):
    msg = "\n"
    msg += f"{header}:".center(width + 2, " ") + "\n"
    msg += "-" * (width + 2)

    key_width = int(width * key_value_ratio)
    value_width = width - key_width
    format_str = f"\n{{k:{key_width}}}: {{t:>{value_width}.{precision}}} s"

    for k, t in d.items():
        msg += format_str.format(k=k, t=t)

    return msg
