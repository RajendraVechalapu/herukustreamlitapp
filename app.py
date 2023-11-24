# simple_addition_app.py

import streamlit as st

def add_numbers(num1, num2):
    """Function to add two numbers."""
    result = num1 + num2
    return result

def main():
    # Streamlit app title
    st.title("Simple Addition App")

    # Input for the first number
    num1 = st.number_input("Enter the first number:")

    # Input for the second number
    num2 = st.number_input("Enter the second number:")

    # Call the add_numbers function
    result = add_numbers(num1, num2)

    # Display the result
    st.write(f"The result of {num1} + {num2} is: {result}")

# Check if the script is being run directly
if __name__ == "__main__":
    # Call the main function to run the Streamlit app
    main()
