import streamlit as st
import pandas as pd
import random

# Load your DataFrame
# Replace 'your_data.csv' with the actual path to your Excel file
df = pd.read_excel('Book1.xlsx')  # !pip install openpyxl

# Define a function to get random words based on selected lists
def get_random_words(selected_lists):
    selected_words = {selected_list: [] for selected_list in selected_lists}
    for selected_list in selected_lists:
        if selected_list == 'B2 List 1':
            selected_words[selected_list].extend(random.sample(df['b2_list1'].dropna().tolist(), 15))
        elif selected_list == 'B2 List 2':
            selected_words[selected_list].extend(random.sample(df['b2_list2'].dropna().tolist(), 15))
        elif selected_list == 'B1 List 1':
            selected_words[selected_list].extend(random.sample(df['b1_list1'].dropna().tolist(), 15))
        elif selected_list == 'B1 List 2':
            selected_words[selected_list].extend(random.sample(df['b1_list2'].dropna().tolist(), 15))
        elif selected_list == 'C1 List 1':
            selected_words[selected_list].extend(random.sample(df['first_list'].dropna().tolist(), 15))
        elif selected_list == 'C1 List 2':
            selected_words[selected_list].extend(random.sample(df['second_list'].dropna().tolist(), 15))
        elif selected_list == 'A2 List 1':
            selected_words[selected_list].extend(random.sample(df['a2_list1'].dropna().tolist(), 15))
        elif selected_list == 'A1 List 1':
            selected_words[selected_list].extend(random.sample(df['a1_list1'].dropna().tolist(), 15))
        elif selected_list == 'Verbs':
            selected_words[selected_list].extend(random.sample(df['verbs'].dropna().tolist(), 15))
    return selected_words

# Create a Streamlit app
def main():
    st.set_page_config(layout="wide") 
    st.title('German Word Display App')
    # st.markdown("----------------")
    st.markdown('#### Click reload for new words')

    # Add select options for choosing lists
    selected_lists = st.multiselect('Select Lists to Display', 
                                    ['B2 List 1', 'B2 List 2', 'B1 List 1', 'B1 List 2', 'C1 List 1', 'C1 List 2', 'A2 List 1', 'A1 List 1', 'Verbs'],
                                    default=['B2 List 1', 'C1 List 1'])

    # Get random words based on selected lists
    selected_words = get_random_words(selected_lists)

    # Add a page reload button
    if st.button('Reload Page'):
        st.experimental_rerun()

    num_columns = len(selected_lists)  # Number of columns matches the number of selected lists
    columns = st.columns(num_columns)

    for i, selected_list in enumerate(selected_lists):
        with columns[i]:
            st.subheader(f'{selected_list}:')
            for j, word in enumerate(selected_words[selected_list]):
                st.write(f"{j+1}. {word}")
            
    st.markdown("----------------")

if __name__ == "__main__":
    main()
