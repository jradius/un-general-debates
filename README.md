The UN General Debate Corpus is hosted in the Harvard Dataverse: https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/0TJX8Y

In the data/ directory you will find the original README.txt file detailing it's creators and licensing.

You will also find python scripts for transforming and building a complete dataset from the corpus and supporting dataset "Speakers_by_session.xlsx".
___

### UN General Debates Data Transformation Script
### ```transform_UNGDC.py```

This script contains a function that transforms the UN General Debate Corpus,
which includes transcripts of General Debate statements from 1946 to 2022, 
into a pandas DataFrame. 

It can be imported into notebooks to facilitate analysis,
or used as a stand-alone to generate a csv file.

```get_data(create_csv=False)```

    The data is located in a specific directory structure 'UNGDC_1946-2022\\TXT',
    with subfolders for each UN General Debate session/year containing the text files.
    Each text file's name is in the format 'country_session_year.txt'.

    The function reads each text file, extracts the country, session, and year from the
    filename, and stores these along with the file's content in a DataFrame.
    
     Args:
        create_csv (bool, optional): If True, the function will output a CSV file,
        rather than returning a Pandas DataFrame. 
        - Defaults to False.
    
    Returns:
        pd.DataFrame: A DataFrame containing the country, session, year, and
        text data from all text files in the UN General Debate Corpus.

<br>
This script needs to remain in the same directory as the UNGDC_1946-20* folder.
For example,<br><br>
UN General Debates<br>
|<br>
|-- UNGDC_1946-20* -> folder containing the UN General Debates Corpus<br>
|-- README.txt<br>
|-- Speakers_by_session.xlsx<br>
|-- transform_UNGDC.py -> this script<br>

__________________________________________________________
### UN General Debates Dataset Build Script
### ```build_dataset.py```

There are a few "gotchas" when transforming the corpus and cleaning the data.
This script takes care of all that. Running the script creates a csv file containing 
the full corpus dataset, complete with speaker and post. 

It uses the ```get_data()``` function (renamed to ```transform_UNGDC_data()``` for readability)
to transform the corpus into a dataframe and then joins it to the ```Speaker_by_session``` 
dataset. 

(I attempted to ```import transform_UNGDC```, but it fails for some reason - however, I was able to 
```import transform_UNGDC``` into a Jupyter Notebook successfully)

__________________________________________________________
#### <b><i>From the original README.txt:</i></b>

- The dataset contains the United Nations General Debate Corpus (UNGDC) covering the period 1946-2022.
	"UNGDC_1946-2022"

- There are 10,568 speeches in plain text format (UTF8). Speeches are structured by Year (Session). Each speech is named using the following convention: ISO 3166-1 alpha-3 country code, followed by the UN Session number, followed by year. E.g. USA_75_2020.txt.

- The collection also contains a file (Speakers_by_session.xlsx) recording names and posts of speakers in UN General Debates. Note: before 1994 the UN records do not consistently identify the posts of all speakers.

- When using the UNGDC data, please cite: 

Slava Jankin, Alexander Baturo, and Niheer Dasandi. "Words to Unite Nations: The Complete UN General Debate Corpus, 1946-Present." OSF working paper, https://osf.io/6kty4

AND 

Alexander Baturo, Niheer Dasandi, and Slava Mikhaylov, "Understanding State Preferences With Text As Data: Introducing the UN General Debate Corpus" Research & Politics, 2017.
__________________________________________________________