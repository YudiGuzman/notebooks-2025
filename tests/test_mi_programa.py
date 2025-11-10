# tests/test_mi_programa.py
import math
import pytest
from mi_programa import sumar

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
@pytest.mark.parametrize("a,b", [(5, 3), (-2, 7), (0.1, 0.3), (0, 10)])
def test_sumar_conmutatividad(a, b):
    assert sumar(a, b) == sumar(b, a)

# --- Tipos inválidos: debe lanzar TypeError ---
@pytest.mark.parametrize("a,b", [
    ("2", 3),
    (None, 1),
    ([], 5),
    (3, {"x": 1}),
])
def test_sumar_tipos_invalidos(a, b):
    with pytest.raises(TypeError):
        sumar(a, b)

# --- Propiedad básica: a + 0 == a ---
@pytest.mark.parametrize("a", [0, 1, -1, 1.5, -3.2, 10**5])
def test_sumar_elemento_neutro(a):
    assert sumar(a, 0) == a
    assert sumar(0, a) == a
