def get_num_words(filepath):
    with open(filepath) as file:
        content = file.read()

    num_words = content.split()
    return len(num_words)

def get_num_characters(filepath):
    with open(filepath) as file:
        content = file.read().lower()

    char_count = {}

    for word in content.split():
        for c in word:
            if c.isalpha():
                if c in char_count:
                    # Counting the letter-amount
                    char_count[c] = char_count[c]+1
                else:
                    # Adding a new letter into the dictionary
                    char_count[c] = 1
    
    return char_count

def get_sorted_result(filepath):
    num_characters = get_num_characters(filepath)
    sorted_keys = sorted(num_characters, key=lambda key: num_characters[key], reverse=True)

    export = "\n".join(f"{key}: {num_characters[key]}" for key in sorted_keys)

    return export