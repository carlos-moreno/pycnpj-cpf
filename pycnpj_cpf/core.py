from re import sub

NUMBER_FOR_REST = 11
SIZE_CPF = 11
SIZE_CNPJ = 14
PATTERN = r"[.\-/]"

CPF = {
    "first_digit": [10, 9, 8, 7, 6, 5, 4, 3, 2],
    "second_digit": [11, 10, 9, 8, 7, 6, 5, 4, 3, 2],
}

CNPJ = {
    "first_digit": [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2],
    "second_digit": [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2],
}


def remove_punctuation(value: str) -> str:
    return sub(PATTERN, "", value)


def extract_digits(value: str) -> str:
    return "".join(list(filter(lambda x: x.isdigit(), value)))


def check_value_cpf(value: str) -> bool:
    value = remove_punctuation(value)
    return value.isdigit() and len(value) == SIZE_CPF


def check_value_cnpj(value: str) -> bool:
    value = remove_punctuation(value)
    return value.isdigit() and len(value) == SIZE_CNPJ


def first_digit_cpf_checker_is_valid(value: str) -> bool:
    value = remove_punctuation(value)
    if check_value_cpf(value):
        combinations = list(
            zip(CPF.get("first_digit"), [int(x) for x in value[:10]])
        )
        sum_ = 0
        for item in combinations:
            x, y = item
            sum_ += x * y
        rest_of_division = sum_ % NUMBER_FOR_REST
        result = (
            0 if rest_of_division < 2 else NUMBER_FOR_REST - rest_of_division
        )
        return result == int(value[9])
    else:
        return False


def second_digit_cpf_checker_is_valid(value: str) -> bool:
    value = remove_punctuation(value)
    if check_value_cpf(value):
        combinations = list(
            zip(CPF.get("second_digit"), [int(x) for x in value[:11]])
        )
        sum_ = 0
        for item in combinations:
            x, y = item
            sum_ += x * y
        rest_of_division = sum_ % NUMBER_FOR_REST
        result = (
            0 if rest_of_division < 2 else NUMBER_FOR_REST - rest_of_division
        )
        return result == int(value[10])
    else:
        return False


def first_digit_cnpj_checker_is_valid(value: str) -> bool:
    value = remove_punctuation(value)
    if check_value_cnpj(value):
        combinations = list(
            zip(CNPJ.get("first_digit"), [int(x) for x in value[:12]])
        )
        sum_ = 0
        for item in combinations:
            x, y = item
            sum_ += x * y
        rest_of_division = sum_ % NUMBER_FOR_REST
        result = (
            0 if rest_of_division < 2 else NUMBER_FOR_REST - rest_of_division
        )
        return result == int(value[12])
    else:
        False


def second_digit_cnpj_checker_is_valid(value: str) -> bool:
    value = remove_punctuation(value)
    if check_value_cnpj(value):
        combinations = list(
            zip(CNPJ.get("second_digit"), [int(x) for x in value[:13]])
        )
        sum_ = 0
        for item in combinations:
            x, y = item
            sum_ += x * y
        rest_of_division = sum_ % NUMBER_FOR_REST
        result = (
            0 if rest_of_division < 2 else NUMBER_FOR_REST - rest_of_division
        )
        return result == int(value[13])
    else:
        False


def cnpj_or_cpf_is_valid(value: str) -> bool:
    value = remove_punctuation(value)
    result = False
    if len(value) == SIZE_CPF and (
        first_digit_cpf_checker_is_valid(value)
        and second_digit_cpf_checker_is_valid(value)
    ):
        result = True
    if len(value) == SIZE_CNPJ and (
        first_digit_cnpj_checker_is_valid(value)
        and second_digit_cnpj_checker_is_valid(value)
    ):
        result = True
    return result
