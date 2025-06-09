import streamlit as st

# Title of the app
st.title('Simple Calculator')

# Input fields for numbers
a = st.number_input('Enter first number', value=0.0)
b = st.number_input('Enter second number', value=0.0)

# Dropdown for selecting operation
operation = st.selectbox('Select operation', ('Add', 'Subtract', 'Multiply', 'Divide'))

# Perform calculation based on selected operation
if operation == 'Add':
    result = a + b
elif operation == 'Subtract':
    result = a - b
elif operation == 'Multiply':
    result = a * b
elif operation == 'Divide':
    result = a / b if b != 0 else 'Infinity'

# Display the result
st.write('Result:', result)