import face_recognition as fr
import cv2, os
# from IPython.display import Image, display
from matplotlib import pyplot as plt

image_path = "./122193_123765_3426.png"
image = fr.load_image_file(image_path)
face_locations = fr.face_locations(image)
for (top, right, bottom, left) in face_locations:
  cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 3)

plt.rcParams["figure.figsize"] = (16, 16)
plt.imshow(image)
plt.title("distance : ")
plt.show()







# plt.rcParams["figure.figsize"] = (1, 1)

# known_person_list = []
# known_person_list.append(fr.load_image_file("./people1.jpg"))
# known_person_list.append(fr.load_image_file("./people2.png"))
# known_person_list.append(fr.load_image_file("./people3.jpg"))
# known_person_list.append(fr.load_image_file("./people4.jpg"))

# known_face_list = []
# for person in known_person_list:
#   top, right, bottom, left = fr.face_locations(person)[0]
#   face_image = person[top:bottom, left:right]
#   known_face_list.append(face_image)
# for face in known_face_list:
#   plt.imshow(face)
#   plt.show()

# unknown_person = fr.load_image_file("./unknown.jpg")
# top, right, bottom, left = fr.face_locations(unknown_person)[0]
# unknown_face = unknown_person[top:bottom, left:right]
# plt.title("unknown_face")
# plt.imshow(unknown_face)
# plt.show()

# enc_unknown_face = fr.face_encodings(unknown_face)
# plt.imshow(enc_unknown_face)
# plt.show()

# for face in known_face_list:
#   enc_known_face = fr.face_encodings(face)
#   distance = fr.face_distance(enc_known_face, enc_unknown_face[0])
#   plt.title("distance : " + str(distance))
#   plt.imshow(face)
#   plt.show()