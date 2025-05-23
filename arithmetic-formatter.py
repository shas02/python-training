from typing import List

def arithmetic_arranger(problems: List[str], show_answers: bool = False):
    if len(problems) > 5:
        raise ValueError('Error: Too many problems.')

    topParts: str = '\n'
    bottomParts: str = '\n'
    dashesParts: str = '\n'
    results: str = ''

    for problem in problems:
        partsOfProblem: List[str] = problem.split(' ')

        number1: str = partsOfProblem[0]
        validateNumber(number1)

        number2: str = partsOfProblem[2]
        validateNumber(number2)

        operator: str = partsOfProblem[1]
        validateOperator(operator)

        partLen: int = getPartLen(number1, number2)

        topParts += formTopPart(number1, partLen)
        bottomParts += formBottomPart(operator, number2, partLen)
        dashesParts += formDashes(partLen)

        if show_answers:
            result: int = calculateResult(number1, number2, operator)
            results += formResultPart(result, partLen)

    topParts += '\n'
    bottomParts += '\n'

    butyfiedProblems: str = ''
    butyfiedProblems += topParts
    butyfiedProblems += bottomParts
    butyfiedProblems += dashesParts
    if show_answers:
        dashesParts += '\n'
        butyfiedProblems += results

    return butyfiedProblems

def validateNumber(number: str):
    if not number.isdigit():
        raise ValueError('Error: Numbers must only contain digits.')
    if len(number) > 4:
        raise ValueError('Error: Numbers cannot be more than four digits.')

def validateOperator(operator: str):
    if not operator == "+" and not operator == "-":
        raise ValueError("Error: Operator must be '+' or '-'.")

def getPartLen(number1: str, number2: str) -> int:
    number1Len: int = len(number1)
    number2Len: int = len(number2)
    if number1Len > number2Len:
        longestNumberLen = number1Len
    else:
        longestNumberLen = number2Len

    return longestNumberLen + 2


def formTopPart(number: str, partLen: int) -> str:
    topPart: str = ''
    for _ in range(partLen - len(number)):
        topPart += " "
    topPart += number + "    "
    return topPart

def formBottomPart(operator: str, number: str, partLen: int) -> str:
    bottomPart: str = operator + ' '
    for _ in range(partLen - 2 - len(number)):
        bottomPart += " "
    bottomPart += number + "    "
    return bottomPart

def formDashes(partLen: int) -> str:
    dashes: str = ''
    for _ in range(partLen):
        dashes += "-"
    dashes += "    "
    return dashes

def calculateResult(number1: str, number2: str, operator: str) -> int:
    number1Int: int = int(number1)
    number2Int: int = int(number2)
    result: int = 0
    if operator == "+":
        result = number1Int + number2Int
    elif operator == "-":
        result = number1Int - number2Int
    return result

def formResultPart(result: int, partLen: int) -> str:
    resultPart: str = ''
    resultStr: str = str(result)
    for _ in range(partLen - len(resultStr)):
        resultPart = " " + resultPart

    resultPart += resultStr + "    "

    return resultPart


print(f'\n{arithmetic_arranger(["3801 - 2", "123 + 49"])}')