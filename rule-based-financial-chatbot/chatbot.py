import pandas as pd

# Load CSV
df = pd.read_csv("ex_data.csv")

# Clean column names
df.columns = df.columns.str.strip()

# Ensure correct data types (using YOUR typo)
cols = ['REVENUE', 'NET INCOME', 'TOTAL ASSETS',
        'TOTAL LIABILITES', 'OPERATING_CASH_FLOW']

for col in cols:
    df[col] = df[col].astype(str).str.replace(',', '')
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Fix YEAR formatting
df['YEAR'] = df['YEAR'].astype(int)

# Sort data
df = df.sort_values(['COMPANY', 'YEAR'])

# Calculate growth
df['Revenue Growth (%)'] = df.groupby('COMPANY')['REVENUE'].pct_change() * 100
df['Net Income Growth (%)'] = df.groupby('COMPANY')[
    'NET INCOME'].pct_change() * 100

# Fill NaN growth
df[['Revenue Growth (%)', 'Net Income Growth (%)']] = (
    df[['Revenue Growth (%)', 'Net Income Growth (%)']].fillna(0)
)

# ---------------- CHATBOT ---------------- #


def chatbot(query):
    query = query.lower()

    latest = df.sort_values('YEAR').groupby('COMPANY').tail(1)

    if "highest revenue" in query:
        company = latest.loc[latest['REVENUE'].idxmax(), 'COMPANY']
        return f"{company} has the highest revenue."

    elif "microsoft revenue" in query:
        revenue = latest[latest['COMPANY'] == "Microsoft"]['REVENUE'].values[0]
        return f"Microsoft's latest revenue is {revenue} million USD."

    elif "tesla net income" in query:
        tesla = df[df['COMPANY'] == "Tesla"]
        change = tesla.iloc[-1]['NET INCOME'] - tesla.iloc[-2]['NET INCOME']
        trend = "increased" if change > 0 else "decreased"
        return f"Tesla's net income has {trend} by {abs(change)} million USD."

    elif "apple and microsoft" in query:
        apple = latest[latest['COMPANY'] ==
                       "Apple"]['Revenue Growth (%)'].values[0]
        ms = latest[latest['COMPANY'] ==
                    "Microsoft"]['Revenue Growth (%)'].values[0]
        return f"Apple growth: {apple:.2f}%, Microsoft growth: {ms:.2f}%."

    else:
        return "Sorry, I can only answer predefined financial questions."


# Run chatbot
while True:
    user = input("Ask a question (type 'exit' to quit): ")
    if user.lower() == 'exit':
        print("Goodbye!")
        break
    print(chatbot(user))
