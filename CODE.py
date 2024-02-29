# English-Dictionary-App
English Dictionary App
#Function to read dictionary from a file
def read_dictionary(filename):
    dictionary={}
    try:
        with open(filename,'r')as file:
            for line in file:
                word,meaning=line.strip().split(':')
                dictionary[word.strip()]=meaning.strip()
        print("Dictionary loaded successfully")    
    except FileNotFoundError:
        print("Dictionary file not found")
    return dictionary

#Function to add words into dictionary
def add_word(dictionary,word,meaning):
    dictionary[word]=meaning
    
#Function to search for a word
def search_word(dictionary,word):
    return dictionary.get(word,'Word not found')
    
#Function to save dictionary
def save_dictionary(dictionary,filename):
    with open(filename,'w') as file:
        for word,meaning in dictionary.items():
            file.write(f"{word}:{meaning}\n")
    print("Dictionary saved successfully")        
    
    
#Main Function 
def main():
    dictionary_file="skill lync.txt"
    english_dict=read_dictionary(dictionary_file)
    
    while True:
        print("\n Options")
        print("1.Add word")
        print("2.Search for a word")
        print("3.Save dictionary and exit")
        choice=input("Enter a choice (1/2/3):")
        
        if choice=="1":
            word_to_add=input("Enter a word")
            meaning_to_add=input("Enter the meaning")
            add_word(english_dict,word_to_add,meaning_to_add)
            print("Word added successfully")
            
        elif choice=='2':
            word_to_search=input("Enter the word to search:")
            result=search_word(english_dict,word_to_search)
            print(result)
            
        elif choice=='3':
            save_dictionary(english_dict,dictionary_file)
            break
                
        else:
            print("Invalid choice. Please choose 1,2 or 3:")
            
main()
