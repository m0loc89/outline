from pages.document_page import DocumentPage


def test_creacion_documento(driver):
    """Caso 2 (Válida): crear documento con título válido."""
    # TODO: requiere sesión autenticada previa (ver test_login.py)
    assert True


def test_titulo_largo(driver):
    """Caso 3 (Frontera): título con 255 caracteres, límite superior."""
    titulo = "A" * 255
    # TODO: completar con la creación real del documento y la aserción
    # de que el título no se truncó.
    assert True


def test_caso_frontera(driver):
    """Caso 4 (Frontera): título con 1 carácter, límite inferior."""
    titulo = "A"
    # TODO: completar con la creación real del documento y la aserción
    # de que el documento se crea correctamente.
    assert True
