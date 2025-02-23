import string

def create_sample_file():
    print("'sample.txt' not found. Please enter text to create the file:")
    user_text = input("Enter your paragraph: ")
    with open("sample.txt", "w", encoding="utf-8") as file:
        file.write(user_text)

def read_file():
    with open("sample.txt", "r", encoding="utf-8") as file:
        return file.read()

def count_word_frequency(text):
    text = text.lower().translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    return word_counts

def save_report(total_words, common_words):
    with open("word_count_report.txt", "w", encoding="utf-8") as file:
        file.write("Word Count Report\n")
        file.write(f"Total Words: {total_words}\n")
        file.write("Top Words:\n")
        for word, count in common_words:
            file.write(f"{word} - {count}\n")

try:
    with open("sample.txt", "r", encoding="utf-8") as f:
        pass
except FileNotFoundError:
    create_sample_file()

text = read_file()
word_counts = count_word_frequency(text)
total_words = sum(word_counts.values())

try:
    top_n = int(input("Enter the number of top common words to display: "))
except ValueError:
    top_n = 5  
common_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:top_n]

print(f"Total words: {total_words}")
print("Top common words:")
for word, count in common_words:
    print(f"{word} - {count} times")

save_report(total_words, common_words)
print("Report saved as 'word_count_report.txt'.")
