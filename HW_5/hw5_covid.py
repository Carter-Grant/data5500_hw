import requests
import json
from datetime import datetime
from collections import defaultdict

# Load and read state codes from the text file
with open('C:/Users/carte/OneDrive/Documents/GitHub/data5500_hw/HW_5/states_territories.txt') as f:
    
    states = [line.strip() for line in f.readlines()]

# Function to fetch COVID data for a specific state
def fetch_covid_data(state):
    url = f'https://api.covidtracking.com/v1/states/{state}/daily.json'
    response = requests.get(url)
    # Return the JSON response as a Python dictionary
    return response.json()

# Function to analyze the COVID data and do calculations 
def analyze_data(data):
    new_cases = []  # List to store daily new cases
    monthly_new_cases = defaultdict(int)  # Dictionary to store monthly new cases

    highest_new_cases = 0  # Variable to track the highest # of new cases
    date_highest_new_cases = ""  # Variable to store the date of the highest new cases
    most_recent_no_cases_date = ""  # Variable to store the most recent date with no new cases

    # Iterate over each entry in the data
    for entry in data:
        date = entry['date'] 
        positive_increase = entry['positiveIncrease'] 
        new_cases.append(positive_increase)  

# Calculate monthly new cases
        date_str = str(entry['date'])  
        date_obj = datetime.strptime(date_str, '%Y%m%d')  # Convert string to datetime object
        month_key = date_obj.strftime('%Y-%m')  # Get the month as a key (YYYY-MM)
        monthly_new_cases[month_key] += entry['positiveIncrease']  # Sum new cases for the month

        # Check for highest new cases
        if positive_increase > highest_new_cases:
            highest_new_cases = positive_increase  # Update the highest new cases
            date_highest_new_cases = date_obj  # Update the date of highest new cases

        # Check for most recent date with no new cases
        elif positive_increase == 0:
            most_recent_no_cases_date = date_obj  # Update the most recent date with no new cases

    # Calculate the average new cases over the dataset
    average_new_cases = sum(new_cases) / len(new_cases) if new_cases else 0

    # Determine the month with highest and lowest new cases
    highest_month = max(monthly_new_cases.items(), key=lambda x: x[1])[0] if monthly_new_cases else None
    lowest_month = min(monthly_new_cases.items(), key=lambda x: x[1])[0] if monthly_new_cases else None

    # Return the results as a dictionary
    return {
        "average_new_cases": average_new_cases,
        "date_highest_new_cases": date_highest_new_cases.strftime('%Y-%m-%d') if date_highest_new_cases else None,
        "highest_new_cases_value": highest_new_cases,
        "most_recent_no_cases_date": most_recent_no_cases_date.strftime('%Y-%m-%d') if most_recent_no_cases_date else None,
        "highest_month": highest_month,
        "lowest_month": lowest_month
    }
def save_data_to_json(state, data):
    file_path = f'C:/Users/carte/OneDrive/Documents/GitHub/data5500_hw/HW_5/{state}.json'
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file)
# Main function
def main():
    # Iterate through each state to fetch and analyze data
    for state in states:
        data = fetch_covid_data(state) 
        analysis = analyze_data(data)  
        
        # Output results
        print("Covid confirmed cases statistics\n")
        print(f"State name: {state.upper()}")
        print(f"Average number of new daily confirmed cases: {analysis['average_new_cases']:.2f}")
        print(f"Date with the highest new number of covid cases: {analysis['date_highest_new_cases']} (New cases: {analysis['highest_new_cases_value']})")
        print(f"Most recent date with no new covid cases: {analysis['most_recent_no_cases_date']}")
        print(f"Month with the highest new number of covid cases: {analysis['highest_month']}")
        print(f"Month with the lowest new number of covid cases: {analysis['lowest_month']}\n")

# Entry point for the program
if __name__ == "__main__":
    main()  # Call the main function to execute the program

