NUMBER_FOR_REST_CPF = 11

CPF = {
    "first_digit": [10, 9, 8, 7, 6, 5, 4, 3, 2],
    "second_digit": [11, 10, 9, 8, 7, 6, 5, 4, 3, 2],
}

CNPJ = {
    "first_digit": [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2],
    "second_digit": [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2],
}


def extract_digits(value):
    return "".join(list(filter(lambda x: x.isdigit(), value)))


def calculate_first_digit_cpf(value: str):
    combinations = list(
        zip(CPF.get("first_digit"), [int(x) for x in value[:10]])
    )
    sum_ = 0
    for item in combinations:
        x, y = item
        sum_ += x * y
    rest_of_division = sum_ % NUMBER_FOR_REST_CPF
    result = (
        0 if rest_of_division < 2 else NUMBER_FOR_REST_CPF - rest_of_division
    )
    return result == int(value[9])


def calculate_second_digit_cpf(value: str):
    combinations = list(
        zip(CPF.get("second_digit"), [int(x) for x in value[:11]])
    )
    sum_ = 0
    for item in combinations:
        x, y = item
        sum_ += x * y
    rest_of_division = sum_ % NUMBER_FOR_REST_CPF
    result = (
        0 if rest_of_division < 2 else NUMBER_FOR_REST_CPF - rest_of_division
    )
    return result == int(value[10])


def calculate_first_digit_cnpj(value: str):
    combinations = list(
        zip(CNPJ.get("first_digit"), [int(x) for x in value[:12]])
    )
    sum_ = 0
    for item in combinations:
        x, y = item
        sum_ += x * y
    rest_of_division = sum_ % NUMBER_FOR_REST_CPF
    result = (
        0 if rest_of_division < 2 else NUMBER_FOR_REST_CPF - rest_of_division
    )
    return result == int(value[12])


def calculate_second_digit_cnpj(value: str):
    combinations = list(
        zip(CNPJ.get("second_digit"), [int(x) for x in value[:13]])
    )
    sum_ = 0
    for item in combinations:
        x, y = item
        sum_ += x * y
    rest_of_division = sum_ % NUMBER_FOR_REST_CPF
    result = (
        0 if rest_of_division < 2 else NUMBER_FOR_REST_CPF - rest_of_division
    )
    return result == int(value[13])


def valida_cpf_cnpj(value: str):
    value = extract_digits(value)
    if len(value) == 11:
        return calculate_first_digit_cpf(value) and calculate_second_digit_cpf(
            value
        )
    if len(value) == 14:
        return calculate_first_digit_cnpj(
            value
        ) and calculate_second_digit_cnpj(value)
    else:
        return f"{value} is invalid"
