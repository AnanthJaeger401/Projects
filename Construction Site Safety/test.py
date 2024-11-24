from ultralytics import YOLO
import cv2
import matplotlib.pyplot as plt

model = YOLO("best.pt")

image_path = "test_image1.jpg"
image = cv2.imread(image_path)

results = model.predict(source=image, save=False, show=False)

annotated_image = results[0].plot()

plt.imshow(cv2.cvtColor(annotated_image, cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()

for result in results[0].boxes.data:
    x1, y1, x2, y2, conf, cls = result.tolist()
    print(f"Class: {model.names[int(cls)]}, Confidence: {conf:.2f}, Box: ({x1:.2f}, {y1:.2f}, {x2:.2f}, {y2:.2f})")
