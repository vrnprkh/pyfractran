def update(n, num, denum):
  for i in range(len(num)):
    if (n * num[i]) % denum[i] == 0:
      return int(n * num[i] / denum[i])

  return n
# a
# n = initialState
# num = list of numerators
# denum = list of denominators
# max = max iterations to run, 0 for until stop
# printNewState = true or false, if true, print n every time it is updated
def run(n, num, denum, max = 0, printNewState = 0):
  iter = 1
  while True:
    if printNewState:
      print(n)
    new = update(n, num, denum)
    if new == n:
      return n
    n = new
    if iter == max:
      return n
    iter += 1


# sample code
# n = 2
# num = [17, 78, 19, 23, 29, 77, 95, 77, 1, 11, 13, 15, 1, 55]
# denum = [91, 85, 51, 38, 33, 29, 23, 19, 17, 13, 11, 2, 7, 1]

# print(run(n, num, denum, 100))