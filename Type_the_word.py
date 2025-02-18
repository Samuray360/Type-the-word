import random
import flet as ft

def main(page: ft.Page):
    page.bgcolor = "navy"
    page.window.height = 600
    page.window.width = 600
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    stored_words = [
        "Lantern", "Glacier", "Serendipity", "Tapestry", "Nebula", "Wanderlust", 
        "Harmonize", "Ember", "Cascade", "Quixotic", "Vortex", "Jubilant", 
        "Monolith", "Obsidian", "Reverie", "Echo", "Prism", "Mirage", "Enigma", 
        "Saffron", "Wistful", "Crescent", "Twilight", "Solitude", "Whisper", 
        "Aurora", "Labyrinth", "Ephemeral", "Euphoria", "Odyssey"
    ]
    
    used_words = []
    word = random.choice(stored_words)
    used_words.append(word)

    word_display = ft.Text(f"Selected Word: {word}", color="white")
    user_word = ft.TextField(label="Write the word", color="white")

    match_label = ft.Text("Match", color="green", height=200, visible=False)
    missmatch_label = ft.Text("Don't match", color="red", height=200, visible=False)

    def check_button_clicked(e):
        match_label.visible = False
        missmatch_label.visible = False

        if user_word.value == word:
            match_label.visible = True  
        else:
            missmatch_label.visible = True 

        match_label.update()
        missmatch_label.update()

    check_button = ft.ElevatedButton(text="Check", color="white", width=200, on_click=check_button_clicked)

    page.add(word_display, user_word, missmatch_label, match_label, check_button)

ft.app(target=main)
