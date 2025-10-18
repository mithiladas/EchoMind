import pygame
import random
import time

# start pygame
pygame.init()

# save sound files
sounds = {
    "bell": pygame.mixer.Sound("bell.wav"),
    "clap": pygame.mixer.Sound("clap.wav"),
    "whistle": pygame.mixer.Sound("whistle.wav"),
    "drum": pygame.mixer.Sound("drum.wav")
}

# start game
print("Welcome to the Sound Memory Game!")
print("Listen carefully and repeat the sounds in order.\n")

sound_names = list(sounds.keys())
level = 1

while True:
    print(f"--- Level {level} ---")
    
    # random sound sequence
    sequence = random.choices(sound_names, k=level)
    
    # play sound
    for s in sequence:
        sounds[s].play()
        time.sleep(1)  # 1 sec break
    
    time.sleep(0.5)
    
    # user input
    user_input = input("Enter the sound names separated by space: ").split()
    
    if user_input == sequence:
        print("✅ Correct! Moving to next level.\n")
        level += 1
    else:
        print("❌ Wrong sequence! Game Over.")
        print(f"The correct sequence was: {sequence}")
        break

pygame.quit()

