"""
This script needs to remain in the same directory as the UNGDC_1946-20* folder.
For example,
    UN General Debates
    |
    |-- UNGDC_1946-20* -> folder containing the UN General Debates Corpus
    |-- README.txt
    |-- Speakers_by_session.xlsx
    |-- transform_UNGDC.py -> this script

See README.txt for more information about the data; original authors, license, etc.
Source: https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/0TJX8Y
"""

import os
import glob
import pandas as pd


def transform_UNGDC_data():
    """
    This function creates a pandas DataFrame from the UN General Debate Corpus,
    which includes transcripts of General Debate statements from 1946 to 2022,
    held during the annual sessions of the United Nations General Assembly.

    The data is located in a specific directory structure 'UNGDC_1946-2022\\TXT',
    with subfolders for each UN General Debate session/year containing the text files.
    Each text file's name is in the format 'country_session_year.txt'.

    The function reads each text file, extracts the country, session, and year from the filename,
    and stores these along with the file's content in a DataFrame.

    Returns:
        pd.DataFrame: A DataFrame containing the country, session, year, and
        text data from all text files in the UN General Debate Corpus.
    """

    # Initialize an empty list to store the data
    data = []

    # Define directory pattern
    directory_pattern = os.path.join('UNGDC_1946-20*', 'TXT', '*', '*.txt')

    # Loop through each text file in the directory
    for filename in glob.glob(directory_pattern):
        # Extract country, session, and year from the filename
        basename = os.path.basename(filename)  # Get the filename with extension
        country, session, year = os.path.splitext(basename)[0].split('_')  # Remove extension and split

        # Open the file and read the text
        with open(filename, 'r', encoding="utf-8") as file:
            text = file.read()

        # Append the data to the list
        data.append({'country': country, 'session': session, 'year': year, 'text': text})

    # Create a DataFrame from the list
    result = pd.DataFrame(data)

    return result

# Read and clean corpus dataset
corpus = transform_UNGDC_data()
corpus['year'] = corpus['year'].astype(int)
corpus['session'] = corpus['session'].astype(int)

# Read and clean Speakers_by_session dataset
column_names = ['year', 'session', 'country', 'country_name', 'speaker', 'post']
speakers = pd.read_excel('Speakers_by_session.xlsx', skiprows=1, usecols=range(6), names=column_names, index_col=False)

# Merge both datasets to get the full UN General Debates corpus
corpus = pd.merge(speakers, corpus, how='right', on=['year', 'session', 'country'])

corpus.to_csv('UNGDC_1946-2022.csv', index=False)