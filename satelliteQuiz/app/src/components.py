import flet as ft
from typing import List, Dict
import os

class Components:
    def __init__(self):
        self.text_align = "center"

    def continueOrFinish(self, questionNumber: int):
        if questionNumber < 20:
            return ft.ElevatedButton("Continue", on_click=lambda _: print("XD"))
        return ft.ElevatedButton("Finish", on_click=lambda _: print("XD2"))
    
    def displayAnswers(self, answers: List[Dict[str, bool]]):
        radios = []
        for all_answers in answers:
            radios.append(ft.Radio(label=all_answers["text"], value=all_answers["correct"]))
        
        return radios
    
    def createQuestionView(self, questionNumber: int, question: str, answers: List[Dict[str, bool]], description: str):
        return ft.View(
            f"/question{questionNumber}",
            [
                ft.AppBar(title=ft.Text(value=f"Pregunta #{questionNumber}"), center_title=True),
                ft.Column(
                    [
                        ft.Text(value=question, text_align=self.text_align),
                        ft.RadioGroup(
                            content=ft.Column(self.displayAnswers(answers))
                        ),
                        self.continueOrFinish(questionNumber)
                    ], 
                    horizontal_alignment=self.text_align
                )
            ],
            horizontal_alignment=self.text_align
        )