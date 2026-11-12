def calculate_median(numbers):
    numbers.sort()
    n = len(numbers)

    if n % 2 == 0:
        median = (numbers[n // 2 - 1] + numbers[n // 2]) / 2
    else:
        median = numbers[n // 2]

    return median


list1 = [2, 4, 7, 8, 10, 12]
list2 = [2, 4, 7, 8, 10, 12, 14]

print("Median of even list:", calculate_median(list1))
print("Median of odd list:", calculate_median(list2))
