MAX_ERR = 1

# reference = "TTTAGCGAACCCAAGCGGCAGGGGTCGCGGCACGGCGAACTAAAACGTCCCCGGCAGGTCGTGTATACATGTTTGTGCTCAACATTCAGAGTCCTCCTTTGCGTGCCCGGGTAGCGTCTAGGCGCCGACGATCGACCAGCGGGGCTATTCGGGCCCCTCCCTCGCCACCTGACAGCTCTC"
reference = "hello"
suffix = range(len(reference))
suffix = sorted(suffix, key=lambda x: reference[x:]) 

def get_ref(idx):
  if idx < len(reference):
    return reference[idx]
  return chr(255)

def exact_match(l,r,st,key):
  if r<l:
    return -1
  m = (l+r)//2
  # print(m)
  current = reference[suffix[m]:]
  current = current[st : min(st+len(key),len(current))]
  # print(l,r,m)
  print(current,key[st:])
  if current == key[st:]:
    return m
  if current[st:st+len(key)] < key[st:]:
    return exact_match(m+1, r, st, key)
  return exact_match(l, m-1, st, key)

def match(l,r,st,key,error):
  
  if error > MAX_ERR:
    return [1e9,-1]

  if st>=len(reference):
    return [1e9,-1]
  
  if r<l:
    return [1e9,-1]

  print()
  print("match")
  print(l,r,st,error)
  print()
  suffix_pos = exact_match(l, r, 0, key[st:])


  if suffix_pos != -1:
    match_pos = suffix[suffix_pos]
    # print("here",suffix_pos,match_pos)
    return [error,match_pos]
  

  i = l
  
  print(l,r,st)
  while(i<=r and get_ref(suffix[i]+st) != key[st] ):
    i+=1
  j = i
  while(j<=r and get_ref(suffix[j]+st) == key[st]):
    j+=1

  
  print(l,i,j,r)
  a = match(l,i-1,st+1,key,error+1)
  b = match(i,j-1,st+1,key,error)
  c = match(j,r,st+1,key,error+1)

  return min(a,b,c)

x = "elo"

[error,match_pos] = match(0,len(suffix)-1,0,x,0) 

print("error: "+str(error))
print("match pos: "+str(match_pos))

print(suffix)

