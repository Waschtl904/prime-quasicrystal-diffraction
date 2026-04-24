"""Analyse von Spektraltypen und Hyperuniformitaet."""

import numpy as np


def number_variance(points: np.ndarray, radii: np.ndarray) -> np.ndarray:
    """
    Varianz der Punktanzahl in Intervallen der Laenge 2R.

    Fuer hyperuniforme Systeme waechst sigma^2(R) langsamer als R.
    Fuer Poisson-Zufall gilt sigma^2(R) ~ R (normal).
    Fuer periodische Kristalle gilt sigma^2(R) ~ const.

    Parameters
    ----------
    points : 1D-Array der Punktpositionen (muss nicht sortiert sein)
    radii  : Array von Fensterradien R > 0

    Returns
    -------
    variance : Array der Varianzen sigma^2(R)
    """
    points = np.sort(np.asarray(points, dtype=float))
    variances = []
    for R in radii:
        centers = np.arange(
            points[0] + R, points[-1] - R, step=max(R / 10, 1.0)
        )
        counts = [
            int(np.sum((points >= c - R) & (points <= c + R)))
            for c in centers
        ]
        variances.append(np.var(counts) if len(counts) > 1 else np.nan)
    return np.array(variances)


def hyperuniformity_exponent(radii: np.ndarray, variance: np.ndarray) -> float:
    """
    Schaetze den Hyperuniformitaetsexponenten alpha aus sigma^2(R) ~ R^alpha.

    Interpretation:
      alpha < 1  -> hyperuniform
      alpha ~ 1  -> Poisson-artig
      alpha > 1  -> geclustert

    Returns float (nan wenn zu wenig Datenpunkte).
    """
    mask = (radii > 0) & (variance > 0) & ~np.isnan(variance)
    if mask.sum() < 2:
        return float("nan")
    log_R = np.log(radii[mask])
    log_V = np.log(variance[mask])
    alpha, _ = np.polyfit(log_R, log_V, 1)
    return float(alpha)
