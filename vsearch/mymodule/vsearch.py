def search4letters(phrase: str, letters: str) -> set:
    """Ищет символы из letters в строке phrase.
       Возвращает их в виде множества"""
    return set(letters).intersection(set(phrase))
