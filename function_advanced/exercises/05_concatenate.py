def concatenate(*letters, **replacements):
    text = "".join(letters)
    for k in replacements:
        text = text.replace(k, replacements[k])

    return text


