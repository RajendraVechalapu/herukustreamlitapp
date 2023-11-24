import streamlit as st
import datetime
import random

def calculator():
    st.title("Simple Calculator")

    # Get user input for two numbers
    num1 = st.number_input("Enter the first number:", step=1.0)
    num2 = st.number_input("Enter the second number:", step=1.0)

    # Choose operation
    operation = st.radio("Select an operation", ["Addition", "Subtraction", "Multiplication", "Division"])

    # Perform calculation based on the selected operation
    if operation == "Addition":
        result = num1 + num2
    elif operation == "Subtraction":
        result = num1 - num2
    elif operation == "Multiplication":
        result = num1 * num2
    elif operation == "Division":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Cannot divide by zero"

    # Display the result
    st.write(f"Result of {operation}: {result}")

    # Add a button to display a funny quote with timestamp when clicked
    if st.button("Click for a Funny Quote"):
        display_funny_quote()

def display_funny_quote():
    # List of funny quotes
    funny_quotes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "I told my wife she should embrace her mistakes. She gave me a hug.",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "I'm reading a book on anti-gravity. It's impossible to put down!",
        "Why don't skeletons fight each other? They don't have the guts.",
    ]

    # Select a random funny quote
    quote = random.choice(funny_quotes)

    # Display the funny quote with a timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.write(f"\n\n{quote}\n\nTimestamp: {timestamp}")

if __name__ == "__main__":
    calculator()
