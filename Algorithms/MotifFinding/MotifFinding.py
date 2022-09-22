import random

MOTIF_LENGTH = 10

def getProfile(motifs):
  n = (4 + len(motifs))
  A = [1 / n] * MOTIF_LENGTH
  T = [1 / n] * MOTIF_LENGTH
  C = [1 / n] * MOTIF_LENGTH
  G = [1 / n] * MOTIF_LENGTH
  for motif in motifs:
    for i in range(MOTIF_LENGTH):
      if motif[i] == 'a':
        A[i] += 1 / n
      elif motif[i] == 't':
        T[i] += 1 / n
      elif motif[i] == 'c':
        C[i] += 1 / n
      else:
        G[i] += 1 / n
  return (A, T, C, G)

def findProb(profile, motif):
  (A, T, C, G) = profile
  prob = 1
  for i in range(MOTIF_LENGTH):
    if motif[i] == 'a':
      prob *= A[i]
    elif motif[i] == 't':
      prob *= T[i]
    elif motif[i] == 'c':
      prob *= C[i]
    else:
      prob *= G[i]
  return prob

def getMotifs(profile, dnas):
  motifs = []
  for dna in dnas:
    motif = getMotif(profile, dna)
    motifs.append(motif)
  return motifs

def getMotif(profile, dna):
  maxProb = -1
  bestMotif = ""
  for i in range(len(dna) - MOTIF_LENGTH + 1):
    prob = findProb(profile, dna[i:i + MOTIF_LENGTH])
    if prob > maxProb:
      bestMotif = dna[i:i + MOTIF_LENGTH]
      maxProb = prob
  return bestMotif

def getConsensus(profile):
  (A, T, C, G) = profile
  result = ""
  for i in range(MOTIF_LENGTH):
    if A[i] == max(A[i], T[i], C[i], G[i]):
      result += 'a'
    elif T[i] == max(A[i], T[i], C[i], G[i]):
      result += 't'
    elif C[i] == max(A[i], T[i], C[i], G[i]):
      result += 'c'
    else:
      result += 'g'
  return result

def getRandomMotifs(dnas):
  motifs = []
  for dna in dnas:
    st = random.randint(0, len(dna) - MOTIF_LENGTH)
    motifs.append(dna[st:st + MOTIF_LENGTH])
  return motifs

def getScore(motifs, profile):
  score = 0
  consensus = getConsensus(profile)
  for motif in motifs:
    for i in range(MOTIF_LENGTH):
      if (motif[i] != consensus[i]):
        score += 1
  return score


def getBestMotifs(dnas):
  motifs = getRandomMotifs(dnas)
  profile = getProfile(motifs)
  bestMotifs = motifs
  minScore = getScore(motifs, profile)

  while (True):
    profile = getProfile(motifs)
    motifs = getMotifs(profile, dnas)
    newScore = getScore(motifs, profile)
    if newScore < minScore:
      bestMotifs = motifs
      minScore = newScore
    else:
      break
  return (minScore, bestMotifs)


f = open("Algorithms/MotifFinding/sequences.fastq", "r")
dnas = [s for s in f.read().split('\n') if len(s) > 0 and s[0] != '>']
minScore = 1e9
bestMotifs = ''

for i in range(100):
  (score, motifs) = getBestMotifs(dnas)
  if (score < minScore):
    minScore = score
    bestMotifs = motifs

profile = getProfile(bestMotifs)

print(getConsensus(profile))
