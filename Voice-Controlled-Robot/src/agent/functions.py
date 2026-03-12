from livekit.agents import Agent, function_tool, RunContext
from .prompts import instructions
from pydobot import Dobot
from dotenv import load_dotenv
import os


class Assistant(Agent):
    def __init__(self) -> None:
        super().__init__(instructions=instructions)
        self.dobot = Dobot(port=os.getenv('DOBOT_PORT'), verbose=False)
        self.currentAngles = self.dobot.pose()[4:]  
        
    @function_tool
    async def moveRobot(
        self,
        context: RunContext,
        angle: int,
    ):
        '''
        Move the robotic arm to the specified angle.
        
        Args:
            angle (int): The angle to move the robotic arm to, in degrees
            This angle should be between 0 and 90 degrees.

        '''
        print(f'Moving robotic arm to {angle} degrees.')
        self.dobot._set_ptp_cmd(
            angle,
            self.currentAngles[1],
            self.currentAngles[2],
            self.currentAngles[3],
            mode=4,
            wait=False,
        )

        return f'I Moved robotic arm to {angle} degrees.'