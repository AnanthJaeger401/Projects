from ultralytics import YOLO
import cv2
import os
import numpy as np

model = YOLO('yolov8n.pt')
model.train(data='data.yaml', epochs=100, batch=16, imgsz=640, save=True, save_period=1)

metrics = model.val()
print(metrics)
