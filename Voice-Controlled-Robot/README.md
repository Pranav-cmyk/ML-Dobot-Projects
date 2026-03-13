# Dobot Voice Control

An AI-powered voice assistant for the Dobot Magician robotic arm. This project uses **LiveKit Agents** and **Google's Gemini Realtime Model** to provide a natural language interface for controlling robotic movements.

## 🚀 Features

- **Natural Language Interaction**: Talk to your robot to move joints or toggle the end effector.
- **Real-time Voice Control**: Low-latency interaction powered by LiveKit's RTC infrastructure.
- **Intelligent Joint Mapping**: The assistant understands joint names (Base, Shoulder, Elbow, Wrist) and handles angle limits.
- **End Effector Control**: Simple voice commands to "pick up" or "release" objects using the suction cup.

## 🛠️ Prerequisites

- **Python**: 3.13 or higher.
- **Hardware**: Dobot Magician robotic arm.
- **Services**:
  - [LiveKit Cloud](https://cloud.livekit.io/) account (or self-hosted).
  - [Google AI Studio](https://aistudio.google.com/) API Key for Gemini.

## 📦 Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd Voice-Controlled-Robot
   ```

2. **Install dependencies**:
   Using `uv`:
   ```bash
   uv sync
   ```

   Using `pip`:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables**:
   Create a `.env` file in the root directory:
   ```bash
   cp .env.example .env
   ```
   Fill in your credentials:
   ```env
   LIVEKIT_URL=<your-livekit-url>
   LIVEKIT_API_KEY=<your-api-key>
   LIVEKIT_API_SECRET=<your-api-secret>
   GOOGLE_API_KEY=<your-google-api-key>
   DOBOT_PORT=<your dobot port>
   ```

## 🎮 Usage

Start the LiveKit agent:
```bash
uv run main.py dev
```

Once the agent is running, connect via a LiveKit-compatible frontend (like the [LiveKit Agent Playground](https://agents-playground.livekit.io/)) to start talking to the robot.

### Example Commands:
- "Hey, move the base to 45 degrees."
- "Lift the shoulder a bit."
- "Turn on the suction cup."
- "Release the object."

## 🏗️ Project Structure

- `main.py`: Entry point that starts the LiveKit agent server.
- `src/agent/agent.py`: Defines the agent session and integration with Gemini.
- `src/agent/functions.py`: Contains the `Assistant` class with `controlRobot` tool.
- `src/agent/prompts.py`: System instructions for the AI assistant.
