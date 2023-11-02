class DictionaryApp:
    def __init__(self):
        self.dictionary = {}

    def create_dictionary(self):
        filename = "dictionary.txt"
        try:
            with open(filename, "w") as file:
                for word, meaning in self.dictionary.items():
                    file.write(f"{word}: {meaning}\n")
            print("Dictionary has been generated successfully.")
        except IOError:
            print("Error: Unable to generate the dictionary file.")

    def insert_word_meaning(self):
        word = input("Enter a word: ")
        if word in self.dictionary :
            print("Word already present in the dictionary.\nTry again with another word!")
            return
        meaning = input(f"Enter the meaning of '{word}': ")
        self.dictionary[word] = meaning
        print(f"'{word}' added to the dictionary.")

    def search_word_meaning(self):
        word = input("Enter a word to search: ")
        meaning = self.dictionary.get(word, "Word not found in the dictionary.")
        print(f"The meaning of '{word}'' is : '{meaning}'")

    def delete_word(self):
        word = input("Enter a word to delete: ")
        if word in self.dictionary:
            del self.dictionary[word]
            print(f"'{word}' deleted from the dictionary.")
        else:
            print(f"'{word}' not found in the dictionary.")

    def menu(self):
        while True:
            print("\nDictionary Application Menu:")
            print("1. Generate Dictionary")
            print("2. Insert New Word-Meaning")
            print("3. Search for a Word-Meaning")
            print("4. Delete a Word")
            print("5. Exit Application")
            choice = input("Enter the function you wish to perform (1/2/3/4/5): ")

            if choice == "1":
                self.create_dictionary()
            elif choice == "2":
                self.insert_word_meaning()
            elif choice == "3":
                self.search_word_meaning()
            elif choice == "4":
                self.delete_word()
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    tool = DictionaryApp()
    tool.menu()
