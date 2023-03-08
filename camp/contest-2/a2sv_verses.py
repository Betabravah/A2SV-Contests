from collections import defaultdict

n, a, b = list(map(int, input().split()))
nums = list(map(int, input().split()))


def subarrays_with_sum_less(target):
    running = answer = left = 0

    for right in range(len(nums)):
        running += nums[right]

        while running >= target:
            running -= nums[left]
            left += 1

        answer += right - left + 1
    return answer

print(subarrays_with_sum_less(b + 1) - subarrays_with_sum_less(a))