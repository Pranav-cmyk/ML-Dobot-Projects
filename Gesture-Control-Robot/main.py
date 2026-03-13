from src import RobotController

def main():
    try:
        robot_controller = RobotController(
            numberOfHands=2
        )
        robot_controller.start()
    except Exception as e:
        print(f"Failed to start: {e}")


if __name__ == "__main__":
    main()