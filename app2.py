from pyzbar.pyzbar import decode
from PIL import Image
import cv2
import time
import csv

video = cv2.VideoCapture(0)

students = []
with open("attendance.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        students.append(row[1])

while True:
    check, frame = video.read()
    d = decode(frame)
    try:
        for obj in d:
            name = obj.data.decode()
            if name in students:
                students.remove(name)
                print("Deleted:", name)
    except Exception as e:
        print("Error:", e)

    cv2.imshow("Attendance", frame)
    key = cv2.waitKey(1)
    if key == ord("q"):
        print("Remaining students:", students)
        break

video.release()
cv2.destroyAllWindows()
