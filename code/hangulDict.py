
def decompose_hangul(syllable):
  "Decompose a Hangul Syllable into its jamo"
  SBase = 0xAC00
  LBase = 0x1100
  VBase = 0x1161
  TBase = 0x11A8
  Lcount = 19
  Vcount = 21
  Tcount = 28
  SIndex = ord(syllable) - SBase

  if SIndex < 0 or SIndex >= ( Lcount*Vcount*Tcount ):
    # Unicode value is not in the hangul range
    return None
  L = chr(LBase + SIndex//(Vcount*Tcount))
  V = chr(VBase + (SIndex%(Vcount*Tcount))//Tcount)
  T = SIndex % Tcount
  if T:
    T = chr( TBase + T -1 )
  else:
    T = None
  return L, V, T

def compose_hangul(L, V, T):
  syllable = chr(588*ord(L) + 28*ord(V) + ord(T) + 44032)
  return syllable

def create_hangul_dict():
  syllable_to_jamo = {}
  jamo_to_syllable = {}
  for code in range( 0xAC00, 0xD7A4 ):
    syllable = chr(code)
    jamo = decompose_hangul(syllable)
    syllable_to_jamo[syllable] = jamo
    jamo_to_syllable[jamo] = syllable
  return syllable_to_jamo, jamo_to_syllable

def retain_hangul_char(text):
  return ''.join([char for char in text if 0xAC00 <= ord(char) <= 0xD7A3 ])