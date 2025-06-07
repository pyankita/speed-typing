import time
import random


sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Typing fast and accurately takes a lot of practice.",
    "Python is a versatile and powerful programming language.",
    "Focus on accuracy before increasing your typing speed.",
    "Always test your code after every major change."
]

def typing_test():
    sentence = random.choice(sentences)
    print("Type the following sentence:\n")
    print(sentence)
    input("Press Enter when you are ready to start...")

    start_time = time.time()
    typed = input("\nStart typing here:\n")
    end_time = time.time()

    # Calculate typing speed
    total_time = end_time - start_time
    time_in_minutes = total_time / 60
    word_count = len(typed.split())
    wpm = word_count / time_in_minutes

    # Calculate accuracy
    correct_chars = 0
    for i in range(min(len(typed), len(sentence))):
        if typed[i] == sentence[i]:
            correct_chars += 1
    accuracy = (correct_chars / len(sentence)) * 100

    print(" Time Taken: {:.2f} seconds".format(total_time))
    print(" Your Typing Speed: {:.2f} WPM".format(wpm))
    print(" Accuracy: {:.2f}%".format(accuracy))


typing_test()
