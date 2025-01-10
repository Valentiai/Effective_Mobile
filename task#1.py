def is_isomorphic(s,t):
  if len(s)!=len(t):
    return False
  d_s = dict()
  d_t = dict()
  for i in range(len(s)):
    if (s[i] in d_s and d_s[s[i]]!=t[i]) or (t[i] in d_t and d_t[t[i]]!=s[i]):
      return False
    d_s[s[i]] = t[i]
    d_t[t[i]] = s[i]
  return True
