# Zadania dla uczniów - lekcja 2

1. Wskaż w pliku `.github/workflows/ci.yml`: nazwę workflow, eventy, job i step.
2. Dodaj job `lint` z `ruff check .`.
3. Ustaw `needs: lint` w jobie `test`.
4. Wywołaj celowy błąd lint, sprawdź PR i napraw go.
5. Dla chętnych: dodaj artifact z raportem testów i wpis do `GITHUB_STEP_SUMMARY`.
