class AutomationError(Exception):
    """Error base de la automatización."""


class ElementNotFoundError(AutomationError):
    """No se pudo localizar un elemento requerido."""


class LoginFlowError(AutomationError):
    """Falló el flujo de inicio de sesión."""
