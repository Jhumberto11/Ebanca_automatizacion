from dataclasses import dataclass
from getpass import getpass

import keyring


SERVICE_NAME = "ebanca_automation"


@dataclass
class Credentials:
    username: str
    password: str
    code : str


class CredentialService:
    def get_credentials(self) -> Credentials:
        username = input("Usuario eBanca: ").strip()

        if not username:
            raise ValueError("El usuario no puede estar vacío.")


        code = getpass("Codigo eBanca: ")

        if not code:
            raise ValueError("El código no puede estar vacío.") 

        password = keyring.get_password(SERVICE_NAME, username)

        if password:
            print("✓ Contraseña recuperada del gestor seguro del sistema.")
            return Credentials(username=username, password=password, code=code)

        password = getpass("Contraseña eBanca: ")

        if not password:
            raise ValueError("La contraseña no puede estar vacía.")

        save = input(
            "¿Guardar la contraseña en el gestor seguro del sistema? [s/N]: "
        ).strip().lower()

        if save in {"s", "si", "sí", "y", "yes"}:
            keyring.set_password(SERVICE_NAME, username, password)
            print("✓ Contraseña guardada en el gestor seguro.")

        return Credentials(username=username, password=password, code=code)
