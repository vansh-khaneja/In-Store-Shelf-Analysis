# In-Sore Shelf Analysis 
This repository guides to develop a Store Shelf Analysing system that is capabable of counting the no. of object over the shelf along with checking that if all the products are arranged sequentially in a proper way or not. For this purpose I have used ```opencv``` for image processing and ```yolov8``` from [ultralytics](https://docs.ultralytics.com/modes/predict/) to detect the products here bottles in our case.

![Alt Text - description of the image](https://github.com/vansh-khaneja/In-Store-Shelf-Analysis/blob/main/cobined_output.png?raw=true)

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Execution](#execution)
- [Front-End](#front-end)
- [Contributors](#contributors)

## Execution

In this project, we used ultralytics ```yolov8``` model to detect the bottles placed over the shelf in a store for a defined area like shelf 1, shelf 2 etc. Then by fetching the cordinates of the bottles we are judging whether the bottles are placed sequentially or not.


## Features

- Fast and efficient 
- Best for Diet freaks 
- Text and Image multimodal searching
- Real-time Analysis

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/vansh-khaneja/In-Store-Shelf-Analysis
    cd In-Store-Shelf-Analysis
    ```

2. Set up the Python environment and install dependencies:

    ```sh
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3. Set up Qdrant:

    Login to [Qdrant Cloud](https://cloud.qdrant.io/) to get the api_key and url.
   
   ```sh
    qdrant_client = QdrantClient(
    url="https://xxxxxx-xxxxx-xxxxx-xxxx-xxxxxxxxx.us-east.aws.cloud.qdrant.io:6333",
    api_key="<your-api-key>",
    )
    ```
4. Run the ```data_upload.ipynb``` in jupyter notebook to setup and upload data in vector database.

5. Execute the ```main.py``` file by running this command to run the API.

    ```sh
    python main.py
    ```
    
![Alt Text - description of the image](https://github.com/vansh-khaneja/In-Store-Shelf-Analysis/blob/main/output1.png?raw=true)


## Contact
Feel free to ask any query at vanshkhaneja2004@gmail.com

Happy Coding :)



    
