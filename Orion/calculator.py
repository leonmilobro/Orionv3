def rechnen(text):
    try:
        return str(eval(text))
    except:
        return None
