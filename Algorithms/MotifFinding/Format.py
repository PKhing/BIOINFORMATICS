consensus = "ccataaatag"

f = open("Algorithms/MotifFinding/sequences.fastq", "r")
dnas = [s for s in f.read().split('\n') if len(s) > 0 and s[0] != '>']
print(dnas)
def count_mismatch(s1, s2):
  mismatch = 0
  for i in range(len(s1)):
    if s1[i] != s2[i]:
      mismatch += 1
  return mismatch

def find_location(s1, s2):
  min_mismatch = 1e9
  location = -1
  for i in range(len(s1) - len(s2) + 1):
    mismatch = count_mismatch(s2, s1[i:i + len(s2)])
    if mismatch < min_mismatch:
      min_mismatch = mismatch
      location = i
  return [location, min_mismatch]


sum = 0
positions = []
for dna in dnas:
  [location, mismatch] = find_location(dna, consensus)
  sum += mismatch
  print(mismatch)
  positions.append(location)

print(sum)

f = open("Algorithms/MotifFinding/output.out", "w+")

for dna, position in zip(dnas, positions):
  f.write(dna[:position] + dna[position:position +
                               10].upper() + dna[position + 10:] + '\n')
