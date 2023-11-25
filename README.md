# HeadShot-Tracking-Python
## Project Overview

This Python project utilizes face recognition to track a specific person's head in a live camera feed. The goal is to identify the person whose face is provided in a reference picture and then track that person in real-time video. Once the target person is detected in the live video stream, a red circle is drawn around their head, and a notification is displayed indicating that the target has been detected.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [License](#license)

## Prerequisites

Before using this project, make sure you have the following prerequisites installed:

- Python 3.x
- OpenCV
- dlib
- face_recognition
- Other dependencies specified in the `requirements.txt` file

You can install the required dependencies using the following command:

```bash
pip install -r requirements.txt
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Dhruvdangi03/HeadShot-Tracking-Python.git
cd HeadShot-Tracking-Python
```

2. Install the required dependencies (see [Prerequisites](#prerequisites)).

3. Run the project:

```bash
python headshot_tracking.py
```

## Usage

1. Place a reference image (containing the target person's face) in the `Reference_images` folder.

2. Run the project using the instructions in the [Installation](#installation) section.

3. The live camera feed will open, and the system will attempt to detect and track the target person's head.

4. If the target person is detected, a red circle will be drawn around their head, and a notification will be displayed.

5. Press `Q` to exit the application.


## How It Works

1. The project uses face recognition to identify the target person's face in the reference image.

2. It then accesses the live camera feed and continuously analyzes the video frames.

3. If the target person's face is detected in the live video, a red circle is drawn around their head.

4. A notification message is displayed to indicate that the target person has been detected on the side of window.

Feel free to contribute, report issues, or suggest improvements!
