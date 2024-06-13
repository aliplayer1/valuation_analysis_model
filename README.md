# DCF Model

This project parses PDF documents containing financial statements of a company and produces common financial metrics used to analyze the valuation using the discounted cash flow (DCF) model.

## Directory Structure

DCF_Model/
├── main.py
├── cli.py
├── dcf_calculations.py
├── extract_pdf.py
├── parse_financials.py
├── tsla-20240331.pdf
└── .gitignore

## Usage

To run the script, navigate to the project directory and use the following command:

```sh
python3 cli.py tsla-20240331.pdf --discount_rate 0.1 --growth_rate 0.15 --projection_years 5
```

## Files

__main__.py: Entry point for the application.
cli.py: Handles the command-line interface.
dcf_calculations.py: Calculates the DCF value.
extract_pdf.py: Extracts text from PDF files.
parse_financials.py: Parses financial data from extracted text.
.gitignore: Specifies files and directories to be ignored by Git.
tsla-20240331.pdf: Sample PDF file for testing.

## Installation

To install the required dependencies, use:

```sh
pip install pymupdf pandas
```

## Example

Here is an example of how to run the program:

```sh
python3 cli.py tsla-20240331.pdf --discount_rate 0.1 --growth_rate 0.15 --projection_years 5
```

This command will parse the provided PDF file, extract financial data, calculate financial metrics, and output the discounted cash flow (DCF) valuation.