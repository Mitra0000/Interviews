def edit_distance(word1, word2):
  table = setup_table(word1, word2)
  for row in range(1, len(word1) + 1):
    for col in range(1, len(word2) + 1):
      table[row][col] = min(
        table[row - 1][col] + 1, 
        table[row][col - 1] + 1, 
        table[row - 1][col - 1] + 
          (1 if word1[row - 1] != word2[col - 1] else 0))
  return table[-1][-1]

def setup_table(word1, word2):
  table = []
  # Create a table of size |word1| rows x |word2| columns.
  for i in range(len(word1) + 1):
    table.append([])
    for j in range(len(word2) + 1):
      table[i].append(float('inf'))

  # Populate the first row with ascending numbers.
  table[0] = list(range(len(word2) + 1))
  # Populate the first column with ascending numbers.
  for i in range(len(table)):
    table[i][0] = i
  return table
  
if __name__ == "__main__":
  word1 = input("Enter first word: ")
  word2 = input("Enter second word: ")
  print(edit_distance(word1, word2))
