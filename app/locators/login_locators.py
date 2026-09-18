from selenium.webdriver.common.by import By


class LoginLocators:
    """
    Los selectores del sitio viven SOLO aquí.

    Si eBanca cambia su HTML, modifica este archivo en vez de tocar
    páginas, workflows o servicios.
    """

    USERNAME_CANDIDATES = [
        (By.CSS_SELECTOR, 'input[autocomplete="off"]'),
        (By.CSS_SELECTOR, 'input[name*="user" i]'),
        (By.CSS_SELECTOR, 'input[id*="user" i]'),
        (By.XPATH, '//input[contains(translate(@placeholder,"USUARIO","usuario"),"usuario")]'),
    ]

    CONTINUE_CANDIDATES = [
        (By.XPATH, '//button[contains(translate(normalize-space(.),"CONTINUAR","continuar"),"continuar")]'),
        (By.XPATH, '//button[contains(translate(normalize-space(.),"SIGUIENTE","siguiente"),"siguiente")]'),
        (By.XPATH, '//input[@type="submit"]'),
        (By.CSS_SELECTOR, 'button[type="submit"]'),
    ]

    PASSWORD_CODE = [
        (By.CSS_SELECTOR, 'input[type="password"]'),
        (By.CSS_SELECTOR, 'input[autocomplete="current-password"]'),
    ]

    PASSWORD_CANDIDATES = [
       (By.CSS_SELECTOR, 'input.ui-keyboard-input[type="password"]'),
        (By.CSS_SELECTOR, 'input[type="password"]'),
        (By.CSS_SELECTOR, 'input[autocomplete="current-password"]'),
    ]

    CONTINUE_CODE = [
        (By.XPATH, '//button[contains(translate(normalize-space(.),"INGRESAR","ingresar"),"ingresar")]'),
        (By.XPATH, '//button[contains(translate(normalize-space(.),"INICIAR","iniciar"),"iniciar")]'),
        (By.CSS_SELECTOR, 'button[type="submit"]'),
        (By.XPATH, '//input[@type="submit"]'),
    ]

    LOGIN_CANDIDATES = [
        (By.XPATH, '//button[contains(translate(normalize-space(.),"CONTINUAR","continuar"),"continuar")]'),
        (By.XPATH, '//button[contains(translate(normalize-space(.),"INICIAR","iniciar"),"iniciar")]'),
        (By.CSS_SELECTOR, 'button[type="submit"]'),
        (By.XPATH, '//input[@type="submit"]'),
    ]
