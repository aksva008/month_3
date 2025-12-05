
import flet as ft
from datetime import datetime

def main(page: ft.Page):
    page.title = 'My first app' #встроенный параметр
    page.theme_mode = ft.ThemeMode.DARK
   
    greeting_text = ft.Text(value='Hello world')
    

    def on_button_click(_):
        name = name_input.value.strip()
        timestamp = datetime.now().strftime("%y:%m:%d - %H:%M:%S")

        if name:
            greeting_text.value = f'{timestamp} Hello {name}'
            greeting_text.color = None
            name_input.value = None
        else:
            greeting_text.value = 'Введите корректное имя'
            greeting_text.color = ft.Colors.RED

        page.update()
 
    def theme(_):
        if page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT
        else:
            page.theme_mode = ft.ThemeMode.DARK
        page.update()


    name_input = ft.TextField(label='Введите имя', on_submit=on_button_click, expand=True)
    button_elevated = ft.ElevatedButton(text='Send', on_click=on_button_click)
    theme_button = ft.ElevatedButton(text='Сменить тему', on_click=theme)

    view_greeting_text = ft.Row([greeting_text], alignment=ft.MainAxisAlignment.CENTER)

    page.add(view_greeting_text, ft.Row([name_input, button_elevated, theme_button]))

       



ft.app(target=main)

# alignment=ft.MainAxisAlignment.SPACE_EVENLY
