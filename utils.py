import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("sample.png")
resize = cv2.resize(image, (1000, 600))
def shelf_coordinates(image):
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    adaptive_thresh = cv2.adaptiveThreshold(gray, 255, 
                                             cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                             cv2.THRESH_BINARY_INV, 11, 2)
    shelf_coords =[]
    kernel = np.ones((5, 5), np.uint8)
    morphed = cv2.morphologyEx(adaptive_thresh, cv2.MORPH_CLOSE, kernel)

    edges = cv2.Canny(morphed, 50, 150)

    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, threshold=100, minLineLength=100, maxLineGap=10)

    detected_lines = []

    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            detected_lines.append((x1, y1, x2, y2)) 
            cv2.line(image_rgb, (x1, y1), (x2, y2), (0, 255, 0), 5)  

    shelf_lines = {1: [], 2: [], 3: []}

    if detected_lines:
        for (x1, y1, x2, y2) in detected_lines:
            mean_y = int((y1 + y2) / 2)
            if mean_y < 200: 
                shelf_lines[1].append(mean_y)
            elif 200 <= mean_y < 400:
                shelf_lines[2].append(mean_y)
            else:
                shelf_lines[3].append(mean_y)

    line_thickness = 5  
    for shelf, y_coords in shelf_lines.items():
        if y_coords:  
            mean_y = int(np.mean(y_coords))
            cv2.line(image_rgb, (0, mean_y), (image.shape[1], mean_y), (255, 0, 0), 20)  # Draw red line
            shelf_coords.append([(0, mean_y), (image.shape[1], mean_y)])

    for shelf, y_coords in shelf_lines.items():
        if y_coords: 
            mean_y = int(np.mean(y_coords))
            cv2.line(edges, (0, mean_y), (edges.shape[1], mean_y), (255), 20)  # Draw white line

    return shelf_coords


