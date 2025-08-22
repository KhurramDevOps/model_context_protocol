from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name= "doc_mcp", stateless_http = True)



@mcp.tool()
def greet(name: str) -> str:
    return f"Hello {name}"

mcp_server = mcp.streamable_http_app()

