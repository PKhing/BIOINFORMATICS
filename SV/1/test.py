f = open("bioinformatics/SV/1/reads1.fastq", "r")
reads1 = [s for s in f.read().split('\n') if len(s)>0 and s[0] != '>']
f = open("bioinformatics/SV/1/reads2.fastq", "r")
reads2 = [s for s in f.read().split('\n') if len(s)>0 and s[0] != '>']

f = open("bioinformatics/SV/1/output.txt", "a")

reference = "ATAGTGCCGTGGCCGCGGGACGGTACGGAGCCTATCCCCTCGCCAGCCGATTCTGCCACCCCGACGCACTGGCTACGGAGCCTATCCCCTCGCCAGCCGATTCTGCCACCCCGACGCACTGGCCGGGAGCCGTCGCTCGGGCGATGGCCG"

def count_mismatch(s1,s2):
  mismatch = 0
  for i in range(len(s1)):
    if s1[i] != s2[i]:
      mismatch += 1
  return mismatch

def find_location(s):
  min_mismatch = 1e9
  location = -1
  for i in range(len(reference)-len(s)):
    mismatch = count_mismatch(s, reference[i:i+len(s)])
    if mismatch < min_mismatch:
      min_mismatch = mismatch
      location = i
  return [location,min_mismatch]

def replace(s1,s2,location):
  return s1[:location] + s2 + s1[location+len(s2):]

lines = []
for i in range(len(reads1)):
  line = " "*(len(reference)+2)
  [location1,min_mismatch1] = find_location(reads1[i])
  [location2,min_mismatch2] = find_location(reads2[i])

  # if min_mismatch1 != 0:
  #   location1 = location2-20-len(reads2[i])
  # elif min_mismatch2 !=0 :
  #   location2 = location1+20+len(reads2[i])
  
  if location2 <= location1:
    location2 = location1+20+len(reads2[i])
  if location1+20+len(reads2[i]) != location2:
    location1 = location2-20-len(reads2[i])


  if min_mismatch1 == 0:
    line = replace(line,reads1[i]+'<1',location1)
  else:
    line = replace(line,reads1[i]+'<1*',location1)

  if min_mismatch2 == 0:
    line = replace(line,reads2[i]+'<2',location2)
  else:
    line = replace(line,reads2[i]+'<2*',location2)
    
  lines.append([min(location1,location2),line])

lines = sorted(lines)

for line in lines:
  f.write(line[1]+'\n')
f.close()