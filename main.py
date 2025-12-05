
import flet as ft
from datetime import datetime

def main(page: ft.Page):
    page.title = 'My first app' #встроенный параметр
    page.theme_mode = ft.ThemeMode.DARK
    greeting_text = ft.Text(value='Hello world')
    
    greeting_history = []
    history_text = ft.Text("История приветствий:")

    favorite_names = []
    favorites_text = ft.Text("Любимые имена:")

    # greeting_text.value = 'Привет'
    # greeting_text.color = ft.Colors.GREEN

    def on_button_click(_):
    # print(name_input.value)
        name = name_input.value.strip()
        timestamp = datetime.now().strftime("%y:%m:%d - %H:%M:%S")

        if name:
            greeting_text.value = f'{timestamp} Hello {name}'
            greeting_text.color = None
            name_input.value = None
        
            greeting_history.append(f"{timestamp} Hello {name}")
            print(greeting_history)
            history_text.value = "История приветствий:\n" + '\n'.join(greeting_history)        
        else:
            greeting_text.value = 'Введите корректное имя'
            greeting_text.color = ft.Colors.RED

            page.update()

    name_input = ft.TextField(label='Введите имя', on_submit=on_button_click, expand=True)
    button_text = ft.TextButton(text='send', on_click=on_button_click)
    button_elevated = ft.ElevatedButton(text='send', on_click=on_button_click)
    button_icon = ft.IconButton(icon=ft.Icons.SEND, on_click=on_button_click)
    fav_icon = ft.IconButton(icon=ft.Icons.STAR, icon_color="yellow", icon_size=30)
 
    def clear_history(_):
        print(greeting_history)
        greeting_history.clear()
        history_text.value = 'История приветствий:'
        page.update()
        print(greeting_history)
    
    def add_to_favorites(_):
        if greeting_history:
            last_greeting = greeting_history[-1]
        if "Hello " in last_greeting:
            name = last_greeting.split("Hello ")[1].strip()
            if name and name not in favorite_names:
                favorite_names.append(name)
                favorites_text.value = "Любимые имена:\n" + "\n".join(favorite_names)
                page.update()


    add_fav_button = ft.ElevatedButton(text='Добавить в избранное', on_click=add_to_favorites)
    fav_icon = ft.IconButton(icon=ft.Icons.STAR, icon_color="yellow", icon_size=30)
    clear_button = ft.IconButton(icon=ft.Icons.DELETE, on_click=clear_history)
    
    view_greeting_text = ft.Row([greeting_text], alignment=ft.MainAxisAlignment.CENTER)

    page.add(view_greeting_text, ft.Row([name_input, button_elevated, clear_button, add_fav_button]), history_text, favorites_text)

ft.app(target=main)

# alignment=ft.MainAxisAlignment.SPACE_EVENLY
