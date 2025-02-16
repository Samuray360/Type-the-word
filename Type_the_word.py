import random
import flet as ft
repeted = False 
user_word = ft.TextField(label="write the word")
while repeted == False:
        
       
    stored_words = [
    "Lantern", "Glacier", "Serendipity", "Tapestry", "Nebula", "Wanderlust", 
    "Harmonize", "Ember", "Cascade", "Quixotic", "Vortex", "Jubilant", 
    "Monolith", "Obsidian", "Reverie", "Echo", "Prism", "Mirage", "Enigma", 
    "Saffron", "Wistful", "Crescent", "Twilight", "Solitude", "Whisper", 
    "Aurora", "Labyrinth", "Ephemeral", "Euphoria", "Odyssey"]
    used_words=[]
    word = random.choice(stored_words)
    word_display = ft.Text(f"Selected Word: {word}")

    if word in used_words: 
            repeted == True

def main(page: ft.Page):

    page.bgcolor = "white"
    page.window.height = 600
    page.window.width = 600
    page.add( word_display,user_word)
    
ft.app(main)   
# def check_button():
#     if word_display ==user_word :
        # text.visibility_turn_on match

        # else:
         
        # text.visiblitity_ turn_on dont match