import random
import flet as ft
repeted = False 

stored_words = [
    "Lantern", "Glacier", "Serendipity", "Tapestry", "Nebula", "Wanderlust", 
    "Harmonize", "Ember", "Cascade", "Quixotic", "Vortex", "Jubilant", 
    "Monolith", "Obsidian", "Reverie", "Echo", "Prism", "Mirage", "Enigma", 
    "Saffron", "Wistful", "Crescent", "Twilight", "Solitude", "Whisper", 
    "Aurora", "Labyrinth", "Ephemeral", "Euphoria", "Odyssey"]

used_words=[]

while repeted == False:
    word = random.choice(stored_words)
    user_word = input()
    if word in used_words: 
        repeted == True
    

# def word_comparetor():
    
    