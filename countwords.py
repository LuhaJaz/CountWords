introString=input("Enter your Introduction")
CharacterCount= 0
WordCount= 1
for i in introString:
        CharacterCount= CharacterCount+1
        print(CharacterCount)
        if(i==""):
            WordCount= WordCount+1
print("Number of Word in the strings")
print(WordCount)            
print("Number of characters in the string")
print(CharacterCount)