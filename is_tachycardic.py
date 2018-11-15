

def is_tachycardic(hr, age):
    if hr > 186:
        tachy = True
    elif hr > 151 and 1 <= age <= 2:
        tachy = True
    elif hr > 137 and 3 <= age <= 4:
        tachy = True
    elif hr > 133 and 5 <= age <= 7:
        tachy = True
    elif hr > 130 and 8 <= age <= 12:
        tachy = True
    elif hr > 119 and 13 <= age <= 15:
        tachy = True
    elif hr > 100 and age > 15:
        tachy = True
    else:
        tachy = False

    return tachy
