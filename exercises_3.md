# Zadania dla uczniów — lekcja 3

## Zadanie 1 — Compose smoke check dla Pull Requestów

### Cel
Przy każdym `pull_request` chcemy sprawdzić, czy stack z `docker-compose.yml` wstaje poprawnie.

### Wymagania
Utwórz workflow `.github/workflows/compose-pr-check.yml`, który:

1. uruchamia się na:
   - `pull_request`
2. ma jeden job `compose-smoke`,
3. wykonuje:
   - checkout repo,
   - `docker compose up -d --build`,
   - krótkie oczekiwanie na start aplikacji,
   - `curl --fail http://127.0.0.1:8000/health`,
4. zapisuje logi do pliku `compose.log`,
5. wysyła `compose.log` jako artifact o nazwie `compose-logs`,
6. dodaje wpis do `GITHUB_STEP_SUMMARY`, w którym będą:
   - event,
   - ref,
   - informacja, czy smoke test przeszedł,
7. zatrzymuje Compose na końcu,
8. upload logów i cleanup mają działać nawet wtedy, gdy smoke test nie przejdzie.

### Podpowiedź
Użyj:
- `if: always()`
- `docker compose logs > compose.log`
- `actions/upload-artifact@v4`

---

## Zadanie 2 — Symulowany release tylko dla branch `master`

### Cel
Nie mamy własnego serwera ani registry, więc zasymulujemy release:
- budujemy obraz,
- zapisujemy go do pliku,
- wrzucamy go jako artifact.

### Wymagania
Utwórz workflow `.github/workflows/simulated-release.yml`, który:

1. uruchamia się na:
   - `push`
2. ma job `package-image`,
3. job ma działać **tylko wtedy**, gdy push jest na branch `master`,
4. workflow ma:
   - checkout repo,
   - build obrazu z tagiem `gha-gr2-release:${{ github.sha }}`,
   - `docker save` do pliku `image.tar`,
   - kompresję do `image.tar.gz`,
   - upload artifact o nazwie `docker-image-${{ github.sha }}`,
5. doda wpis do `GITHUB_STEP_SUMMARY`, w którym będą:
   - actor,
   - branch/ref,
   - SHA,
   - nazwa artefaktu,
   - informacja, że to symulowany release.

### Podpowiedź
Użyj warunku:
- `if: ${{ github.ref == 'refs/heads/master' }}`

---

## Zadanie 3 — dla chętnych

Rozszerz `compose-pr-check.yml` tak, aby:
1. summary wyświetlało też numer PR,
2. artifact miał nazwę zawierającą numer PR,
3. w summary znalazła się linia:
   - kto uruchomił workflow,
   - jaki event go uruchomił.

### Podpowiedź
Sprawdź:
- `github.actor`
- `github.event.pull_request.number`