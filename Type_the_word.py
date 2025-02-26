import random
import flet as ft

def main(page: ft.Page):
    page.bgcolor = "black"
    page.window.height = 600
    page.window.width = 600
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    match_label = ft.Text("Match", color="green", height=200, visible=False)
    mismatch_label = ft.Text("Don't match", color="red", height=200, visible=False)
    user_word = ft.TextField(label="Write the word", color="white")

    stored_words = [
        "Lantern", "Glacier", "Serendipity", "Tapestry", "Nebula", "Wanderlust", 
        "Harmonize", "Ember", "Cascade", "Quixotic", "Vortex", "Jubilant", 
        "Monolith", "Obsidian", "Reverie", "Echo", "Prism", "Mirage", "Enigma", 
        "Saffron", "Wistful", "Crescent", "Twilight", "Solitude", "Whisper", 
        "Aurora", "Labyrinth", "Ephemeral", "Euphoria", "Odyssey"
    ]

    selected_word = random.choice(stored_words)
    word_display = ft.Text(f"Selected Word: {selected_word}", color="white")

    def check_button_clicked(e):
        nonlocal selected_word  
        match_label.visible = False
        mismatch_label.visible = False

        if user_word.value.strip().lower() == selected_word.lower():  
            match_label.visible = True
        else:
            mismatch_label.visible = True

        selected_word = random.choice(stored_words)  
        word_display.value = f"Selected Word: {selected_word}"  
        page.update()  

    check_button = ft.ElevatedButton(text="Check", color="white", width=200, on_click=check_button_clicked)

    page.add(word_display, user_word, mismatch_label, match_label, check_button)

ft.app(target=main)
