import flet as ft
from typing import List, Dict, Any

class Components:
    def __init__(self, page: ft.Page, main_data: List[Dict[str, Any]], text_data):
        self.text_align = "center"
        self.page = page
        self.main_data = main_data
        self.text_data = text_data
        self.question_count = len(main_data)

    def buttonContinueOrFinish(self, question_number: int):
        if question_number < 20:
            return ft.ElevatedButton("Siguiente Pregunta", on_click=lambda _: self.page.go(f"/question{question_number + 1}"))
        return ft.ElevatedButton("Finish", on_click=lambda _: self.page.go("/results"))
    
    def displayAnswers(self, answers: List[Dict[str, bool]]):
        radios = []
        for all_answers in answers:
            radios.append(ft.Radio(label=all_answers["text"]))
        
        return radios
    
    def createHomeView(self):
        return ft.View(
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
                                    ft.ElevatedButton("Comenzar Quiz", on_click=lambda _: self.page.go("/question1")),
                                    ft.ElevatedButton("Acerca de...", on_click=lambda _: self.page.go("/about_us"))
                                ]
                            )
                        ],
                        horizontal_alignment="center"
                )
                )
            ]
        )
    
    def createAboutUsView(self):
        return ft.View(
            "/about_us",
            [
                ft.AppBar(title=ft.Text("Acerca de")),
                ft.Text(value=self.text_data["about_us"])
            ]
        )
    
    def createNotFoundView(self):
        return ft.View(
            "/not_found",
            [
                ft.AppBar(title=ft.Text("404 - No encontrado")),
                ft.Text("La página que buscas no existe.")
            ]
        )
    
    def createResultsView(self):
        return ft.View(
            "/results",
            [
                ft.AppBar(title=ft.Text("Resultados del Quiz"), center_title=True),
                ft.Text("¡Aquí mostrarías la puntuación final!"), # Reemplaza con la lógica de puntuación
            ]
        )

    def createQuestionView(self, question_number: int):
        question_data = self.main_data[question_number - 1]
        return ft.View(
            f"/question{question_number}",
            [
                ft.AppBar(title=ft.Text(value=f"Pregunta #{question_number}"), center_title=True),
                ft.Column(
                    [
                        ft.Text(value=question_data["question"], text_align=self.text_align),
                        ft.RadioGroup(
                            content=ft.Column(self.displayAnswers(question_data["answers"]))
                        ),
                        self.buttonContinueOrFinish(question_number)
                    ], 
                    horizontal_alignment=self.text_align
                )
            ],
            horizontal_alignment=self.text_align
        )
    
    def route_change(self, e: ft.RouteChangeEvent):
        self.page.views.clear()
        self.page.views.append(self.createHomeView())  
        if self.page.route.startswith("/question"): 
            try:
                question_number = int(self.page.route[9:]) 
                if 1 <= question_number <= self.question_count:
                    self.page.views.append(self.createQuestionView(question_number))
                else:
                    self.page.views.append(self.createNotFoundView()) # Manejo de error para preguntas fuera de rango
            except ValueError:
                self.page.views.append(self.createNotFoundView())  

        elif self.page.route == "/about_us":
            self.page.views.append(self.createAboutUsView())
        elif self.page.route == "/results":
             self.page.views.append(self.createResultsView())

        self.page.update()
