# Information Retrieval System

- **Author:** Samhitha Gouru
- **Student ID:** A20550016
- **github repo link:** https://github.com/SSP24SCM16G/Information-Retrieval
## Abstract
This project introduces an Information Retrieval (IR) system built using Python to facilitate efficient and accurate data search and retrieval from various web sources. The system combines Scrapy for automated web crawling, custom indexing mechanisms, and a Flask-based API for user interaction. Advanced text processing techniques, including vector space modeling and cosine similarity, are used to enhance the relevance of search results.

The primary objective of this project is to develop a scalable IR system that can handle extensive web data with high retrieval accuracy. The system aims to provide users with the ability to query and retrieve information quickly, catering to diverse informational needs across different domains.

Moving forward, the project will focus on expanding the dataset and improving the crawler's efficiency to cover a broader range of web sources. Enhancements in natural language processing techniques will be explored to improve the accuracy of the vector space model. Additionally, user interface improvements are planned to make the system more accessible and user-friendly. Ongoing performance optimization will ensure the system remains robust and responsive as it scales.

## Overview

The project develops an Information Retrieval (IR) system aimed at enhancing the efficiency and accuracy of online data search and retrieval. The solution integrates a web crawler, text indexing, and query processing functionalities into a cohesive system. The crawler gathers data from designated web sources, which is then indexed using a custom-developed text processing pipeline. User queries are processed through a Flask-based API, leveraging vector space modeling and cosine similarity for relevant document retrieval.

The proposed system consists of three main components:
1. **Web Crawler**: Utilizes Scrapy to efficiently harvest content from the internet, focusing on scalability and respecting site policies.
2. **Indexer**: Implements a text indexing framework that processes and stores data, preparing it for retrieval. This component uses natural language processing techniques to enhance data normalization and relevance.
3. **Query Processor**: A Flask web service that serves as the interface for user queries, employing a vector space model to compute and return the most relevant search results based on cosine similarity.

The system is designed to be modular, allowing for independent updates and scalability. Future enhancements will include the integration of machine learning algorithms for improved query understanding and response accuracy.

## Design

The IR system is engineered to perform comprehensive web crawling, precise text indexing, and efficient query processing. It supports advanced text processing techniques to enhance data normalization and search relevance. The system can handle complex queries and return results based on semantic similarities, ensuring a high degree of accuracy and relevance.

Users interact with the system through a user-friendly Flask-based API, which receives queries and returns search results. The API is designed to be intuitive, allowing users to easily input their search criteria and receive relevant information swiftly.

The components of the system—crawler, indexer, and query processor—are tightly integrated to ensure seamless data flow and processing. The modular architecture allows for individual component upgrades without disrupting overall system functionality. This integration supports scalability, facilitating future enhancements such as the incorporation of machine learning algorithms for improved data interpretation and retrieval.

## Architecture

### Software Components

The IR system comprises three primary software components:

1. **Web Crawler**: Built with Scrapy, this component autonomously navigates and extracts data from the web, adhering to site-specific protocols and policies.
2. **Indexer**: Utilizes custom Python classes for text processing, normalization, and indexing, preparing the data for efficient retrieval.
3. **Query Processor**: Operates through a Flask-based API, implementing a vector space model with cosine similarity to evaluate and rank the relevance of documents to user queries.

### Interfaces

The system interfaces include:

- A RESTful API provided by the Flask framework, which serves as the main interaction point for users to submit queries and receive responses.
- Internal interfaces between the crawler, indexer, and query processor ensure data consistency and facilitate seamless data exchange and processing.

### Implementation

- To implement and execute the system, start by pulling the latest code from the Git repository using the command `git pull origin master`. After updating the code, run the `python main.py` command to initiate the system.
- Once the system starts, the crawler activates and begins fetching web documents. It's important to ensure that the crawler runs until it reaches the designated maximum page limit to gather adequate data for processing.
- During the crawling phase, continually monitor the progress to verify that web pages are being scraped effectively up to the maximum depth set in the crawler’s configuration.
- After the crawling is complete, the system will prompt the user in the terminal to "Enter the search query". Following this input, the system processes the query and displays results based on cosine similarity. It lists document names, links, and cosine scores in descending order, showcasing the effectiveness and precision of the retrieval process.

## Operation

### Software Commands

- To start the system, run the command `python main.py`. This initiates the main application, activating the crawler and setting up the indexing and query processing components.

### Inputs

- During operation, the system prompts the user in the terminal to "Enter the search query". The user needs to input their query directly into the terminal, which the system then processes to find and return relevant documents based on cosine similarity.

### Installation

- Before operating the system, ensure that all required dependencies are installed. This typically involves installing Python packages such as Scrapy for web crawling and Flask for the web service. Use the command `pip install -r requirements.txt` to install all necessary Python packages listed in a requirements file.
- Additionally, if not already configured, set up the Python environment suitable for running the application, ensuring that all paths and necessary configurations are correctly established.

### Flow

- Pull the latest version of the project files from the GitHub repository.
- Open the downloaded files using Visual Studio Code to access and edit the project.
- Navigate to the terminal within Visual Studio Code.
- Execute the command `python main.py` to start the system. This initiates data collection with all collected data being saved as JSON files in the data directory.
- After data collection, the terminal will prompt you to "Enter your query".
- Enter a query.
- The system processes the query and displays results in the terminal. The results include document titles, links, and their cosine similarity scores, all presented in descending order of relevance.

## Conclusion

### Success/Failure Results

- The system has successfully demonstrated the ability to autonomously crawl web pages, index the collected data, and retrieve information based on user queries. It effectively ranks and displays results according to relevance, utilizing cosine similarity scores.
- Failures, if any, typically arise from limitations in the crawler's scope or issues with web page accessibility, which can prevent the system from fetching or processing some data correctly.

### Caveats/Cautions

- Users should be aware of the system's dependency on the proper configuration of the crawling parameters (like max_allowed_pages and max_allowed_depth) to avoid overloading servers or violating website terms of use.
- The accuracy of search results can be impacted by the quality and preprocessing of the indexed data. Improper handling of data normalization and vectorization may lead to less accurate results.
- It's essential to maintain the software components updated and monitor their interactions to ensure optimal performance and avoid potential breakdowns during operations.

### Outputs

- The system outputs are displayed directly in the terminal, providing a list of the most relevant documents to the user's query. Each entry includes the document title, a link, and its cosine similarity score, which quantifies the relevance to the entered query.
- Search Query: steps
  <p align="center">
    <img width="372" alt="image" src="https://github.com/SSP24SCM16G/Information-Retrieval/assets/159294382/a81f35a7-6109-4237-b963-26f7966af7a5">
  </p>

- Search query: gum
  <p align="center">
    <img width="418" alt="image" src="https://github.com/SSP24SCM16G/Information-Retrieval/assets/159294382/1844ea31-33e0-43e9-aa8d-7e2c180b1cce">
  </p>

- Search query: Not all of us can do great things. But we can do small things with great love
  <p align="center">
    <img width="401" alt="image" src="https://github.com/SSP24SCM16G/Information-Retrieval/assets/159294382/5bf5f629-1500-47a7-8789-c649ee2d5446">
  </p>

- Search query: information on friendship
  <p align="center">
    <img width="394" alt="image" src="https://github.com/SSP24SCM16G/Information-Retrieval/assets/159294382/9f5cc70e-1a90-4f13-8064-49861b0d9227">
  </p>

- Search query: iam samhitha gouru
  <p align="center">
    <img width="417" alt="image" src="https://github.com/SSP24SCM16G/Information-Retrieval/assets/159294382/3f032625-3455-44d9-9870-18ea00af4e5f">
  </p>

- Search query: books
  <p align="center">
    <img width="451" alt="image" src="https://github.com/SSP24SCM16G/Information-Retrieval/assets/159294382/455eb5b6-20b6-4f72-bc25-5cfece7b6226">
  </p>
## Data Sources

- **Web Links:** [WikiHow Main Page](https://www.wikihow.com/Main-Page)
  - The system's crawler is configured to target specific web pages or a range of websites, depending on the project requirements. These sources are selected based on their relevance and richness of content necessary for the system's purpose.

- **Downloads:**
  - Data is automatically downloaded by the crawler in the form of web pages, which are then processed and stored as JSON files in the data directory. This ensures that all necessary information is retained and available for indexing and retrieval.

- **Access Information:**
  - The data collected and stored locally is accessible exclusively through the system’s querying interface. Users can interact with this data by entering search queries directly into the terminal, which processes and displays the relevant information.
  - There are no external databases or additional online storage used in this setup, making the system self-contained and independent, provided it has initial access to the internet for crawling purposes.

- **Created JSON Files:**
  - JSON files storing the data are available at the following location:
    [Data Directory](https://github.com/SSP24SCM16G/Information-Retrieval/tree/main/IR_Project/crawler/data)

<img width="342" alt="image" src="https://github.com/SSP24SCM16G/Information-Retrieval/assets/159294382/121e1bdf-fbe8-4c26-9058-4d627365138d" style="display: block; margin: 0 auto;">

## Source Code

Indexer2:


<img width="402" alt="image" src="https://github.com/SSP24SCM16G/Information-Retrieval/assets/159294382/b82813dd-8399-4644-ba0b-d5daf40d5be7">

Indexer2:

<img width="402" alt="image" src="https://github.com/SSP24SCM16G/Information-Retrieval/assets/159294382/d1fcb6e9-0a4d-4b3c-b794-e1b65d807100">

Indexer:

<img width="408" alt="image" src="https://github.com/SSP24SCM16G/Information-Retrieval/assets/159294382/706fce22-e0e5-480b-8f59-9f1476893a87">

Main.py:

<img width="408" alt="image" src="https://github.com/SSP24SCM16G/Information-Retrieval/assets/159294382/b9865fbf-b154-4c96-b436-36e5fd06f5f4">


## Coverage

Test coverage is comprehensively managed to encompass all critical functionalities of the system. This includes:

- **Crawler Coverage:** Tests ensure that the crawler adheres to set limits like `max_allowed_pages` and `max_allowed_depth`, correctly handles different types of web pages, and respects `robots.txt` rules.

- **Indexer Coverage:** Checks that all expected types of data are correctly processed, normalized, and indexed without errors.

- **Query Processor Coverage:** Ensures that the system correctly processes queries, calculates cosine similarity accurately, and returns the correct order of results based on relevance.

- **Integration Coverage:** Validates the seamless interaction between the crawler, indexer, and query processor to ensure data flows correctly through all stages from collection to retrieval.


- <img width="385" alt="image" src="https://github.com/SSP24SCM16G/Information-Retrieval/assets/159294382/a0e590e2-9187-4104-a23d-2aa64fbc54d9">


- <img width="378" alt="image" src="https://github.com/SSP24SCM16G/Information-Retrieval/assets/159294382/e3256b0f-7195-4311-863a-878fc4ce656a">


- <img width="371" alt="image" src="https://github.com/SSP24SCM16G/Information-Retrieval/assets/159294382/1ac1a62b-4705-43cb-8b18-a2de88876afa">

## References

[1] F. Yin, X. He, and Z. Liu, "Research on Scrapy-Based Distributed Crawler System for Crawling Semi-structured Information at High Speed," 2018 IEEE 4th International Conference on Computer and Communications (ICCC), Chengdu, China, 2018, pp. 1356-1359. [Online]. Available: [DOI](https://doi.org/10.1109/CompComm.2018.8781062).

[2] Z. Yao, W. Daling, F. Shi, Z. Yifei, and L. Fangling, "An Approach for Crawling Dynamic WebPages Based on Script Language Analysis," 2012 Ninth Web Information Systems and Applications Conference, Haikou, China, 2012, pp. 35-38. [Online]. Available: [DOI](https://doi.org/10.1109/WISA.2012.34).

[3] B. Bhardwaj, S. I. Ahmed, J. Jaiharie, R. Sorabh Dadhich, and M. Ganesan, "Web Scraping Using Summarization and Named Entity Recognition (NER)," 2021 7th International Conference on Advanced Computing and Communication Systems (ICACCS), Coimbatore, India, 2021, pp. 261-265. [Online]. Available: [DOI](https://doi.org/10.1109/ICACCS51430.2021.9441888).

[4] S. Irfan and S. Ghosh, "Ranking Web Pages Using Cosine Similarity Measure," 2019 International Conference on Computing, Power and Communication Technologies (GUCON), New Delhi, India, 2019, pp. 867-870. [Online]. Available: [DOI](https://doi.org/10.1109/GUCON46384.2019.9033736).

[5] K. Mahmoud, H. Ismail, and M. Kholief, "ROEF: A Smart Search Engine of the 3rd Generation World Wide Web (WWW)," 2015 25th International Conference on Computer Theory and Applications (ICCTA), Alexandria, Egypt, 2015, pp. 118-125. [Online]. Available: [DOI](https://doi.org/10.1109/ICCTA37466.2015.9513436).

[6] A. I. Kadhim, "Term Weighting for Feature Extraction on Twitter: A Comparison Between BM25 and TF-IDF," 2019 International Conference on Advanced Science and Engineering (ICOASE), Zakho - Duhok, Iraq, 2019, pp. 124-128. [Online]. Available: [DOI](https://doi.org/10.1109/ICOASE.2019.8723825).

[7] Y. Hong, J. Vaidya, and H. Lu, "Search Engine Query Clustering Using Top-k Search Results," 2011 IEEE/WIC/ACM International Conferences on Web Intelligence and Intelligent Agent Technology, Lyon, France, 2011, pp. 112-119. [Online]. Available: [DOI](https://doi.org/10.1109/WI-IAT.2011.224).
