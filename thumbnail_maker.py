from PIL import Image
import base64
import io

def image_converter(original_file):
    original_data = base64.b64decode(original_file)

    original_image = Image.open(io.BytesIO(original_data))

    resized_image = original_image.resize((100, 100))

    buffer = io.BytesIO()
    resized_image.save(buffer, format="PNG")
    resized_image_data = base64.b64encode(buffer.getvalue())

    return resized_image_data


