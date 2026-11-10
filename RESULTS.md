# API lab results

## Part 0
- Step 0.1, the number of pizza names: 18
- Step 0.3, status code of the request without a token: 401
- Step 0.4, the name of your pizza: An Old Pugliese
- Step 0.12, results of the three runs without a session (optional):
- Step 0.16, blocks of "how many of the three tools are excluded":

## Defect report
- Title:
- Request:
- Expected result:
- Actual result:
- Severity:

## Part A
- Step A4, status codes when the other user reads, changes and deletes: read ___, update ___, delete ___

## Part B
1.
2.
3.
4.
5.
6.
7.
8.

# API lab

## How to install and run

    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    pytest -v

## Input domain model for POST /api/ratings

| Characteristic | Block | Value in the test | Test |
|---|---|---|---|
| C1 Value of stars | below 1 | 0 | test_stars_out_of_range[0] |
| C1 Value of stars | 1 to 5 (base) | 3 | test_base_choice_is_saved |
| C1 Value of stars | above 5 | 6 | test_stars_out_of_range[6] |
| C2 Type of stars | whole number (base) | 3 | test_base_choice_is_saved |
| C2 Type of stars | decimal | 3.5 | |
| C2 Type of stars | text | "3" | |
| C2 Type of stars | missing | no field | |
| C3 Pizza | exists (base) | a new pizza | test_base_choice_is_saved |
| C3 Pizza | does not exist | 999999999 | |
| C4 Token | the user's own (base) | from auth | test_base_choice_is_saved |
| C4 Token | none | no header | |
| C4 Token | wrong length | token short | |