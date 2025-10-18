import pygame
import random
import time

# pygame শুরু করা
pygame.init()

# সাউন্ড ফাইল লোড করা
sounds = {
    "bell": pygame.mixer.Sound("bell.wav"),
    "clap": pygame.mixer.Sound("clap.wav"),
    "whistle": pygame.mixer.Sound("whistle.wav"),
    "drum": pygame.mixer.Sound("drum.wav")
}

# গেম শুরু
print("Welcome to the Sound Memory Game!")
print("Listen carefully and repeat the sounds in order.\n")

sound_names = list(sounds.keys())
level = 1

while True:
    print(f"--- Level {level} ---")
    
    # র‍্যান্ডম সাউন্ড সিকোয়েন্স তৈরি
    sequence = random.choices(sound_names, k=level)
    
    # সাউন্ডগুলো বাজানো
    for s in sequence:
        sounds[s].play()
        time.sleep(1)  # ১ সেকেন্ড বিরতি
    
    time.sleep(0.5)
    
    # ইউজারের ইনপুট নেওয়া
    user_input = input("Enter the sound names separated by space: ").split()
    
    if user_input == sequence:
        print("✅ Correct! Moving to next level.\n")
        level += 1
    else:
        print("❌ Wrong sequence! Game Over.")
        print(f"The correct sequence was: {sequence}")
        break

pygame.quit()
