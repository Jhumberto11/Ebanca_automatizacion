from core.exceptions import LoginFlowError
from pages.login_page import LoginPage
from services.credentials import Credentials


class LoginWorkflow:
    def __init__(self, driver):
        self.page = LoginPage(driver)

    def execute(self, credentials: Credentials):
        try:
            self.page.load()

            self.page.enter_username(credentials.username)
            self.page.continue_after_username()

            self.page.enter_code(credentials.code)
            self.page.submit_code()

            # Si el banco solicita una etapa adicional/MFA antes de mostrar
            # la contraseña, aquí es donde se puede agregar en el futuro.
            self.page.enter_password(credentials.password)
            self.page.submit_login()

        except Exception as exc:
            raise LoginFlowError(
                "No se pudo completar el flujo de inicio de sesión. "
                "Puede que los selectores de la página hayan cambiado."
            ) from exc
