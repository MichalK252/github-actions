# GitHub Actions - lekcja 2

Repo startowe do lekcji o wielu jobach w CI.

## Masz już gotowe
- prostą aplikację Flask,
- testy `pytest`,
- `Dockerfile` i `docker-compose.yml`,
- workflow z jednym jobem testowym z lekcji 1.

## Cel tej lekcji
Rozbudować workflow tak, aby miał osobny job `lint`, osobny job `test`, zależność `needs` oraz dwa czytelne statusy w Pull Requeście.

## Uruchomienie lokalne
```bash
pip install -r requirements.txt
ruff check .
pytest -q
```

## Przykładowy przebieg pracy na lekcji
1. Utwórz branch `feature/first-ci`.
2. Dodaj plik `.github/workflows/ci.yml`.
3. Wypchnij branch do GitHuba.
4. Otwórz Pull Request.
5. Sprawdź wynik pipeline'u w zakładce **Checks** i **Actions**.
6. Celowo zepsuj test, zobacz czerwony pipeline, napraw i ponów.

# GitHub Actions - lekcja 2

Repo startowe do lekcji o wielu jobach w CI.

## Masz już gotowe
- prostą aplikację Flask,
- testy `pytest`,
- `Dockerfile` i `docker-compose.yml`,
- workflow z jednym jobem testowym z lekcji 1.

## Cel tej lekcji
Rozbudować workflow tak, aby miał osobny job `lint`, osobny job `test`, zależność `needs` oraz dwa czytelne statusy w Pull Requeście.

## Uruchomienie lokalne
```bash
pip install -r requirements.txt
ruff check .
pytest -q
```

## Szybki błąd demonstracyjny
Dopisz na początku `app/main.py` linię `import os`.
Ruff zgłosi wtedy nieużywany import.

