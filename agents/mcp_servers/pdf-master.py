from mcp.server.fastmcp import FastMCP
from pypdf import PdfReader

mcp = FastMCP("PDF Master")

@mcp.tool()
def pdf_master_tool(file_path:str)-> str:
    """
    This tool is used to process PDF files.
    It can extract text
    """
    reader = PdfReader(file_path)
    content = ""
    for page in reader.pages:
        content += page.extract_text() + "\n"
    return content


if __name__ == "__main__":
    mcp.run(transport='stdio')