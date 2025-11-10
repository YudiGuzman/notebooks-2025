# -*- coding: utf-8 -*-
"""
Módulo de utilidades aritméticas mínimas para prácticas XP.

Provee una función `sumar(a, b)` robusta, con *type hints* y validación
de entradas para ayudar a escribir pruebas unitarias con PyTest.

Uso esperado
------------
>>> sumar(2, 7)
9
>>> sumar(-1, 1)
0
>>> sumar(0.1, 0.2)
0.30000000000000004
"""

from typing import Union

Numeric = Union[int, float]

def _ensure_numeric(x, name: str) -> None:
    """Valida que `x` sea numérico (int o float), de lo contrario lanza TypeError."""
    if not isinstance(x, (int, float)):
        raise TypeError(f"{name} debe ser numérico (int o float); se recibió {type(x).__name__}")

def sumar(a: Numeric, b: Numeric) -> Numeric:
    """Suma dos valores numéricos.

    Parámetros
    ----------
    a : int | float
    b : int | float

    Retorna
    -------
    int | float
        La suma de `a` y `b`.

    Levanta
    -------
    TypeError
        Si `a` o `b` no son numéricos.
    """
    _ensure_numeric(a, "a")
    _ensure_numeric(b, "b")
    return a + b
