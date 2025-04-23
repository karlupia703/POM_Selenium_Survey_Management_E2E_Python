from Config.config import Config

class Translations:
    DATA = {
        "en_US": {
            "program": "Graphic Design",
            "title": "Survey Management",
            "googleButton": "Sign In with Google",
            "accessWithGoogle": "Access to Survey Management App",
            "signInButton": "Sign In"
        },
        "Español": {
            "program": "Diseño Gráfico",
            "title": "Gestión de Encuestas",
            "googleButton": "Iniciar sesión con Google",
            "accessWithGoogle": "Acceso a la aplicación de gestión de encuestas",
            "signInButton": "Iniciar sesión"

        },
        "pt_BR": {
            "program": "Design Gráfico",
            "title": "Gestão de Pesquisas",
            "googleButton": "Entrar com o Google",
            "accessWithGoogle": "Acesso ao aplicativo de gerenciamento de pesquisas",
            "signInButton": "Entrar"
        }
    }

    @classmethod
    def current_search_term(cls):
        # Safely get the "program" field based on current language
        return cls.DATA.get(Config.language, cls.DATA["en_US"]).get("program")

    @classmethod
    def get_translation(cls, lang_code):
        return cls.DATA.get(lang_code, {})
