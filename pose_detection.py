import cv2
import mediapipe as mp
import time

# Initialize MediaPipe Pose
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
mp_draw = mp.solutions.drawing_utils

# Webcam capture
cap = cv2.VideoCapture(0)

def detect_pose(landmarks):
    # Get key landmarks
    nose = landmarks[mp_pose.PoseLandmark.NOSE.value]
    left_hip = landmarks[mp_pose.PoseLandmark.LEFT_HIP.value]
    right_hip = landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value]
    left_knee = landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value]
    right_knee = landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value]
    left_wrist = landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value]
    right_wrist = landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value]

    # Average hip and knee height
    hip_y = (left_hip.y + right_hip.y) / 2
    knee_y = (left_knee.y + right_knee.y) / 2

    # ---- Pose Rules ----
    if left_wrist.y < nose.y or right_wrist.y < nose.y:
        return "Hand Raised"

    elif hip_y < knee_y - 0.05:
        return "Standing"

    else:
        return "Sitting"

print("📸 Pose Detection Started (Press Q to quit)")

last_pose = ""
last_time = time.time()

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = pose.process(rgb_frame)

    if result.pose_landmarks:
        landmarks = result.pose_landmarks.landmark
        pose_name = detect_pose(landmarks)

        # 🔴 Display Landmark points & skeleton
        mp_draw.draw_landmarks(
            frame,
            result.pose_landmarks,
            mp_pose.POSE_CONNECTIONS
        )

        # Avoid spamming terminal
        if pose_name != last_pose and time.time() - last_time > 1:
            print(f"Pose detected: {pose_name}")
            last_pose = pose_name
            last_time = time.time()

    cv2.imshow("Webcam (Press Q to Exit)", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()