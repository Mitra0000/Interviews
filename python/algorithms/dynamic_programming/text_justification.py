class TextJustifier:
  def __init__(self, lineWidth):
    self.__lineWidth = lineWidth

  def justifyText(self, text):
    self.__memo = {}
    self.__justify(0, text)
    # Construct the breaks from the __memo here
    lines = []
    pos = 0
    while pos < len(text) and pos in self.__memo:
      lines.append(text[pos:self.__memo[pos][1]+1])
      pos = self.__memo[pos][1]
    return "\n".join(lines)
    

  """
  Calculate the badness of a line starting at i and finishing at j.
  j must be greater or equal to i.
  """
  def __badness(self, i, j, text):
    if text[j] != " " and j != len(text) - 1:
      return float('inf')
    if (j - i) > self.__lineWidth:
      return float('inf')
    return (self.__lineWidth - (j - i))
  
  """
  Calculates total badness for text.
  """
  def __justify(self, i, text):
    if i not in self.__memo:
      if (i == len(text) - 1):
        return 0
      self.__memo[i] = min([
          (self.__badness(i, j, text) + self.__justify(j, text), j)
          for j in range(i + 1,
                         len(text))
      ])
    
    return self.__memo[i][0]

if __name__ == '__main__':
  # Create a new TextJustifier with line width 15
  justifier = TextJustifier(15)
  text = "This is a long piece of text that requires justifying as it is too big."
  print(justifier.justifyText(text))
