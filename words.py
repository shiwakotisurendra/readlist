import streamlit as st
import pandas as pd
import random

# Load your DataFrame
# Replace 'your_data.csv' with the actual path to your CSV file
df = pd.read_excel('Book1.xlsx')  # !pip install openpyxl

# Define a function to get 50 random B2 and C1 German words
def get_random_words():
    b2_words = random.sample(df['first_list'].tolist(), 15)
    c1_words = random.sample(df['second_list'].tolist(), 15)
    b2_words1 = random.sample(df['b2_list1'].dropna().tolist(), 15)
    b2_words2 = random.sample(df['b2_list2'].dropna().tolist(), 15)
    b1_words1 = random.sample(df['b1_list1'].dropna().tolist(), 15)
    b1_words2 = random.sample(df['b1_list2'].dropna().tolist(), 15)
    return b2_words, c1_words,b2_words1,b2_words2,b1_words1,b1_words2

# Create a Streamlit app
def main():
    st.set_page_config(layout="wide") 
    st.title('German Word Display App')
    # st.markdown("----------------")
    st.markdown('#### Click reload for new words')

    # Get random words
    b2_words, c1_words,b2_words1,b2_words2,b1_words1,b1_words2 = get_random_words()


    # Add a page reload button
    if st.button('Reload Page'):
        st.experimental_rerun()

    
    num_columns = 3  # You can adjust the number of columns as needed
    col1, col2,col3,col4,col5,col6 = st.columns([1,1,1,1,1,1])
    with col1:
            # Display B2 words in multiple columns
        st.subheader('C1 German List1:')
        # b2_columns = st.columns(3)
        for i, word in enumerate(b2_words):
            # b2_columns[i % num_columns].write(f"{i+1}. {word}")
            st.write(f"{i+1}. {word}")
            
    with col2:
        # Display C1 words in multiple columns
        st.subheader('C1 German List2:')
        # c1_columns = st.columns(num_columns)
        # c1_columns = st.columns(3)
        for i, word in enumerate(c1_words):
            # c1_columns[i % num_columns].write(f"{i+1}. {word}")
            st.write(f"{i+1}. {word}")
    
    with col3:
        # Display C1 words in multiple columns
        st.subheader('B2 German List1:')
        # c1_columns = st.columns(num_columns)
        # b1_column1 = st.columns(3)
        for i, word in enumerate(b2_words1):
            # b1_column1[i % num_columns].write(f"{i+1}. {word}")
            st.write(f"{i+1}. {word}")
            
    with col4:
        # Display C1 words in multiple columns
        st.subheader('B2 German List2:')
        # c1_columns = st.columns(num_columns)
        # b1_column2 = st.columns(3)
        for i, word in enumerate(b2_words2):
            # b1_column2[i % num_columns].write(f"{i+1}. {word}")
            st.write(f"{i+1}. {word}")
            
    with col5:
        # Display C1 words in multiple columns
        st.subheader('B1 German List1:')
        # c1_columns = st.columns(num_columns)
        # b1_column2 = st.columns(3)
        for i, word in enumerate(b1_words1):
            # b1_column2[i % num_columns].write(f"{i+1}. {word}")
            st.write(f"{i+1}. {word}")
            
    with col6:
        # Display C1 words in multiple columns
        st.subheader('B1 German List2:')
        # c1_columns = st.columns(num_columns)
        # b1_column2 = st.columns(3)
        for i, word in enumerate(b1_words2):
            # b1_column2[i % num_columns].write(f"{i+1}. {word}")
            st.write(f"{i+1}. {word}")
    st.markdown("----------------")

if __name__ == "__main__":
    main()