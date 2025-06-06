from typing import List


def convert_to_snake_case(pascal_or_camel_cased_string: str) -> str:
    snake_cased_char_list: List[str] = [
        '_' + char.lower() if char.isupper()
        else char
        for char in pascal_or_camel_cased_string
    ]

    return ''.join(snake_cased_char_list).strip('_')

def main():
    print(convert_to_snake_case('aLongAndComplexString'))
    print(convert_to_snake_case('IAmAPascalCasedString'))

main()