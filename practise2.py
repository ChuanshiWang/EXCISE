# enumerate() method:
str1 = "Howl's Moving Castle"

for index, character in enumerate(str1):
    print(f"Index: {index}, Character: {character}")
    # join() method:
    some_list = ['Baa', 'baa', 'black', 'sheep']

    # Joining list elements into a single string separated by spaces
    joined_string = ' '.join(some_list)
    print(joined_string)
    # random() method:
    import random

    some_list = ['Baa', 'baa', 'black', 'sheep']

    # Picking a random item from the list
    random_item = random.choice(some_list)
    print(random_item)