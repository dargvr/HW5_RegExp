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


def get_chords_from_song_text(input_song_file: str) -> set:
    """
    Find chords in the song's text

    Arguments:
    input_song_file: str: the path to the file

    Returns:
    set: a set of chords from input_song_file
    """
    with open(input_song_file, encoding="utf-8") as song_file:
        song_text = song_file.read()
        pattern = r"\b[ABCDEFGH]\d?#?(?:sus|b|maj|m)?(?:/[ABCDEFGH])?(?:\d{1,2})?\b#?"  # Извините, раньше играла на гитаре, решила побаловаться-поприкаловаться
        chords = set(re.findall(pattern, song_text))
        return chords
