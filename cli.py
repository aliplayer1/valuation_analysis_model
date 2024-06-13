import argparse
from extract_pdf import extract_text_from_pdf
from parse_financials import parse_financial_data, calculate_financial_metrics
from dcf_calculations import calculate_dcf

def main():
    parser = argparse.ArgumentParser(description="Parse PDF financial statements and calculate DCF valuation.")
    parser.add_argument("pdf_path", type=str, help="Path to the PDF file containing financial statements.")
    parser.add_argument("--discount_rate", type=float, default=0.1, help="Discount rate for DCF calculation.")
    parser.add_argument("--growth_rate", type=float, default=0.02, help="Growth rate for future cash flows.")
    parser.add_argument("--projection_years", type=int, default=5, help="Number of years to project future cash flows.")
    
    args = parser.parse_args()
    
    pdf_path = args.pdf_path
    discount_rate = args.discount_rate
    growth_rate = args.growth_rate
    projection_years = args.projection_years
    
    text = extract_text_from_pdf(pdf_path)
    financial_data = parse_financial_data(text)
    
    if not financial_data:
        print("No financial data found in the PDF.")
        return
    
    financial_metrics = calculate_financial_metrics(financial_data)
    dcf_value = calculate_dcf(financial_data, discount_rate, growth_rate, projection_years)
    
    print("\nFinancial Data Extracted:")
    for key, value in financial_data.items():
        print(f"{key}: ${value:.2f}")
    
    print("\nCommon Financial Metrics:")
    for key, value in financial_metrics.items():
        print(f"{key}: ${value:.2f}")
    
    print(f"\nDCF Valuation: ${dcf_value:.2f}")

if __name__ == "__main__":
    main()
