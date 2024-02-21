import streamlit as st
import pandas as pd
import numpy as np
from prediction import predict

import streamlit as st
from prediction import predict  # assuming predict function is defined in prediction.py

st.title('Chat Bot')

st.header("Enter your message below:")
user_input = st.text_input("You:", "")

if st.button("Send"):
    if user_input.strip() != "":
        # Assuming predict function takes user input and returns a response
        response = predict(user_input)
        st.text("Bot: " + response)
    else:
        st.warning("Please enter a message.")

st.text('')
st.text('')
st.markdown(
    '`Created by` [CPINS](https://google.com) | \
         `Code:` [GitHub](https://github.com/)')