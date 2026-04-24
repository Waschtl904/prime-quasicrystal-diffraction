# Prime–Quasicrystal Diffraction

Numerische und theoretische Untersuchung von Beugungsspektren
arithmetischer Punktmengen (Primzahlen und Varianten) und deren Beziehung
zu Quasikristallen.

## Forschungsfrage

> Wie lässt sich das Beugungsspektrum der eindimensionalen Primzahlmenge
> und ausgewählter arithmetisch definierter Unterfolgen im Rahmen der
> Quasikristall-Theorie (Cut-and-Project, Approximanten, Spektraltypen)
> präzise einordnen, und inwiefern zeigen diese Systeme quasikristallähnliche
> oder neue Spektralmerkmale?

## Teilfragen

1. **Numerische Strukturfrage** – Wie unterscheidet sich das Beugungsspektrum
   der Primzahlen von Poisson-Zufallspunkten und klassischen 1D-Quasikristallen
   (Fibonacci-Kette, Sturmian-Sequenzen)?
2. **Arithmetische Variationsfrage** – Wie verändern sich Spektrum und
   Hyperuniformität bei arithmetischen Filtern (Restklassen mod q,
   Faktorisierungsmuster, Primideale in Zahlkörpern)?
3. **Einordnungsfrage** – Lassen sich die Spektralmerkmale als
   „approximantenartig" oder als neue Klasse zwischen kristallin /
   quasikristallin / hyperuniform-zufällig interpretieren?

## Projektstruktur

```
prime-quasicrystal-diffraction/
├── src/                  # Python-Module
│   ├── point_sets.py     # Erzeugung arithmetischer Punktmengen
│   ├── diffraction.py    # Strukturfaktor und Beugungsintensität
│   └── analysis.py       # Hyperuniformität, Spektraltypen
├── notebooks/            # Jupyter-Notebooks für Exploration
├── data/                 # Gespeicherte Spektren und Punktmengen
├── docs/                 # Projektplan, Notizen, Paper-Entwurf
└── README.md
```

## Erste Schritte

```bash
git clone https://github.com/Waschtl904/prime-quasicrystal-diffraction.git
cd prime-quasicrystal-diffraction
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install numpy scipy matplotlib jupyter sympy
```

## Abhängigkeiten

- Python 3.10+
- numpy, scipy, matplotlib
- jupyter
- sympy (für symbolische Zahlentheorie)

## Schlüsselliteratur

| Quelle | Relevanz |
|--------|----------|
| Torquato et al. (2018, PRL) | Primzahlen als hyperuniformes Vielteilchensystem |
| Pink (ETH Antrittsvorlesung) | Zahlentheorie und Quasikristalle |
| Levine & Steinhardt (1984, PRL) | Quasikristalle: neue Klasse geordneter Strukturen |
| Baake & Grimm (Aperiodic Order) | Standardwerk Quasikristall-Mathematik |
| Smith et al. (2023, arXiv) | Hat-Monokachel / Einstein-Problem |

## Lizenz

MIT License
