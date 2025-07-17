setlocal

set RAW=output\raw.txt
set SUM=output\summary.txt

if not exist output (
    mkdir output
)

extract_text "%~1" %RAW% || exit /b
summarize %RAW% %SUM% || exit /b

echo Done! Summary saved at %SUM%