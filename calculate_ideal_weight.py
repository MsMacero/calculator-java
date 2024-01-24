# calculator.py
def calculate_ideal_weight(gender, height_cm):
    ideal_weight = -1
    correction = height_cm - 152

    if gender == "male":
        ideal_weight = 48

        if correction > 0:
            ideal_weight += (correction * 1.1)

    elif gender == "female":
        ideal_weight = 45.5

        if correction > 0:
            ideal_weight += correction * 0.9

    return ideal_weight
