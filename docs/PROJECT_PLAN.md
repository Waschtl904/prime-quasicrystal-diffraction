# Projektplan: Prime–Quasicrystal Diffraction

## Forschungsfrage

> Wie laesst sich das Beugungsspektrum der eindimensionalen Primzahlmenge
> und ausgewaehlter arithmetisch definierter Unterfolgen im Rahmen der
> Quasikristall-Theorie (Cut-and-Project, Approximanten, Spektraltypen)
> praezise einordnen, und inwiefern zeigen diese Systeme quasikristallaehliche
> oder neue Spektralmerkmale?

---

## Etappenplan

### Etappe 1 – Bootstrap (Monat 1)

- [ ] Literatur lesen:
  - Torquato / Zhang / de-Courcy-Ireland: Primzahlen als hyperuniformes System (PRL 2018)
  - Pink: "Symmetrie und Zahlentheorie am Beispiel von Quasikristallen" (ETH-Vortrag)
  - Levine & Steinhardt (1984, PRL): Quasikristalle als neue Klasse geordneter Strukturen
- [ ] `notebooks/01_primes_diffraction_basics.ipynb` durcharbeiten
- [ ] `src/analysis.py` testen: number_variance fuer Primzahlen vs. Zufall

### Etappe 2 – Numerische Experimente (Monat 2)

- [ ] Systematischer Vergleich: Intervalle [N, 2N] fuer wachsendes N
- [ ] Arithmetische Varianten: p == a mod q fuer verschiedene a, q
- [ ] Hyperuniformitaetsexponent alpha fuer alle Varianten bestimmen
- [ ] Erste Plots und Beobachtungen in docs/ dokumentieren

### Etappe 3 – Theorie und Einordnung (Monat 3)

- [ ] Vergleich mit Approximanten-Theorie und Cut-and-Project-Konstruktionen
- [ ] Pisot-/Salem-Zahlen Exkurs: Verbindung zu Inflationsfaktoren
- [ ] Erste Conjectures formulieren und in docs/conjectures.md festhalten

### Etappe 4 – Verallgemeinerungen (Monat 4–6, optional)

- [ ] 2D-Verallgemeinerung: Primzahlen in Gaussschen / Eisenstein-Zahlen
- [ ] Primideale in Q(sqrt(5)) projiziert auf R – Penrose-Verbindung
- [ ] Paper-Entwurf (docs/paper_draft.md)

---

## Schluesselliteratur

| Quelle | Relevanz |
|--------|----------|
| Torquato et al. (2018, PRL) | Primzahlen als hyperuniformes Vielteilchensystem |
| Pink (ETH Antrittsvorlesung) | Zahlentheorie und Quasikristalle |
| Levine & Steinhardt (1984, PRL) | Quasikristalle: neue Klasse geordneter Strukturen |
| Baake & Grimm: Aperiodic Order | Standardwerk Quasikristall-Mathematik |
| Smith et al. (2023, arXiv:2303.10798) | Hat-Monokachel / Einstein-Problem |

## Werkzeuge

- Python 3.10+: numpy, scipy, matplotlib, sympy, jupyter
- GitHub fuer Versionskontrolle
- LaTeX (optional) fuer Paper-Entwurf
