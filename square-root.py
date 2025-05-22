from typing import Optional

def square_root_bisection(square_target: int, tolerance: float = 1e-7, max_iterations: int = 100) -> Optional[float]:
    root: Optional[float] = None

    if square_target < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')
    if square_target == 1:
        root = 1
        print(f'The square root of {square_target} is 1')
    elif square_target == 0:
        root = 0
        print(f'The square root of {square_target} is 0')

    else:
        low: float = 0
        high: float = max(1, square_target)

        for _ in range(max_iterations):
            mid: float = (low + high) / 2
            square_mid: float = mid**2

            if abs(square_mid - square_target) < tolerance:
                root = mid
                break
            elif square_mid < square_target:
                low = mid
            else:
                high = mid

        if root is None:
            print(f"Failed to converge within {max_iterations} iterations.")
        else:
            print(f'The square root of {square_target} is approximately {root}')

    return root

N = 16
square_root_bisection(N)