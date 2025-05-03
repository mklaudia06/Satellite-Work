import flet as ft
from src.components import Components
from src.funcs import readJson


def main(page: ft.Page):
    mainData = readJson("./utils/quiz.json")
    textData = readJson("./utils/text.json")
    comps = Components(page, mainData, textData)

    def route_change(e: ft.RouteChangeEvent):
        comps.route_change(e)

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)
    
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

ft.app(main)