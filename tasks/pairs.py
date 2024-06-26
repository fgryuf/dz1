from typing import Any

__all__ = (
    'corresponding_pairs',
)


def corresponding_pairs(arr1: list[Any], arr2: list[Any]) -> list[tuple[Any, Any]]:
    """
    Функция должна возвращать соответствующие элементы двух массивов:
    corresponding_pairs([1, 2], [3, 4]) == [(1, 3), (2, 4)]
    """
    n = min(len(arr1), len(arr2))
    ans = []
    for i in range(n):
        ans.append((arr1[i], arr2[i]))
    return ans
