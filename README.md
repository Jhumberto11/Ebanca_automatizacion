# eBanca Automation - arquitectura escalable

Proyecto base en Python + Selenium.

## 1. Crear entorno
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## 2. Configuración
Copia `.env.example` como `.env`.

## 3. Ejecutar
```bash
python -m app.main
```

O doble clic en `run.bat`.

## Credenciales
La contraseña NO se guarda en el código. La primera vez se solicita en consola y
puede almacenarse en el gestor seguro de credenciales del sistema mediante `keyring`.

## ChromeDriver
No necesitas descargar ChromeDriver manualmente. `webdriver.Chrome()` utiliza
Selenium Manager para resolver un driver compatible y almacenarlo en caché.

## Sesión
El navegador puede permanecer abierto y el perfil de Chrome es persistente.
Esto NO evita un cierre de sesión impuesto por el banco por seguridad o inactividad.

## Si cambia el HTML del banco
Los selectores están centralizados en:

`app/locators/login_locators.py`

Así no necesitas modificar el resto de la aplicación.
