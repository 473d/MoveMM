import cv2
import mediapipe as mp
import pyautogui


cam = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)


# 7jm l screen
screen_w, screen_h = pyautogui.size()


while True:
    _, frame = cam.read()
    #frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)
    landmark_points = output.multi_face_landmarks
    frame_h, frame_w, _ = frame.shape


    if landmark_points:
        landmarks = landmark_points[0].landmark
        for id, landmark in enumerate(landmarks[13:14]):
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 0))




# l mouse byt7rrk lmma yt7rrk l fm
# .................................................................................................

            if id == 0:
                screen_x = screen_w * landmark.x
                screen_y = screen_h * landmark.y
                pyautogui.moveTo(screen_x, screen_y)


#.................................................................................................




############################################################### 3shn a3ml clk
        lips = [landmarks[13], landmarks[14]]


        print(lips[0].y)
        print(lips[1].y)
        s=lips[1].y - lips[0].y
        print(s)
        print("######################################################")


        for landmark in lips:


            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 255))


        if (lips[1].y - lips[0].y)  > 0.07:
            pyautogui.click()
            pyautogui.sleep(1)
##############################################################################



    cv2.imshow('MOVE', frame)
    cv2.waitKey(1)



















