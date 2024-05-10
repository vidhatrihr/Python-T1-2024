# marks = input().split(',')

# marks.sort()
# print(marks)

# if len(marks) % 2 == 0:
#     middle_1 = len(marks) // 2 
#     middle_2 = len(marks) // 2 + 1
#     median = marks[middle_1] + marks[middle_2] // 2

# if len(marks) % 2 != 0:
#     middle = len(marks) // 2
#     median = marks[middle]
# print(median)

def solution(marks):
    
    sorted_marks = []

    while marks:
        min = marks[0]
        for x in marks:
            if x < min:
                min = x
                sorted_marks.append(min)
                marks.remove(min)
        n = len(sorted_marks)

        median = sorted_marks[n // 2] if n % 2 else (
            sorted_marks[int(n / 2)] + sorted_marks[int(n / 2 - 1)]
        )

        return median
    print(solution(marks))
    # print(
    #     solution(
    #     [90, 40, 40, 30, 60, 20]
    # ))