# tests/test_mi_programa.py
import math
# os - trabajar con rutas de carpetas
# sys - acceder a lista de rutas donde Python busca módulos
import sys, os
# os.path.dirname(_file_) - devuelve la carpeta actual donde esta el archivo test_mi_programa.py
# os.path.join () - sube un nivel en la estructura de carpetas - '..' - carpeta padre
# os.path.abspath() - convierte la ruta en una ruta absoluta completa
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from src.mi_programa import sumar

# --- Casos felices (enteros y flotantes) ---
@pytest.mark.parametrize(
    "a,b,expected",
    [
        (2, 7, 9),
        (-1, 1, 0),
        (0, 0, 0),
        (10**6, 10**6, 2 * 10**6),
        (0.1, 0.2, 0.30000000000000004),  # mostrando la acumulación de error binario
        (-3.5, 1.2, -2.3),
    ],
)
def test_sumar_valores_validos(a, b, expected):
    assert sumar(a, b) == expected

# --- Conmutatividad: sumar(a, b) == sumar(b, a) para varios pares ---
# En XP se llama "property test" porque no valida un caso puntual sino una regla general de comportamiento esperado
@pytest.mark.parametrize("a,b", [(5, 3), (-2, 7), (0.1, 0.3), (0, 10)])
def test_sumar_conmutatividad(a, b):
    assert sumar(a, b) == sumar(b, a)

# --- Tipos inválidos: debe lanzar TypeError --- Verifica la robustez de la función sumar()
@pytest.mark.parametrize("a,b", [
    ("2", 3),
    (None, 1),
    ([], 5),
    (3, {"x": 1}),
])
def test_sumar_tipos_invalidos(a, b):
    with pytest.raises(TypeError):
        sumar(a, b)

# --- Propiedad básica: a + 0 == a ---Prueba de propiedad matemática
@pytest.mark.parametrize("a", [0, 1, -1, 1.5, -3.2, 10**5])
def test_sumar_elemento_neutro(a):
    assert sumar(a, 0) == a
    assert sumar(0, a) == a
