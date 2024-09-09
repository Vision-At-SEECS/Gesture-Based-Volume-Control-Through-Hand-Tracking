# Gesture-Based-Volume-Control-Through-Hand-Tracking
Gesture Based Volume Control Through Hand Tracking

This project demonstrates hand tracking and volume control using OpenCV, MediaPipe, and Pycaw. It captures video from a webcam, detects hands in real-time, and controls the system volume based on the distance between the thumb and index finger.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Contributing](#contributing)
- [Example Images](#Example-Images)

## Installation

To run this project, you need to have Python installed along with the required libraries. Follow the steps below to set up the environment:

1. Clone the repository:
    ```sh
    git clone https://github.com/AbdullahUsama/hand-volume-control.git
    cd hand-volume-control
    ```

2. Create a virtual environment (optional but recommended):
    ```sh
    python -m venv venv-name
    # On Windows use `venv-name\Scripts\activate`
    ```

3. Install the required libraries:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

To run the hand tracking and volume control application, execute the following command:

```sh
python volume-hand-control.py
```
**Press q to quit the application.**

**Note: The module file contains a class that is required by the other python file**

## How It Works
The script performs the following steps:
1. Captures video from the webcam using OpenCV.
2. Converts the captured frames to RGB format.
3. Uses MediaPipe's Hand Detection module to detect hands in the frames.
4. For each detected hand, calculates the positions of the landmarks.
5. Controls the system volume based on the distance between the thumb and index finger using Pycaw.
6. Displays the processed frames in a window with FPS and volume information.

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue.

## Example Images

**Face Detection:**

![image](https://github.com/user-attachments/assets/7064c178-9367-4f8c-9ac6-0c7279e574d9)
