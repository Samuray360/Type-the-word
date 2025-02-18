import random
import flet as ft
repeted = False 
user_word = ft.TextField(label="write the word" ,color="white")
match_label = ft.Text("Match",color="green",height=200,visible=False)
missmatch_label=ft.Text("Don't match",color="red",height=200,visible=False)
match_label=visible=False
missmatch_label=visible=False
stored_words = [
    "Lantern", "Glacier", "Serendipity", "Tapestry", "Nebula", "Wanderlust", 
    "Harmonize", "Ember", "Cascade", "Quixotic", "Vortex", "Jubilant", 
    "Monolith", "Obsidian", "Reverie", "Echo", "Prism", "Mirage", "Enigma", 
    "Saffron", "Wistful", "Crescent", "Twilight", "Solitude", "Whisper", 
    "Aurora", "Labyrinth", "Ephemeral", "Euphoria", "Odyssey"]
used_words=[]
word = random.choice([w for w in stored_words if w not in used_words])
used_words.append(word)

def check_button_clicked(e):
    match_label.visible = False
    missmatch_label.visible = False

    if user_word.value == word_display.value:

        match_label.visible = True  
    else:
        missmatch_label.visible= True 
        


word_display = ft.Text(f"Selected Word: {word}")
def main(page: ft.Page):

    page.bgcolor = "navy"
    page.window.height = 600
    page.window.width = 600
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.add( word_display,user_word,missmatch_label,match_label,ft.ElevatedButton(text="check", color="white", width=200, on_click=check_button_clicked))

    
ft.app(main)   
