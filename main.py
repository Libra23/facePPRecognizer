from face_pp import FacePP
import base64
import glob


face_api = FacePP('Key', 'Secret')
faceset_token = face_api.create_faceset()
face_id = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

train_dataset_paths = "/Users/hiroki/Documents/PycharmProjects/facePPRecognizer/face-dataset/train"
file_labels = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

for index, label in enumerate(file_labels):
    files_path = train_dataset_paths + '/' + label
    # files = os.listdir(files_path)
    files = glob.glob(files_path + '/*.jpg')
    for file in files:
        print(label + ':' + file)
        with open(file, 'rb') as f:
            img_file = base64.encodebytes(f.read())
            face_api.add_face(faceset_token, img_file, face_id[index])

test_dataset_paths = "/Users/hiroki/Documents/PycharmProjects/facePPRecognizer/face-dataset/test"
for index, label in enumerate(file_labels):
    files_path = test_dataset_paths + '/' + label
    # files = os.listdir(files_path)
    files = glob.glob(files_path + '/*.jpg')
    for file in files:
        with open(file, 'rb') as f:
            img_file = base64.encodebytes(f.read())
            print(face_api.search_face(img_file, faceset_token))

