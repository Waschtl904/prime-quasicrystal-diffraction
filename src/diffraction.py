"""Strukturfaktor und Beugungsintensitaet fuer 1D-Punktmengen."""

import numpy as np


def structure_factor(points: np.ndarray, k_values: np.ndarray) -> np.ndarray:
    """
    Strukturamplitude F(k) = (1/N) * sum_j exp(-i k x_j)

    Parameters
    ----------
    points   : 1D-Array der Punktpositionen
    k_values : 1D-Array der k-Werte

    Returns
    -------
    Komplexes 1D-Array F(k)
    """
    points = np.asarray(points, dtype=float)
    k_values = np.asarray(k_values, dtype=float)
    phases = np.exp(-1j * np.outer(k_values, points))
    return phases.mean(axis=1)


def diffraction_intensity(points: np.ndarray, k_values: np.ndarray) -> np.ndarray:
    """Beugungsintensitaet S(k) = |F(k)|^2"""
    return np.abs(structure_factor(points, k_values)) ** 2


def k_grid(k_min: float, k_max: float, n_points: int) -> np.ndarray:
    """Gleichmaessiges k-Gitter fuer Beugungsscan."""
    return np.linspace(k_min, k_max, n_points)
