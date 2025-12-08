import random

class IdeaGeneratorService:

    BASE_TEMPLATES = [
        # Загальні ідеї для pet-project
        "Створіть концепцію веб-проєкту на тему {keywords} з атмосферою {mood}.",
        "Сформуйте макет веб-сайту, де {keywords}, у стилі {mood}.",
        "Придумайте креативний landing page для {keywords} з настроєм {mood}.",
        "Розробіть прототип для pet-project з {keywords}, використовуючи {mood} стиль.",

        # Header
        "Створіть унікальний дизайн header для сайту про {keywords} з {mood} атмосферою.",
        "Придумайте інтерактивний header, що підкреслює {keywords} та передає настрій {mood}.",
        "Сформуйте концепт sticky header для {keywords} у {mood} стилі.",

        # Footer
        "Розробіть сучасний footer для {keywords}, який відображає {mood} атмосферу.",
        "Придумайте footer з інтерактивними елементами для проєкту на тему {keywords}, у стилі {mood}.",

        # Landing
        "Сформуйте структуру landing page для {keywords} з {mood} дизайном.",
        "Придумайте креативні секції для landing page на тему {keywords}, підкреслюючи {mood}.",

        # Portfolio / компоненти
        "Розробіть портфоліо-елементи для {keywords} із {mood} стилем.",
        "Придумайте дизайн карток та UI-компонентів для {keywords} у {mood} атмосфері.",
        "Створіть інтерактивні кнопки та форми для проєкту {keywords}, використовуючи {mood} настрій."
    ]

    MOOD_TRANSLATION = {
        "dark": "темна",
        "bright": "світла",
        "mystery": "містична",
        "sci-fi": "науково-фантастична",
        "romance": "романтична"
    }

    @classmethod
    def generate(cls, keywords: str, mood: str = None, idea_type: str = None) -> str:
        keywords = keywords.strip()
        mood_text = cls.MOOD_TRANSLATION.get(mood, "нейтральна")
        idea_type_text = idea_type or "загальна"

        # Вибір шаблону з урахуванням типу ідеї
        relevant_templates = []
        for template in cls.BASE_TEMPLATES:
            if idea_type_text.lower() in template.lower() or idea_type_text == "загальна":
                relevant_templates.append(template)

        # Якщо для типу немає конкретного шаблону, використовуємо всі
        if not relevant_templates:
            relevant_templates = cls.BASE_TEMPLATES

        template = random.choice(relevant_templates)
        result = f"[Тип ідеї: {idea_type_text}] " + template.format(keywords=keywords, mood=mood_text)
        return result
