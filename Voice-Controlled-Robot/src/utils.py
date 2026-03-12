import BytesIO
import json
from PIL import Image
from base64 import b64encode


def convertNumpyImageToBase64(self, frame: np.ndarray) -> dict:
        with BytesIO() as buffer:
            image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            image.thumbnail([800, 800])
            image.save(buffer, format='JPEG')
            buffer.seek(0)
            
            return {
                'mime_type': 'image/jpeg', 
                'data': b64encode(buffer.read()).decode()
            }

def parseJSONResponse(self, response_text: str) -> dict:
        try:
            lines = response_text.splitlines()
            for i, line in enumerate(lines):
                if line == '```json':
                    json_text = '\n'.join(lines[i+1:])
                    json_text = json_text.split("```")[0]
                    break
            return json.loads(json_text)
            
        except Exception as e:
            logger.warning(f'Failed to parse JSON: {e}')
            return response_text
        
    