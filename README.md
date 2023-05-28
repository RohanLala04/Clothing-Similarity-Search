# Clothing Similarity Search
## Overview
This project aims to create a machine learning model that can receive a text describing a clothing item and return a ranked list of links to similar items from different websites. The solution is implemented as a function deployed on Google Cloud Functions, which accepts a text string and returns JSON responses with ranked suggestions.
## Dataset Collection and Preprocessing
The dataset of clothing item descriptions is collected using web scraping techniques with Selenium and BeautifulSoup from four different clothing brand websites: Zara, Pepe Jeans, H&M, and Levi's. Each website is crawled using Selenium to extract the relevant information, including product titles and links.

The collected data is preprocessed to clean and format the text data. Numerical values and unwanted characters are removed from the "Product_Description" column of the dataset. Finally, the cleaned data is combined from the individual CSV files into a single CSV file.
## Similarity Measurement
To measure similarity between the input text and the clothing items in the dataset, the spaCy library is used. The English language model for spaCy, 'en_core_web_sm', is loaded. The function '**extract_features_lemma**' is created to extract lemma features from the input text. These features are then used to compute similarity scores using cosine similarity.
## Ranking and Result Generation
The Flask route '**get_similar_items**' handles the request and returns similar items based on the input text. The function first reads the preprocessed dataset from the CSV file. Lemma features are extracted from the product descriptions using the '**extract_features_lemma**' function. Cosine similarity scores are computed between the input text and the dataset.

The top N indices with the highest similarity scores are retrieved, and the corresponding product links are extracted. The result is formatted as a JSON response containing the ranked links.
## Deployment Instructions
To deploy the function on Google Cloud Functions, follow these steps:
1. Package the code and required files:
  * Include the '**main.py**' file containing the function code.
  * Include the '**clothing-final.csv**' file, which contains the preprocessed dataset.
  * Create a '**requirements.txt**' file listing the Python packages required by the function.
  * Zip the code and required files into a single archive.
2. Open the Google Cloud Console and navigate to the Cloud Functions section.
3. Create a new function and provide the following details:
  * Set the function region, trigger type, and memory allocation according to your requirements.
  * Set the runtime to the Python version used in your function.
  * Specify the entry point as the Python function to be called first during execution (in this case, '**get_similar_items**').
  * Choose the "Source code" option and select "Upload zip" to upload the archive containing the code and files.
4. Configure any necessary environment variables or additional settings for your function.
5. Deploy the function and wait for the deployment process to complete.

Once deployed, you can test the function by sending a JSON payload with the desired input text to receive JSON responses with ranked suggestions.

## Evaluation
The project has been completed successfully, including the dataset collection and preprocessing, similarity measurement, ranking and result generation, as well as deployment steps. The performance of the project can be evaluated based on its ability to provide accurate and relevant ranked suggestions for similar clothing items.
## Documentation and Code
The code is organized into different files and folders. The Google Cloud Function folder contains the '**clothing-final.csv**', '**main.py**', and '**requirements.txt**' files. The '**main.py**' file is responsible for running the function and generating ranked suggestions. The '**clothing-final.csv**' file contains the combined and cleaned dataset. The '**requirements.txt**' file lists the Python packages required by the function.

The Web Scraping and Dataset Collection folder contains the web scraping scripts and the collected CSV files. 

The code is thoroughly commented to explain the purpose of each section and provide clarity. Relevant comments and documentation within the code help understand its functionality.
## License
This project is licensed under the **MIT License**.

Feel free to explore, modify, and use the code according to the terms of the license. Contributions are also welcome.
