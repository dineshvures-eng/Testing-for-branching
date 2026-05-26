from typing import List

def double(nums: List[int]) -> List[int]:
    return [n * 2 for n in nums]

if __name__ == "__main__":
    print(double([1, 2, 3]))
