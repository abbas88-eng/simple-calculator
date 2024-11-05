import streamlit as st

# Set up the Streamlit interface
st.title("Simple Calculator")

# Display instructions
st.write("Choose an operation and enter two numbers.")

# Operation selection
operation = st.selectbox("Select an operation:", ["Addition (+)", "Subtraction (-)", "Multiplication (*)", "Division (/)"])

# Input fields for the numbers
num1 = st.number_input("Enter the first number:", step=1.0)
num2 = st.number_input("Enter the second number:", step=1.0)

# Perform the calculation when the "Calculate" button is clicked
if st.button("Calculate"):
    # Determine the operation and calculate the result
    if operation == "Addition (+)":
        result = num1 + num2
        st.write(f"{num1} + {num2} = {result}")
    elif operation == "Subtraction (-)":
        result = num1 - num2
        st.write(f"{num1} - {num2} = {result}")
    elif operation == "Multiplication (*)":
        result = num1 * num2
        st.write(f"{num1} * {num2} = {result}")
    elif operation == "Division (/)":
        # Check for division by zero
        if num2 == 0:
            st.write("Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
            st.write(f"{num1} / {num2} = {result}")

# Prompt user to perform another calculation or exit
st.write("To perform another calculation, adjust the numbers or operation and click 'Calculate' again.")
