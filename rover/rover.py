from typing import List, Tuple


def generate_grid(m: int, n: int) -> List[Tuple[int, int]]:
    return [(x, y) for x in range(m) for y in range(n)]
