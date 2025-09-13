# n = int(input())

# for i in range(1, n):
#     if i % n == 0:
#         for j in range(1, i):
#             if j % i == 0:


n = int(input())

for i in range(2, n+1):
    if n % i == 0:

        is_prime = True
        for j in range(2, i):
            if i % j  == 0:
                is_prime = False
                break

        if is_prime:
            print(i)