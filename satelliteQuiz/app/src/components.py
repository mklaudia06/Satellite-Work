import flet as ft
from typing import List, Dict, Any, Callable
from .funcs import createUserJson, updateJson, readJson
import random
import os

class Components:
    def __init__(self, page: ft.Page, main_data: List[Dict[str, str|int]], text_data: Dict[str, str]):
        self.text_align = ft.TextAlign.CENTER
        self.alignment = ft.CrossAxisAlignment.CENTER
        self.page = page
        self.main_data = main_data
        self.text_data = text_data
        self.question_count = len(main_data)
        self.radio_group = None
        self.info_dlg = None
        self.correct_answers_responses = ["Exacto", "Asi es", "Perfecto", "Eres un/a crack"]
        self.incorrect_answers_responses = ["Nope", "Casi, pero no", "No es correcto", "Hmmm, no lo creo"]

    def createDlg(self, title: str, content: str, question_number: int = None):
        def close_and_continue(e):
            self.page.close(self.info_dlg)
            if question_number < 20:
                self.page.go(f"/question{question_number + 1}")
            else:
                self.page.go("/results")

        self.info_dlg = ft.AlertDialog(
            modal=True,
            title=ft.Text(title),
            content=ft.Text(content),
            alignment=ft.alignment.center,
            actions=[
                ft.TextButton("Cerrar", on_click=close_and_continue)
            ]
        )

    def validateAnswers(self, question_number: int):
        question_data = self.main_data[question_number - 1] # No list index out of range
        try:
            if self.radio_group.value is not None:
                if self.radio_group.value == question_data["answers"][question_data["correct_answer"]]["text"].lower():
                    self.createDlg(
                        title=random.choice(self.correct_answers_responses),
                        content=question_data["description"],
                        question_number=question_number
                    )
                    updateJson("./user/userResults.json", question_data["points"])
                    self.page.open(self.info_dlg)
                else:
                    self.createDlg(
                        title=random.choice(self.incorrect_answers_responses),
                        content=question_data["description"],
                        question_number=question_number
                    )
                self.page.open(self.info_dlg)
            else:
                self.createDlg(
                    title=">:/",
                    content="No has marcado ninguna opcion, asegurate de marcar aunque sea una",
                )
                self.page.open(self.info_dlg)
        except Exception as e:
            print(e)

    def buttonContinueOrFinish(self, question_number: int):
        if question_number < 20:
            return ft.ElevatedButton("Siguiente Pregunta", on_click=lambda _: self.validateAnswers(question_number))
        return ft.ElevatedButton("Finish", on_click=lambda _: self.validateAnswers(question_number))
    
    def displayAnswers(self, answers: List[Dict[str, str]]):
        radios = []
        for all_answers in answers:
            radios.append(
                ft.Container(
                    ft.Radio(value=all_answers["text"].lower(), 
                             label=all_answers["text"],
                             label_style=ft.TextStyle(size=15)), 
                    expand=2,
                    )
                )
        
        return radios

    def start(self, e):
        createUserJson("./user/userResults.json")
        self.page.go("/question1")

    def createHomeView(self):
        return ft.View(
            "/",
            [
                ft.AppBar(title=ft.Text("SatelliteQuiz"), bgcolor=ft.Colors.BLACK45),
                ft.SafeArea(
                    ft.Column(
                        [   
                            ft.Image(src="https://media.istockphoto.com/id/466727938/photo/communication-satellite-orbiting-earth.jpg?s=612x612&w=0&k=20&c=dQN649CS_VGkqUmutFNhRmltil9uHFvDIZR3ttkeHtc="),
                            ft.Text("Veamos cuanto sabes acerca de los satélites😼", text_align=self.text_align, size=35),
                            ft.ResponsiveRow(
                                [
                                    ft.ElevatedButton("Comenzar Quiz", on_click=self.start),
                                    ft.ElevatedButton("Acerca de...", on_click=lambda _: self.page.go("/about_us"))
                                ]
                            )
                        ],
                        horizontal_alignment=self.alignment
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
    
    def finish(self, e):
        os.remove("./user/userResults.json")
        self.page.go("/")
    
    def createResultsView(self):
        result = readJson("./user/userResults.json")["points"]
        return ft.View(
            "/results",
            [
                ft.AppBar(title=ft.Text("Resultados del Quiz"), center_title=True),
                ft.Text(result),
                ft.ElevatedButton("Regresar al Menu Principal", on_click=self.finish)
            ]
        )

    def createQuestionView(self, question_number: int):
        question_data = self.main_data[question_number - 1] # No list index out of range
        self.radio_group = ft.RadioGroup(
                            content=ft.Column(self.displayAnswers(question_data["answers"]), tight=True),
                        )
        return ft.View(
            f"/question{question_number}",
            [
                ft.AppBar(title=ft.Text(value=f"Pregunta #{question_number}"), center_title=True),
                ft.ResponsiveRow(
                    [        
                        ft.Column(
                            [
                                ft.Text(value=question_data["question"], text_align=self.text_align),
                                self.radio_group,
                                self.buttonContinueOrFinish(question_number)
                            ], 
                            horizontal_alignment=self.alignment
                        )
                    ]
                )
            ],
            horizontal_alignment=self.alignment
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
                    self.page.views.append(self.createNotFoundView())
            except ValueError:
                self.page.views.append(self.createNotFoundView())  

        elif self.page.route == "/about_us":
            self.page.views.append(self.createAboutUsView())
        elif self.page.route == "/results":
             self.page.views.append(self.createResultsView())

        self.page.update()
