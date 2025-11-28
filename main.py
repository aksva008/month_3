
import flet as ft

def main(page: ft.Page):
    page.title = 'My first app' #встроенный параметр
    greeting_text = ft.Text(value='Hello world', color=ft.Colors.RED)
    
    greeting_text.value = 'Hi'
    greeting_text.color = ft.Colors.PINK_50


    page.add(greeting_text)

ft.app(target=main)