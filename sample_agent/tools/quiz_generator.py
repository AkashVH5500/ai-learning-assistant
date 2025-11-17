# quiz_generator.py – improved quiz generator

import random

class QuizAgent:
    def __init__(self, memory_bank=None):
        self.memory_bank = memory_bank

    def generate_quiz(self, topic, n=5, difficulty="medium"):
        questions = []

        for i in range(n):
            q_text = self._generate_question_text(topic, difficulty)
            choices, answer = self._generate_choices_and_answer(q_text)
            
            questions.append({
                "id": f"q{i}",
                "topic": topic,
                "difficulty": difficulty,
                "question": q_text,
                "choices": choices,
                "answer": answer,
                "explanation": f"The correct answer is {answer} because this follows from the concept of {topic}."
            })

        return {
            "questions": questions,
            "meta": {
                "topic": topic,
                "difficulty": difficulty,
                "count": n
            }
        }

    # ---------------------------
    # Question generation logic
    # ---------------------------
    def _generate_question_text(self, topic, difficulty):
        templates = {
            "easy": [
                f"What is the basic idea of {topic}?",
                f"{topic.capitalize()}: choose the correct definition.",
                f"Which option describes {topic}?"
            ],
            "medium": [
                f"What is the purpose of {topic} in learning systems?",
                f"Which statement about {topic} is true?",
                f"How does {topic} help improve model performance?"
            ],
            "hard": [
                f"Which advanced concept is related to {topic}?",
                f"In which scenario does {topic} perform poorly?",
                f"What is a limitation of {topic} in optimization?"
            ]
        }
        return random.choice(templates.get(difficulty, templates["medium"]))

    # ---------------------------
    # Choices + answer generator
    # ---------------------------
    def _generate_choices_and_answer(self, question):
        # correct answer is always A but shuffled later
        correct = "Correct explanation related to: " + question
        distractors = [
            "Incorrect but plausible statement.",
            "Another misconception.",
            "A random unrelated statement."
        ]

        choices = [correct] + distractors
        random.shuffle(choices)

        answer_index = choices.index(correct)
        answer_letter = ["A", "B", "C", "D"][answer_index]

        return choices, answer_letter
