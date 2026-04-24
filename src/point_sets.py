"""Erzeugung arithmetischer Punktmengen fuer Beugungsexperimente."""

import numpy as np


def primes_in_interval(N: int, M: int) -> np.ndarray:
    """Alle Primzahlen im Intervall [N, M] via Sieb des Eratosthenes."""
    sieve = np.ones(M + 1, dtype=bool)
    sieve[:2] = False
    for p in range(2, int(np.sqrt(M)) + 1):
        if sieve[p]:
            sieve[p * p: M + 1: p] = False
    primes = np.nonzero(sieve)[0]
    return primes[(primes >= N) & (primes <= M)].astype(float)


def primes_residue_class(N: int, M: int, a: int, q: int) -> np.ndarray:
    """Primzahlen p in [N, M] mit p == a (mod q)."""
    ps = primes_in_interval(N, M)
    return ps[ps % q == a % q]


def random_uniform(N: float, M: float, count: int, seed: int = None) -> np.ndarray:
    """Gleichverteilte Zufallspunkte in [N, M] (Poisson-Referenz)."""
    rng = np.random.default_rng(seed)
    return np.sort(rng.uniform(N, M, size=count))


def fibonacci_chain(N_points: int, alpha: float = None) -> np.ndarray:
    """
    Eindimensionale Fibonacci-Kette (kanonisches 1D-Quasikristall-Modell).

    Konstruiert als Sturmian-Sequenz: x_n = floor((n+1)*alpha) + n
    mit alpha = 1/phi (phi = goldener Schnitt) per Default.
    """
    if alpha is None:
        alpha = 2.0 / (1.0 + np.sqrt(5.0))  # 1/phi
    return np.array(
        [np.floor((n + 1) * alpha) + n for n in range(N_points)],
        dtype=float,
    )
