def multiply(number: float, n: int) -> float:
    ans = 1.0
    for _ in range(n):
        ans *= number
    return ans


def get_nth_root(n: int, m: int) -> float:
    low = 1.0
    high = float(m)
    eps = 1e-6  # Precision up to 5-6 decimal places

    while (high - low) > eps:
        mid = (low + high) / 2.0
        if multiply(mid, n) < m:
            low = mid
        else:
            high = mid

    # low and high are within epsilon of each other
    return low


if __name__ == "__main__":
    n = 3
    m = 27
    result = get_nth_root(n, m)
    print(f"{n}-th root of {m} is: {result:.6f}")
    print(f"Check with built-in: {m ** (1.0 / n):.6f}")