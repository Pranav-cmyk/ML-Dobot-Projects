# Dobot Control Projects

A collection of interactive control systems for the **Dobot Magician** robotic arm, ranging from computer vision-based gesture control to natural language voice interfaces.

## 🛠️ Project Overview

This repository contains various implementations for controlling the Dobot Magician. Each project is self-contained with its own dependencies and configuration.

### 1. [Gesture Control Robot](./Gesture-Control-Robot)
Control the Dobot's joints and suction cup using real-time hand tracking.
- **Tech Stack**: Python, MediaPipe, OpenCV, pydobot.
- **Key Feature**: Maps finger angles from two hands to robot joints for intuitive movement.

### 2. [Voice Controlled Robot](./Voice-Controlled-Robot)
Interact with the Dobot using natural language voice commands.
- **Tech Stack**: Python, LiveKit, Google Gemini (Realtime Model), pydobot.
- **Key Feature**: AI-powered assistant that translates voice intent into precise robotic movements.

## ⚙️ General Prerequisites

Before running any project, ensure you have:
1. **Dobot Magician** connected via USB.
2. **Python** installed (check individual project READMEs for specific version requirements).
3. **Serial Drivers** for the Dobot installed on your system.

## 🚀 Getting Started

Navigate to the project of your choice and follow the instructions in its specific `README.md` file.

```bash
# Example: Setting up Gesture Control
cd Gesture-Control-Robot
pip install -r requirements.txt
python main.py
```
