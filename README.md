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

- Fast and efficient method
- Optimizable to increase accuarcy
- Uses `yolov8n` model
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

3. You can also change the model based on the use case. Here in this project we have used ```yolov8n.pt``` model. Please refer [Ultraytics documentation](https://docs.ultralytics.com/models/yolov8/#supported-tasks-and-modes) for learning about different model sizes. You can change the model here.
   
    ```sh
    from ultralytics import YOLO
    model = YOLO("yolov8n.pt")
    
    ```

4. Execute the ```main.py``` file by running this command to run the API.

    ```sh
    python main.py
    ```
    
![Alt Text - description of the image](https://github.com/vansh-khaneja/In-Store-Shelf-Analysis/blob/main/output1.png?raw=true)


## Contact

For any questions or issues, feel free to open an issue on this repository or contact me at vanshkhaneja2004@gmail.com.

Happy coding!
    
