f = open("bioinformatics/Microbiome/Assignment2.2/microbiome_reads_1.txt", "r")
reads1 = [s for s in f.read().split('\n') if len(s)>0 and s[0] != '>']
f = open("bioinformatics/Microbiome/Assignment2.2/microbiome_reads_2.txt", "r")
reads2 = [s for s in f.read().split('\n') if len(s)>0 and s[0] != '>']

f = open("bioinformatics/Microbiome/Assignment2.2/output.txt", "w")


def ismatch(s1,s2):
  mismatch = 0
  for i in range(len(s1)):
    if s1[i] != s2[i]:
      mismatch += 1
  return mismatch == 0

length = len(reads1[0])-1

def connect(reads1,reads2):
  used = set()
  for i in range(len(reads1)):
    if i in used:
      continue

    for j in range(i,len(reads1)):
      if j in used:
        continue
      if ismatch(reads1[i][-length:], reads1[j][:length]) and ismatch(reads2[i][-length:], reads2[j][:length]):
        
        reads1[i] += reads1[j][length:]
        reads2[i] += reads2[j][length:]
        
        used.add(j)
      elif ismatch(reads1[j][-length:], reads1[i][:length]) and ismatch(reads2[j][-length:], reads2[i][:length]):
        print(reads1[i]+' '+reads1[j])
        reads1[i] =reads1[j][:-length] + reads1[i]
        reads2[i] =reads2[j][:-length] + reads2[i]
        print(reads1[i])
        used.add(j)
  # for i in range(len(reads1)):
  #   if i in used:
  #     continue

  #   for j in range(len(reads1)):
  #     if j in used or i==j:
  #       continue
  #     if(reads1[i] in reads1[j]) and (reads2[i] in reads2[j]):
  #       used.add(i)
  #       break
  #     if(reads1[j] in reads1[i]) and (reads2[j] in reads2[i]):
  #       used.add(j)

  new_reads1 = []
  new_reads2 = []

  for i in range(len(reads1)):
    if i not in used:
      new_reads1.append(reads1[i])
      new_reads2.append(reads2[i])
  return [new_reads1,new_reads2]

while length >15:
  [new_reads1,new_reads2] = connect(reads1, reads2)
  if len(reads1) == len(new_reads1):
    # break
    length -= 1
  print(len(reads1),len(new_reads1))
  reads1 = new_reads1
  reads2 = new_reads2

for i in range(len(reads1)):
    f.write(reads1[i][:21+10]+reads2[i]+'\n')
    # f.write(reads1[i]+" "+reads2[i]+'\n')
    # f.write(reads1[i]+'\n')
# print(reads1)


# AGATCCCGATCACCTATCCGATGG CCGATCACCTATCCGATGGACACCG
# AACAAAAAAGGATTAAGTAGTGAAAGCCATTTTGAG ACTCAACAAAAAAGGATTAAGTA
# AAACAAAAAAGGATTAAGTAGTGAAAGCCATTTTGAG
