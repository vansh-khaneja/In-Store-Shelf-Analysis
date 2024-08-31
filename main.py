from ultralytics import YOLO
import cv2
import math
import utils
model = YOLO('yolov8n.pt')


class_list = [
    'person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus', 'train', 'truck', 'boat', 'traffic light',
    'fire hydrant', 'stop sign', 'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow',
    'elephant', 'bear', 'zebra', 'giraffe', 'backpack', 'umbrella', 'handbag', 'tie', 'suitcase', 'frisbee',
    'skis', 'snowboard', 'sports ball', 'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard',
    'tennis racket', 'bottle', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple',
    'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza', 'donut', 'cake', 'chair', 'couch',
    'potted plant', 'bed', 'dining table', 'toilet', 'tv', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone',
    'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'book', 'clock', 'vase', 'scissors', 'teddy bear',
    'hair drier', 'toothbrush'
]

img = cv2.imread("sample.png")
resize = cv2.resize(img, (1000, 600))

shelve_coords = utils.shelf_coordinates(resize)
shelf_2 = (shelve_coords[1][0][1],shelve_coords[2][0][1])
shelf_1 = (shelve_coords[0][0][1],shelve_coords[1][0][1])



start_y = shelf_2[0]
end_y = shelf_2[1]
roi = resize[start_y:end_y, :]

overlay = resize.copy()
cv2.rectangle(overlay, (0, 0), (resize.shape[1], start_y), (0, 0, 0), -1)
cv2.rectangle(overlay, (0, end_y), (resize.shape[1], resize.shape[0]), (0, 0, 0), -1)
alpha = 0.6
cv2.addWeighted(overlay, alpha, resize, 1 - alpha, 0, resize)

bottles = 0
arranged = 1
results = model(roi, stream=True)

points = []

for r in results:
    boxes = r.boxes
    for box in boxes:
        x1, y1, x2, y2 = box.xyxy[0]
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        currentClass = class_list[int(box.cls[0])]
        w, h = x2 - x1, y2 - y1
        cx, cy = int(x1 + w // 2), int(y1 + h // 2)
        currentConf = box.conf[0]

        if currentClass == 'bottle' and currentConf > 0.3:
            bottles += 1
            points.append((cx, cy))
            cv2.rectangle(roi, (x1, y1), (x2, y2), (255, 0, 0), 2)

            cv2.circle(roi, (cx, cy), 8, (0, 0, 255), -1)
            cv2.putText(roi, currentClass, (x1, y1 - 4), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1, cv2.LINE_AA, False)


    
print(points)
sorted_points = sorted(points, key=lambda point: point[0])
print(sorted_points)


for i in range(1, len(sorted_points)):
    if (math.fabs(sorted_points[i][1]-sorted_points[i-1][1])>7):
        arranged*=0

    cv2.line(roi, sorted_points[i - 1], sorted_points[i], (0, 255, 0), 4)
    

ans = "No" if arranged==0 else "Yes"

cv2.putText(resize, "Bottles Alligned: " + ans, (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255,0), 2, cv2.LINE_AA, False)

    

resize[start_y:end_y, :] = roi

cv2.putText(resize, "Shelf 1 ", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2, cv2.LINE_AA, False)

cv2.putText(resize, "Detection Window: " + str(int((end_y-start_y)*100/600))+ "%", (500, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2, cv2.LINE_AA, False)
cv2.putText(resize, "No. of bottles: " + str(bottles),(500, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255,0), 2, cv2.LINE_AA, False)


cv2.imshow("Image", resize)

cv2.waitKey(0)

cv2.destroyAllWindows()
