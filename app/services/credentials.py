from dataclasses import dataclass
from getpass import getpass

import keyring


SERVICE_NAME = "ebanca_automation"


@dataclass
class Credentials:
    username: str
    password: str
    code: str


class CredentialService:

    def get_credentials(self) -> Credentials:

        username = input("Usuario eBanca: ").strip()

        if not username:
            raise ValueError("El usuario no puede estar vacío.")


        password = keyring.get_password(
            SERVICE_NAME,
            username
        )

        if password:

            print(
                "✓ Contraseña recuperada del gestor seguro."
            )

            code = getpass("Código eBanca: ")
        
            if not code:
                raise ValueError("El código no puede estar vacío.")

        
            return Credentials(
                username=username,
                password=password,
                code=code
            )

        password = getpass(
            "Contraseña eBanca: "
        )

        if not password:
            raise ValueError(
                "La contraseña no puede estar vacía."
            )

        guardar = input(
            "¿Guardar contraseña? [s/N]: "
        ).strip().lower()

        if guardar in {
            "s",
            "si",
            "sí",
            "y",
            "yes"
        }:

            self.save_password(
                username,
                password
            )


        code = getpass("Código eBanca: ")
        
        if not code:
            raise ValueError("El código no puede estar vacío.")

        

        return Credentials(
            username=username,
            password=password,
            code=code
        )


    # ======================================================
    # GUARDAR CONTRASEÑA
    # ======================================================

    def save_password(
        self,
        username: str,
        password: str
    ):

        keyring.set_password(
            SERVICE_NAME,
            username,
            password
        )

        print(
            "✓ Contraseña guardada correctamente."
        )


    # ======================================================
    # ACTUALIZAR CONTRASEÑA
    # ======================================================

    def update_password(
        self,
        username: str
    ):

        password_actual = keyring.get_password(
            SERVICE_NAME,
            username
        )

        if password_actual is None:

            print(
                "No existe una contraseña guardada para este usuario."
            )

            return False


        print(
            f"Actualizando contraseña para: {username}"
        )

        nueva_password = getpass(
            "Nueva contraseña: "
        )

        if not nueva_password:

            print(
                "La contraseña no puede estar vacía."
            )

            return False


        confirmar_password = getpass(
            "Confirmar nueva contraseña: "
        )


        if nueva_password != confirmar_password:

            print(
                "Las contraseñas no coinciden."
            )

            return False


        keyring.set_password(
            SERVICE_NAME,
            username,
            nueva_password
        )


        print(
            "✓ Contraseña actualizada correctamente."
        )

        return True


    # ======================================================
    # ELIMINAR CONTRASEÑA
    # ======================================================

    def delete_password(
        self,
        username: str
    ):

        password = keyring.get_password(
            SERVICE_NAME,
            username
        )


        if password is None:

            print(
                "No existe una contraseña guardada."
            )

            return False


        keyring.delete_password(
            SERVICE_NAME,
            username
        )


        print(
            "✓ Contraseña eliminada."
        )

        return True