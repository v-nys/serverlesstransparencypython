import base64
from io import BytesIO
from rembg import remove
from PIL import Image

def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    image_data = base64.b64decode(req)
    image_data = BytesIO(image_data)
    image = Image.open(image_data)
    output = remove(image)
    buffered = BytesIO()
    output.save(buffered, format="PNG")
    image_bytes = buffered.getvalue()
    return base64.b64encode(image_bytes).decode("utf-8")
