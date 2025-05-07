from config.config import Config

class Translations:
    DATA = {
        "en_US": {
            "program": "Graphic Design",
            "title": "Survey Management",
            "googleButton": "Sign In with Google",
            "accessWithGoogle": "Access to Survey Management App",
            "signInButton": "Sign In",
            "createQuestionTitle": "Create question",
            "questionTypeError": "Question type is required",
            "abbreviationNameError": "Abbreviation is required",
            "questionDescriptionError": "Question description is required",
            "editTitle": "Edit question",
            "deleteDialogTitle": "Delete question",
            "deleteDialogBodyText": "Are you sure you want to delete this question?"

        },
        "Español": {
            "program": "Diseño Gráfico",
            "title": "Gestión de Encuestas",
            "googleButton": "Iniciar sesión con Google",
            "accessWithGoogle": "Acceso a la aplicación de gestión de encuestas",
            "signInButton": "Iniciar sesión",
            "createQuestionTitle": "Crear pregunta",
            "questionTypeError": "El tipo de pregunta es obligatorio",
            "abbreviationNameError": "Abreviatura obligatoria",
            "questionDescriptionError": "La descripción de la pregunta es obligatoria",
            "editTitle": "Editar pregunta",
            "deleteDialogTitle": "Eliminar pregunta",
            "deleteDialogBodyText": "¿Está seguro de querer eliminar esta pregunta?"


        },
        "pt_BR": {
            "program": "Design Gráfico",
            "title": "Gestão de Pesquisas",
            "googleButton": "Entrar com o Google",
            "accessWithGoogle": "Acesso ao aplicativo de gerenciamento de pesquisas",
            "signInButton": "Entrar",
            "createQuestionTitle": "Criar pergunta",
            "questionTypeError": "O tipo de pergunta é obrigatório",
            "abbreviationNameError": "A abreviatura é obrigatória",
            "questionDescriptionError": "A descrição da pergunta é obrigatória",
            "editTitle": "Editar pergunta",
            "deleteDialogTitle": "",
            "deleteDialogBodyText": ""
        }
    }

    @classmethod
    def current_search_term(cls):
        # Safely get the "program" field based on current language
        return cls.DATA.get(Config.language, cls.DATA["en_US"]).get("program")

    @classmethod
    def get_translation(cls, lang_code):
        return cls.DATA.get(lang_code, {})
