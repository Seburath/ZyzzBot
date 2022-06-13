from math import log


class Calculator:
    def get_fat_percentage(height, neck, waist, gender="m", hip=0):
        if gender == "m":
            return (
                495
                / (
                    1.0324
                    - 0.19077 * log((waist - neck), 10)
                    + 0.15456 * log(height, 10)
                )
                - 450
            )
        if gender == "f":
            return (
                495
                / (
                    1.29579
                    - 0.35004 * log((waist + hip - neck), 10)
                    + 0.22100 * log(height, 10)
                )
                - 450
            )

        return 0

    def get_fat_score(fat_percentage, gender="m"):
        if gender == "m":
            return -3.3333 * fat_percentage + 126.67
        if gender == "f":
            return -2.6316 * fat_percentage + 139.49

        return 0

    def get_ffmi(height, weight, fat_percentage):
        lean_mass = weight * (1 - (fat_percentage / 100))
        ffmi = lean_mass / ((height / 100) * (height / 100))
        ffmi = ffmi + (6.1 * (1.8 - height / 100))

        return ffmi

    def get_ffmi_score(ffmi, gender="m"):
        if gender == "m":
            return 10 * ffmi - 150
        if gender == "f":
            return 10 * ffmi - 100

        return 0


if __name__ == "__main__":
    print("/" * 54)
    print("gender, neck, height, weight, waist, hip")
    print("example: m 42 171 75 86 0")
    datos = input()
    gender = datos[:1]
    neck, height, weight, waist, hip = map(int, datos[2:].split(" "))

    fat_percentage = Calculator.get_fat_percentage(
        height, neck, waist, gender="m", hip=0
    )
    fat_score = Calculator.get_fat_score(fat_percentage, gender="m")

    ffmi = Calculator.get_ffmi(height, weight, fat_percentage)
    ffmi_score = Calculator.get_ffmi_score(ffmi, gender="m")

    total_score = (fat_score + ffmi_score) / 2

    print("Body Fat %: " + str(fat_percentage))
    print("FFMI: " + str(ffmi))
    print("/" * 20, "SCORE / 100", "/" * 20)
    print("Fat: " + str(int(fat_score)))
    print("Muscle: " + str(int(ffmi_score)))
    print("Total: " + str(int(total_score)))
