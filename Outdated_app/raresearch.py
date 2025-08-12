import os
import re

rare_words = ['кустарное', 'заурядное', 'солидное', 'экспериментальное', 'немыслимое', 'каноническое', 'прорывное']

def find_rare_words(directory):
    rare_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    content = f.read().lower()
                    for rare_word in rare_words:
                        if re.search(rare_word.lower(), content):
                            rare_files.append((file, rare_word))
                            break
    return rare_files

rare_files = find_rare_words('.')
for file, rare_word in rare_files:
    print(f"File: {file}, Rare word: {rare_word}")

rare_counts = {}
for file, rare_word in rare_files:
    if rare_word not in rare_counts:
        rare_counts[rare_word] = 0
    rare_counts[rare_word] += 1

print("\nRare word counts:")
for rare_word, count in rare_counts.items():
    print(f"{rare_word}: {count}")
