# Sample Data Generator

This repository contains `generate_sampledata.py`, a small Python script that generates CSV mock data matching the structure of `sampledata.csv` included in the workspace. The goal of this README is to explain the tool step-by-step so other engineers can understand, reproduce, and extend the generator following software engineering best practices.

**Why this exists:**
- **Purpose:** Create repeatable mock invoice/transaction CSVs for testing ETL, analytics, and UI work.
- **Audience:** engineers and data testers who need realistic, reproducible test data.

**Quick start**

1. Ensure you have Python 3 installed (tested with Python 3.8+).
2. Run the generator (example produces 20 rows):

```bash
python3 generate_sampledata.py --rows 20 --output sampledata_generated.csv --seed 42
```

3. Preview the generated file:

```bash
head -n 10 sampledata_generated.csv
```

**Command-line options**

- `--rows` / `-n`: number of rows to generate (default: `10`).
- `--output` / `-o`: output CSV file path (default: `sampledata_out.csv`).
- `--seed`: integer seed for the random generator to ensure reproducibility (optional).

**File / Data schema**

The output CSV header and a short description of each column (matches `sampledata.csv`):

- `created_at`: date invoice record was created (YYYY-MM-DD).
- `updated_at`: date the record was last updated (>= `created_at`).
- `id`: unique integer identifier for the row.
- `merchant_id`: integer ID for the merchant.
- `member_id`: integer ID for the member/customer.
- `date`: invoice date (often on or before `created_at`).
- `total_amount`: invoice subtotal (two decimals).
- `invoice_number`: string invoice identifier (e.g., `INV001`).
- `gst_amount`: tax amount (two decimals).
- `gross_transaction_amount`: `total_amount + gst_amount`.
- `merchant_gst_number`: simple mock GST string (e.g., `MGST123`).
- `rebates`: rebate amount (two decimals).
- `extras`: extras (kept `0.00` by default).
- `debtiCreditIndicator`: `C` or `D` for credit/debit.
- `pdf_inv_category`: category string (e.g., `services`, `products`).
- `process_status`: `processed` or `failed`.
- `failure_reason`: non-empty when `process_status` is `failed`.
- `discount_delta`, `total_discount_delta`: discount-related numeric fields.
- `manual_review_status`: e.g., `approved`, `pending`, `review_needed`.
- `extracted_invoice_date`: duplicate of `date` used for extraction tests.
- `pdf_generated_file_name`: filename like `invoice1.pdf`.
- `file_id`: numeric file identifier.
- `due_date`: usually `date + 30 days`.

Design notes and rationale

- Single-file, dependency-free script: makes it easy to run in CI and local machines without installing packages.
- Deterministic behavior via `--seed`: pass a seed to reproduce the same output for tests.
- Realistic value ranges: amounts, GST rates, and date windows are chosen to mirror typical invoices; these can be tuned in the script.
- Clear function separation: the script includes helper functions for random date selection, money formatting, and a `generate_row` function to encapsulate row logic. This improves testability and makes extension straightforward.

Step-by-step process (what the script does)

1. Parse CLI args (`--rows`, `--output`, `--seed`).
2. Optionally seed the PRNG (makes the run deterministic).
3. For each row index from `1..rows`:
	- Choose a `created_at` date in a configurable recent window (default: within the last 30 days).
	- Set `updated_at` to be `created_at + 0..5 days`.
	- Set invoice `date` near `created_at`.
	- Generate `total_amount` as a float in a configurable range and calculate `gst_amount` using a chosen GST rate.
	- Compute `gross_transaction_amount = total_amount + gst_amount`.
	- Populate categorical fields (`pdf_inv_category`, `debtiCreditIndicator`, `process_status`) using weighted random choices so most rows are `processed`.
	- If `process_status == failed`, set a `failure_reason` from a small list.
	- Write the row as a CSV line using `csv.DictWriter` with a stable header order.

Testing and reproducibility

- Quick manual test:

```bash
python3 generate_sampledata.py --rows 5 --output tmp.csv --seed 123
cat tmp.csv
```

- Automated test idea: call the generator with a fixed seed and assert that the first row equals a known row string. Because the script uses only the `random` module and deterministic date math relative to `date.today()`, a stable test should set `base_date` injection or patch `date.today()`.

Extending and customization

- To change date ranges, GST rates, or amount ranges, modify the constants near the top of `generate_sampledata.py` or add new CLI flags to expose them.
- To add more realistic merchant/member distributions, replace uniform random generation with sampling from an input list or a small probability distribution.
- To produce other formats (JSON/Parquet), add a serializer function that converts row dicts to the desired format and an `--format` CLI flag.

Best practices followed

- Minimal external dependencies to ease portability.
- Reproducibility via seeds.
- Clear schema and documentation included in this README.
- Encapsulated row generation for testability and extension.

Contributing

If you'd like this generator to be extended (additional fields, CSV schema variants, JSON output, configurable distributions), open an issue or create a pull request with the change and tests.

License

This repository contains example code for internal use. Add a license file as appropriate for your project.

----

If you want, I can also:

- Add unit tests that assert deterministic output for a fixed seed.
- Add CLI flags for date ranges, GST rate choices, and failure-rate control.
- Add a `requirements.txt` or `pyproject.toml` if we introduce third-party dependencies.

Feel free to tell me which of the above you'd like next.
