# Nussinnov's Algorithm
# Find Max Pair

# Get pair score of a and b (0 if it is not a pair)
# You can change the return value to prioritize some pair
def getPairScore(a, b):
  if (a == 'U' and b == 'A') or (a == 'A' and b == 'U'):
    return 1
  if (a == 'G' and b == 'C') or (a == 'C' and b == 'G'):
    return 1
  if (a == 'G' and b == 'U') or (a == 'U' and b == 'G'):
    return 1
  return 0


# Backtrack for nussinnov to get dot bracket notation of the result
def backtrack(i, j, sequence, parent, result):
  if parent[i][j] == -1:
    return
  for (st, ed) in parent[i][j]:
    if st == i + 1 and ed == j - 1:
      if getPairScore(sequence[i], sequence[j]) > 0:
        result[i] = '('
        result[j] = ')'
    backtrack(st, ed, sequence, parent, result)


# Calculate max pairs and dot bracket notation of the result
def nussinnov(sequence):
  n = len(sequence)
  dp = [[0] * n for i in range(n)]
  parent = [[-1] * n for i in range(n)]

  for l in range(3, n + 1):
    for i in range(n - l + 1):
      j = i + l - 1

      dp[i][j] = -1

      if dp[i + 1][j - 1] + getPairScore(sequence[i], sequence[j]) > dp[i][j]:
        dp[i][j] = dp[i + 1][j - 1] + getPairScore(sequence[i], sequence[j])
        parent[i][j] = [(i + 1, j - 1)]

      if dp[i + 1][j] > dp[i][j]:
        dp[i][j] = dp[i + 1][j]
        parent[i][j] = [(i + 1, j)]

      if dp[i][j - 1] > dp[i][j]:
        dp[i][j] = dp[i][j - 1]
        parent[i][j] = [(i, j - 1)]

      for k in range(i + 1, j):
        if dp[i][k] + dp[k + 1][j] > dp[i][j]:
          dp[i][j] = dp[i][k] + dp[k + 1][j]
          parent[i][j] = [(i, k), (k + 1, j)]

  result = ["."] * n
  backtrack(i, j, sequence, parent, result)

  return (dp[0][n - 1], ''.join(result))


f = open("Algorithms/RnaInformatics/input.in", "r")
sequences = f.read().split('\n')

f = open("Algorithms/RnaInformatics/output.out", "w+")
for sequence in sequences:
  (pairs, result) = nussinnov(sequence)
  f.write("{} pairs\n".format(pairs))
  f.write(sequence + '\n')
  f.write(result + '\n\n')
