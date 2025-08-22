from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name= "doc_mcp", stateless_http = True)

# @mcp.tool()
# def read_doc(doc_id: str) -> str:
#     return "This is a test document."

# @mcp.tool()
# def edit_doc(doc_id: str, new_content: str) -> str:
#     return "Document edited successfully."

@mcp.tool()
def greet(name: str) -> str:
    return f"Hello {name}"

mcp_server = mcp.streamable_http_app()

