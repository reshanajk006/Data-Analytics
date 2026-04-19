Financial Chatbot Project

Overview:
This project analyzes financial data from Microsoft, Tesla, and Apple for the last three years. Based on this data, a simple rule-based chatbot was built to answer predefined financial queries.

Files Included:
- data_analysis.ipynb : Contains data cleaning, processing, and analysis
- chatbot.py : Python script for the chatbot
- ex_data.csv : Dataset used for analysis
- README.txt : Project documentation

Features:
- Extracts key financial metrics:
  Revenue, Net Income, Total Assets, Total Liabilites, Operating Cash Flow
- Calculates year-over-year growth:
  Revenue Growth (%), Net Income Growth (%)
- Chatbot responds to predefined queries such as:
  - Highest revenue company
  - Microsoft revenue
  - Tesla net income trend
  - Apple vs Microsoft growth comparison

How to Run:
1. Make sure Python is installed
2. Install pandas:
   pip install pandas
3. Keep ex_data.csv in the same folder as chatbot.py
4. Run:
   python chatbot.py
5. Type queries in terminal (type 'exit' to quit)

Limitations:
- Only supports predefined queries
- No NLP or advanced AI used
- Limited to available dataset

Conclusion:
The project shows how financial data can be structured and used in a simple chatbot. Microsoft shows strong growth, Apple is stable, and Tesla shows fluctuations.
