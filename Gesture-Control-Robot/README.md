# Dobot Gesture Control

Control a Dobot Magician robotic arm using hand gestures captured via your webcam. This project uses **MediaPipe** for real-time hand landmark detection and **OpenCV** for visualization.

## 🚀 Features

- **Real-time Hand Tracking**: Uses MediaPipe to detect and track hand landmarks.
- **Dual-Hand Joint Mapping**: Maps finger angles from two hands to the Dobot's four joints (Base, Shoulder, Elbow, and Wrist).
- **Gesture-Based Suction Control**: Toggle the suction cup by pinching your thumb and pinky tips together (distance-based).
- **Interactive Feed**: Live camera view with landmark overlays and connection lines.

## 🛠️ Prerequisites

- **Python**: 3.9 or higher.
- **Hardware**:
  - Dobot Magician robotic arm.
  - Webcam.
- **Tools**: [uv](https://github.com/astral-sh/uv) (recommended) or pip.

## 📦 Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd Gesture-Control-Robot
   ```

2. **Install dependencies**:
   Using `uv`:
   ```bash
   uv sync
   ```
   Or using `pip`:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables**:
   Create a `.env` file in the root directory:
   ```bash
   cp .env.example .env
   ```
   Edit `.env` and set your Dobot's serial port:
   ```env
   DOBOT_PORT=COM3  # Windows example
   # DOBOT_PORT=/dev/ttyACM0  # Linux example
   ```

## 🎮 Usage

Run the main script:
```bash
uv run main.py
```

### Controls:
- **Movement**: Use two hands in front of the camera. The angles of your index and middle fingers will control the robot's joint positions.
- **Suction**: Bring your thumb tip and pinky tip close together to activate the suction cup. Release to deactivate.
- **Exit**: Press `q` while the camera window is focused to stop the program.

## 🏗️ Project Structure

- `main.py`: Entry point of the application.
- `src/models/robotcontroller.py`: Core logic for bridging camera input and robot commands.
- `src/models/handtracking.py`: MediaPipe wrapper for gesture detection.
- `pyproject.toml`: Project metadata and dependencies.
