def word_search(word,f, line =1):
    currline = f.readline()
    if not currline:
        return -1
    if word in currline:
        return line
    return word_search(word, f, line+1)

with open("sample.txt", "r") as f:
    
    word = input("Enter the word you want to search for: ")
    result = word_search(word, f)
    if result == -1:
        print("Word not found")
    else:
        print(f"Word found at line {result}")
    
            