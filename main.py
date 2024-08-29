import sys

def main():
  text = getBookText("books/frankenstein.txt")
  wordCount = getWordCount(text)
  letterCount = getLetterCount(text)

  letterCtList = dictToList(letterCount)
  letterCtList.sort(reverse = True, key = sort_on)

  print("--- Begin report of books/frankenstein.txt ---")
  print(f'{wordCount} words found in the document')
  print("")

  for item in letterCtList:
    print(f"The '{item['name']}' character was found {item['num']} times")

  print("--- End report ---")

def getBookText(path):
   with open(path) as f:
      file_contents = f.read()

   return(file_contents)

def getWordCount(text):
   return(len(text.split()))

def getLetterCount(text):
  letterDict = {}
   
  for char in text.lower():
    if char in letterDict:
      letterDict[char] += 1
    else:
      letterDict[char] = 1
    
  return(letterDict)

def dictToList(dict):
  return([{'name':k, 'num':v} for k, v in dict.items() if k.isalpha()])

def sort_on(dict):
  return(dict["num"])
  
if __name__ == "__main__":
  sys.exit(main())
