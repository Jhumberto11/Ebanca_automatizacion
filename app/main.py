
import traceback

from core.browser import BrowserManager
from services.credentials import CredentialService
from utils.logging_config import configure_logging
from workflows.login_workflow import LoginWorkflow


credential_service = CredentialService()


print("""
==============================
        E-BANCA
==============================

1. Iniciar sesión
2. Actualizar contraseña guardada
3. Eliminar contraseña guardada
0. Salir
""")


opcion = input(
    "Seleccione una opción: "
).strip()


if opcion == "1":

    credentials = credential_service.get_credentials()

    print(
        f"Usuario: {credentials.username}"
    )


elif opcion == "2":

    username = input(
        "Usuario eBanca: "
    ).strip()

    credential_service.update_password(
        username
    )


elif opcion == "3":

    username = input(
        "Usuario eBanca: "
    ).strip()

    credential_service.delete_password(
        username
    )


elif opcion == "0":

    print(
        "Saliendo..."
    )

def main():
    configure_logging()

    browser = BrowserManager()

    try:
        credentials = credential_service

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