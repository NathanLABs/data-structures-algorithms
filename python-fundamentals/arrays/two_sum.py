"""
Two Sum
Diberikan list angka `nums` dan target `target`, cari 2 index yang
angkanya kalau dijumlah = target.

Contoh:
    nums = [2, 7, 11, 15], target = 9
    output: [0, 1]  (karena nums[0] + nums[1] == 9)
"""


def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))  # [0, 1]
