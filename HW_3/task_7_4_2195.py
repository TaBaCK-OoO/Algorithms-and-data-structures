import sys
import re





def main():
    with open("input_2", "r", encoding="utf-8") as f:
        input_data = f.read().splitlines()
    if not input_data:
        return

    iterator = iter(input_data)

    first_line = next(iterator).split()
    while not first_line:
        first_line = next(iterator).split()

    N = int(first_line[0])
    M = int(first_line[1])

    vocabulary = set()
    for _ in range(N):
        word = next(iterator).strip().lower()
        if word:
            vocabulary.add(word)

    text_lines = []
    for _ in range(M):
        try:
            text_lines.append(next(iterator))
        except StopIteration:
            break

    text = " ".join(text_lines)
    words_in_text = re.findall(r'[a-zA-Z]+', text)
    text_words = set(word.lower() for word in words_in_text)
    unknown_words = text_words - vocabulary
    unused_words = vocabulary - text_words

    if unknown_words:
        print("Some words from the text are unknown.")
    elif unused_words:
        print("The usage of the vocabulary is not perfect.")
    else:
        print("Everything is going to be OK.")


if __name__ == '__main__':
    main()