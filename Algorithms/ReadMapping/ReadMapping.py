# Get BWT from sequence
def getBwt(sequence):
  sequence = sequence + '$'
  sortedSequence = sorted([(sequence[i:], i) for i in range(len(sequence))])
  return "".join([sequence[position - 1] for (_, position) in sortedSequence])

# Get bwt map from current to before
def getBwtMap(bwt):
  # Generate number to distinguish the same character
  def generateNumber(bwt):
    def getCharIndex(char):
      if char == '$':
        return 24
      return ord(char) - ord('a')

    no = [0] * 25
    result = []
    for char in bwt:
      idx = getCharIndex(char)
      result.append(char + str(no[idx]))
      no[idx] += 1
    return result

  bwt = generateNumber(bwt)
  sortedBwt = sorted(bwt)
  return (sortedBwt, {sortedBwt[i]: bwt[i] for i in range(len(bwt))})

# Deconstruct sequence from BWT
def reconstructSequence(bwt):
  (sortedBwt, before) = getBwtMap(bwt)
  current = sortedBwt[0]
  result = ""
  while True:
    result = current[0] + result
    current = before[current]
    if current == '$0':
      break
  return result

# Get position of each char in the original sequence
def getPosition(bwt):
  (sortedBwt, before) = getBwtMap(bwt)
  current = sortedBwt[0]
  position = {}
  count = 1
  while True:
    position[current] = len(bwt) - count
    count += 1
    current = before[current]
    if current == '$0':
      break
  return position

# Find position of string that exact match with the pattern
def findExactMatch(bwt, pattern):
  return findMatch(bwt, pattern, 0)

# Find position of string that has mismatch less than maxMismatch
def findMatch(bwt, pattern, maxMismatch):
  (sortedBwt, before) = getBwtMap(bwt)
  position = getPosition(bwt)
  pattern = pattern[::-1]
  result = []

  for char in sortedBwt:
    mismatch = 0
    currentChar = char
    for patternChar in pattern:
      if patternChar != currentChar[0]:
        mismatch += 1
        if mismatch > maxMismatch:
          break
      currentChar = before[currentChar]
    if mismatch <= maxMismatch:
      result.append(position[char] - len(pattern) + 1)

  return sorted(result)


bwt = getBwt('panamabananas')
print(findMatch(bwt, 'ban', 1))
