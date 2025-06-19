from typing import List

def arithmetic_arranger(problems: List[str], show_answers: bool = False) -> str:
    if len(problems) > 5:
        return 'Error: Too many problems.'

    topParts: List[str] = []
    bottomParts: List[str] = []
    dashesParts: List[str] = []
    results: List[str] = []

    for problem in problems:
        parts: List[str] = problem.split(' ')
        
        if len(parts) != 3:
            return "Error: Invalid format."

        number1, operator, number2 = parts

        if not number1.isdigit() or not number2.isdigit():
            return "Error: Numbers must only contain digits."
        if len(number1) > 4 or len(number2) > 4:
            return "Error: Numbers cannot be more than four digits."
        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."

        width: int = max(len(number1), len(number2)) + 2

        topParts.append(number1.rjust(width))
        bottomParts.append(operator + number2.rjust(width - 1))
        dashesParts.append('-' * width)

        if show_answers:
            result = str(eval(number1 + operator + number2))
            results.append(result.rjust(width))

    arranged_problems: str = (
            '    '.join(topParts) + '\n' +
            '    '.join(bottomParts) + '\n' +
            '    '.join(dashesParts)
    )

    if show_answers:
        arranged_problems += '\n' + '    '.join(results)

    return arranged_problems


print(f'\n{arithmetic_arranger(["3801 - 2", "123 + 49"])}')