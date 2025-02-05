import dlib


class LandmarksDetector:
    def __init__(self, predictor_model_path):
        """
        :param predictor_model_path: path to shape_predictor_68_face_landmarks.dat file
        """
        self.detector = (
            dlib.get_frontal_face_detector()
        )  # cnn_face_detection_model_v1 also can be used
        self.shape_predictor = dlib.shape_predictor(str(predictor_model_path))

    def get_landmarks(self, image):
        img = dlib.load_rgb_image(str(image))
        dets = self.detector(img, 1)

        for detection in dets:
            try:
                face_landmarks = [
                    (item.x, item.y)
                    for item in self.shape_predictor(img, detection).parts()
                ]
                yield face_landmarks
            except:
                print("Exception in get_landmarks()!")
