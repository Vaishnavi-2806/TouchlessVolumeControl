import cv2
import mediapipe as mp
import numpy as np
from math import hypot

from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL

# ---------------- AUDIO SETUP ----------------
devices = AudioUtilities.GetSpeakers()

interface = devices.Activate(
    IAudioEndpointVolume._iid_,
    CLSCTX_ALL,
    None
)

volume = cast(interface, POINTER(IAudioEndpointVolume))

volRange = volume.GetVolumeRange()
minVol = volRange[0]
maxVol = volRange[1]

# ---------------- HAND TRACKING SETUP ----------------
mpHands = mp.solutions.hands
hands = mpHands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

mpDraw = mp.solutions.drawing_utils

# ---------------- WEBCAM ----------------
cap = cv2.VideoCapture(0)

# Store last volume percentage
last_vol_percent = 50

while True:
    success, img = cap.read()

    if not success:
        break

    # Flip image for mirror effect
    img = cv2.flip(img, 1)

    # Get image size
    h, w, c = img.shape

    # Convert BGR to RGB
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Process hand landmarks
    results = hands.process(imgRGB)

    hand_detected = False

    if results.multi_hand_landmarks:

        hand_detected = True

        for handLms in results.multi_hand_landmarks:

            # Thumb tip (landmark 4)
            x1 = int(handLms.landmark[4].x * w)
            y1 = int(handLms.landmark[4].y * h)

            # Index finger tip (landmark 8)
            x2 = int(handLms.landmark[8].x * w)
            y2 = int(handLms.landmark[8].y * h)

            # Calculate distance
            length = hypot(x2 - x1, y2 - y1)

            # Convert distance to volume percentage
            vol_percent = np.interp(length, [20, 200], [0, 100])

            # Save last volume
            last_vol_percent = vol_percent

            # Convert percentage to system volume range
            vol = np.interp(
                vol_percent,
                [0, 100],
                [minVol, maxVol]
            )

            # Set system volume
            volume.SetMasterVolumeLevel(vol, None)

            # Draw landmarks
            mpDraw.draw_landmarks(
                img,
                handLms,
                mpHands.HAND_CONNECTIONS
            )

            # Draw circles on fingertips
            cv2.circle(
                img,
                (x1, y1),
                10,
                (255, 0, 255),
                cv2.FILLED
            )

            cv2.circle(
                img,
                (x2, y2),
                10,
                (255, 0, 255),
                cv2.FILLED
            )

            # Draw line between fingers
            cv2.line(
                img,
                (x1, y1),
                (x2, y2),
                (255, 0, 255),
                3
            )

    # Keep last volume when hand is removed
    if not hand_detected:
        pass

    # Display volume percentage
    cv2.putText(
        img,
        f'Volume: {int(last_vol_percent)}%',
        (50, 80),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        3
    )

    # Show webcam window
    cv2.imshow(
        "Touchless Volume Control",
        img
    )

    # Press ESC to exit
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
