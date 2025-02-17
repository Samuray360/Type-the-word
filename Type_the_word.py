import random
import flet as ft
repeted = False 
user_word = ft.TextField(label="write the word" ,color="white")
match_label = ft.Text("Match",color="green",visible=False)
dont_match_label=ft.Text("Don't match",color="red",visible=False)
  
stored_words = [
    "Lantern", "Glacier", "Serendipity", "Tapestry", "Nebula", "Wanderlust", 
    "Harmonize", "Ember", "Cascade", "Quixotic", "Vortex", "Jubilant", 
    "Monolith", "Obsidian", "Reverie", "Echo", "Prism", "Mirage", "Enigma", 
    "Saffron", "Wistful", "Crescent", "Twilight", "Solitude", "Whisper", 
    "Aurora", "Labyrinth", "Ephemeral", "Euphoria", "Odyssey"]
used_words=[]
word = random.choice(stored_words)
while repeted == True:   
    match_label = visible=False
    dont_match_label= visible=False
    if word in used_words: 
            repeted == False    
    else:
         repeted=True

def check_button_clicked():
    if word_display==user_word :
        match_label.visible=True
    if word_display !=user_word :
        dont_match_label.visible=True
    else:
         match_label.visible=False
         dont_match_label.visible=False

word_display = ft.Text(f"Selected Word: {word}")
def main(page: ft.Page):

    page.bgcolor = "navy"
    page.window.height = 600
    page.window.width = 600
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.add( word_display,user_word,ft.ElevatedButton(text="check", color="white", width=200, on_click=check_button_clicked))

    
ft.app(main)   
