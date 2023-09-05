#get all texts from the story.txt
with open("story.txt", "r") as f:
    story = f.read()

#create container to store the words
words = set()
#set the "start_of_word" initially to -1, so we can check if this stay -1, means did not move, did not found the location of bracket
start_of_word = -1

#targeting the words location
target_start = "<"
target_end = ">"

#loop the angle bracket < >  
for i, char in enumerate(story):
    #if found the opening of the bracket "<", means that found the beinning of the word
    if char == target_start:
        #now change the value of "start_of_word "
        start_of_word = i

    # "start_of_word" not equal to -1 means the beginning of the bracket found
    if char == target_end and start_of_word != -1:
        # then we can take the entire word, and add that to the words list
        word = story[start_of_word: i + 1 ]
        words.add(word)
        start_of_word = -1

answers = {}

for word in words:
    answer = input("Enter a word for " + word + ": ")
    answers[word] = answer

for word in words:
    story = story.replace(word, answers[word])

print(story)


