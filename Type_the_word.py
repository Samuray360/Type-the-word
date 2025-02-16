import random
import flet as ft
repeted = False 
user_word = ft.TextField(label="write the word")
stored_words = [
    "Lantern", "Glacier", "Serendipity", "Tapestry", "Nebula", "Wanderlust", 
    "Harmonize", "Ember", "Cascade", "Quixotic", "Vortex", "Jubilant", 
    "Monolith", "Obsidian", "Reverie", "Echo", "Prism", "Mirage", "Enigma", 
    "Saffron", "Wistful", "Crescent", "Twilight", "Solitude", "Whisper", 
    "Aurora", "Labyrinth", "Ephemeral", "Euphoria", "Odyssey"]

used_words=[]

while repeted == False:
    word = random.choice(stored_words)
    if word in used_words: 
        repeted == True

def main(page: ft.Page):


    page.bgcolor = "white"
    page.window.height = 600
    page.window.width = 600
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

# def word_comparetor():


    
    