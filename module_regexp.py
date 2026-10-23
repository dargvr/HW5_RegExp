import re


def translate_to_salty_language(russian: str) -> str:
    """
    Translation of the Russian phrase or word into the salty language
    (Add the letter “c” after the vowel, followed by the same vowel)

    Arguments:
    russian: str: a phrase in Russian

    Returns:
    str: a phrase in salty language
    """
    pattern = r"([ауоыэяюёие])"
    replacement = r"\g<1>с\g<1>"
    salty = re.sub(pattern, replacement, russian, flags=re.I)
    return salty
