from services.credentials import CredentialService


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