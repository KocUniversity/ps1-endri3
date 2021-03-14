n, B = list(map(int, input().strip().split()))
T = 0

# your code here
i = 1
res = 0
while T < 10000 and i <= n:
  if i % 2 == 0:
    res = (res + ((2**i + 1)**(n - i))) * T
  elif i % 2 != 0:
    res = (res + ((3**i + 1)**(n - i))) * T
  if res > B:
    break
  T += 1
  i += 1

# please do not modify the input and print statements
# and make sure that your code does not have any other print statements
print(T if T < 10000 else "-1")