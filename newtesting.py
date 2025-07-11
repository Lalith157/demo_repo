import os
import sys

app=Flask(__name__):

def read_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
    return content.splitlines

def count_words(lines):
    word_count = 0
    for line in lines:
        words = line.strip().split(" ")
        word_count += len(words)
    return word_count

def main():
    filename = sys.argv[1]
    if not os.path.exists(filename):
        print("File not found", filename)
        exit
    data = read_file(filename)
    count = count_words(data)
    print("Total words in file is: " + count)

main()
