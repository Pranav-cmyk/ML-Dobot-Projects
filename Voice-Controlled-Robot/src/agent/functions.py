from livekit.agents import Agent, function_tool, RunContext
from .prompts import instructions
from pydobot import Dobot
from dotenv import load_dotenv
import os
import serial


class Assistant(Agent):
    def __init__(self) -> None:
        super().__init__(instructions=instructions)

        try:
            self.dobot = Dobot(port=os.getenv('DOBOT_PORT'), verbose=False)
        except serial.serialutil.SerialException:
            print("Could not connect to Dobot. Please check the COM Port ENV file and try again.")
            raise
        
        self.currentAngles = self.dobot.pose()[4:]  
        
    @function_tool
    async def controlRobot(
        self,
        context: RunContext,
        baseAngle: int = None,
        shoulderAngle: int = None,
        elbowAngle: int = None,
        wristAngle: int = None,
        endEffectorState: bool = False,
    ):
        '''
        Move the robotic arm to the specified angle.
        
        Args:
            baseAngle (int): The angle to move the robotic arm's base joint to, in degrees
            This angle should be between 0 and 90 degrees.

            shoulderAngle (int): The angle to move the robotic arm's shoulder joint to, in degrees
            This angle should be between 0 and 90 degrees.
            
            elbowAngle (int): The angle to move the robotic arm's elbow joint to, in degrees
            This angle should be between 0 and 90 degrees.
            
            wristAngle (int): The angle to move the robotic arm's wrist joint to, in degrees
            these angles should be between 0 and 90 degrees.

            endEffectorState (bool): Whether to open or close the end effector (gripper).
            If True, the end effector will be closed (gripping). If False, it will be open (releasing).


        '''

        print(f"End Effector State: {'Closed (Gripping)' if endEffectorState else 'Open (Releasing)'}")
        self.dobot.suck(endEffectorState)
        
        print(f'Moving robotic arm to {baseAngle}, {shoulderAngle}, {elbowAngle}, {wristAngle} degrees.')
        self.dobot._set_ptp_cmd(
            baseAngle if baseAngle is not None else self.currentAngles[0],
            shoulderAngle if shoulderAngle is not None else self.currentAngles[1],
            elbowAngle if elbowAngle is not None else self.currentAngles[2],
            wristAngle if wristAngle is not None else self.currentAngles[3],
            mode=4,
            wait=False,
        )
        self.currentAngles = self.dobot.pose()[4:]

        return f'I Moved robotic arm as you specifided!'