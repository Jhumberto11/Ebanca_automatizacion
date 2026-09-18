import traceback

from core.browser import BrowserManager
from services.credentials import CredentialService
from utils.logging_config import configure_logging
from workflows.login_workflow import LoginWorkflow


def main():
    configure_logging()

    browser = BrowserManager()

    try:
        credentials = CredentialService().get_credentials()

        driver = browser.start()

        workflow = LoginWorkflow(driver)
        workflow.execute(credentials)

        print()
        print("✓ Flujo de login ejecutado.")
        print("✓ Chrome permanecerá abierto.")
        print()
        print(
            "Nota: el perfil de Chrome es persistente, pero un cierre de "
            "sesión impuesto por el banco por seguridad o inactividad "
            "no se intenta evitar."
        )

    except Exception as exc:
        print()
        print(f"ERROR: {exc}")
        print()
        traceback.print_exc()

    finally:
        browser.close()


if __name__ == "__main__":
    main()
