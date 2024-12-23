import pandas as pd

def preprocess_finance_data(file_path):
    """
    Preprocess financial data: parse dates, normalize amounts, and categorize transactions.

    :param file_path: Path to the finance_data.csv file.
    :return: Cleaned DataFrame.
    """
    # Load data
    finance_df = pd.read_csv(file_path)

    # Parse date column
    finance_df['Date'] = pd.to_datetime(finance_df['Date'])

    # Normalize amounts (e.g., convert to absolute values for expenditure)
    finance_df['Amount'] = finance_df['Amount'].astype(float)

    # Add an "Income/Expense" column
    finance_df['Type'] = finance_df['Amount'].apply(lambda x: 'Income' if x > 0 else 'Expense')

    # Categorize transactions
    finance_df['Category'] = finance_df['Category'].str.capitalize()

    print("Finance data preprocessing complete.")
    return finance_df


def preprocess_medical_data(file_path):
    """
    Preprocess medical data: clean text fields and handle missing values.

    :param file_path: Path to the medical_data.csv file.
    :return: Cleaned DataFrame.
    """
    # Load data
    medical_df = pd.read_csv(file_path)

    # Remove leading/trailing spaces in text fields
    medical_df['Name'] = medical_df['Name'].str.strip()
    medical_df['Diagnosis'] = medical_df['Diagnosis'].str.strip()

    # Parse date column
    medical_df['DateOfVisit'] = pd.to_datetime(medical_df['DateOfVisit'])

    # Fill missing values in diagnosis with "Unknown"
    medical_df['Diagnosis'] = medical_df['Diagnosis'].fillna('Unknown')

    print("Medical data preprocessing complete.")
    return medical_df


if __name__ == "__main__":
    # Paths to CSV files
    finance_file = "finance_data.csv"
    medical_file = "medical_data.csv"

    # Preprocess data
    finance_df = preprocess_finance_data(finance_file)
    medical_df = preprocess_medical_data(medical_file)

    # Output preprocessed data for verification
    print("\nPreprocessed Finance Data:")
    print(finance_df)

    print("\nPreprocessed Medical Data:")
    print(medical_df)
