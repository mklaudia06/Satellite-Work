import flet as ft
from src.components import Components
from src.funcs import readJson


def main(page: ft.Page):
    comps = Components()
    mainData = readJson("./utils/quiz.json")
    textData = readJson("./utils/text.json")
    print(page.route)

    def route_change(e: ft.RouteChangeEvent):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    ft.AppBar(title=ft.Text("SatelliteQuiz"), bgcolor=ft.Colors.BLACK45),
                    ft.SafeArea(
                        ft.Column(
                            [   
                                ft.Image(src="https://media.istockphoto.com/id/466727938/photo/communication-satellite-orbiting-earth.jpg?s=612x612&w=0&k=20&c=dQN649CS_VGkqUmutFNhRmltil9uHFvDIZR3ttkeHtc="),
                                ft.Text("Veamos cuanto sabes acerca de los satélites😼", text_align="center", size=35),
                                ft.ResponsiveRow(
                                    [
                                        ft.ElevatedButton("Comenzar Quiz", on_click=lambda _: page.go("/question1")),
                                        ft.ElevatedButton("Acerca de...", on_click=lambda _: page.go("/about_us"))
                                    ]
                                )
                            ],
                            horizontal_alignment="center"
                    )
                    )
                ]
            )
        )
        counter = 0
        if page.route == f"/question{counter}":
            page.views.append(
                comps.createQuestionView(mainData[counter]["id"], mainData[counter]["question"], mainData[counter]["answers"], mainData[counter]["description"])
            )
            counter += 1
        
        elif page.route == "/about_us":
            page.views.append(
                ft.View(
                    "/about_us",
                    [
                        ft.AppBar(title=ft.Text("Acerca de")),
                        ft.Text(value=textData["about_us"])
                    ]
                )
            )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)
    
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

ft.app(main)