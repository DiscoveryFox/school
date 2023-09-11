import math
from typing import List, Generator


def simple_calculate_prime(list_of_prime_factors: list[int]) -> int:
    last_number: int = 1
    for number in list_of_prime_factors:
        last_number *= number
    return last_number


def count_occurrences(list_of_prime_factors: list[int], target: int) -> int:
    return list_of_prime_factors.count(target)


def _translate_normal_to_the_power_of_list(
        list_of_prime_factors: list[int],
) -> list[tuple[int, int]]:
    for number in set(list_of_prime_factors):
        yield number, count_occurrences(list_of_prime_factors, number)


def translate_normal_to_the_power_of_list(
        list_of_prime_factors: list[int],
) -> list[tuple[int, int]]:
    return list(
        _translate_normal_to_the_power_of_list(
            list_of_prime_factors=list_of_prime_factors
        )
    )


def prime_factors_generator(n: int) -> Generator[int, None, None]:
    while n % 2 == 0:  # Wir terminieren alle geraden Zahlen
        yield 2
        n //= 2

    for divisor in range(3, int(math.sqrt(n)) + 1, 2):
        while n % divisor == 0:
            yield divisor
            n //= divisor

    if n > 1:
        yield n


def get_prime_factors(n: int, simplified_output: bool = True) -> List[int]:
    return (
        list(prime_factors_generator(n))
        if simplified_output is False
        else translate_normal_to_the_power_of_list(list(prime_factors_generator(n)))
    )
