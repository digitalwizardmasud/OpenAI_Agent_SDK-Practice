from mcp.server.fastmcp import FastMCP
from openai import OpenAI
import base64
from dotenv import load_dotenv
import os
load_dotenv()

mcp = FastMCP("Image Generator")
client = OpenAI() 





@mcp.tool()
def generate_image_from_prompt(prompt:str)-> str:
    """
    This tool is used to generate images from text prompts.
    """
    response = client.responses.create(
        model="gpt-5-nano",
        input=prompt,
        tools=[{"type": "image_generation"}],
    )

    image_data = [
        output.result
        for output in response.output
        if output.type == "image_generation_call"
    ]
    image_path = os.path.join(os.getcwd(), 'image.png')
    if image_data:
        image_base64 = image_data[0]
        with open(image_path, "wb") as f:
            f.write(base64.b64decode(image_base64))
    
    return image_path if image_data else "No image generated."

    ### Fake output 
    # image_path = os.path.join(os.getcwd(), 'image.png')
    # return image_path
if __name__ == "__main__":
    mcp.run(transport='sse')