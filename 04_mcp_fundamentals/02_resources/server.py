from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name="resource_mcp", stateless_http=True)

docs  = {
    "deposition.md": "  Hello World This is a simple document.",
    "readme.md": " Hello World This is a readme document.",
    "index.md": " Hello World This is a index document.",

}

@mcp.resource("docs://documents", 
              mime_type="application/json")
def list_docs():
    """List all available documents."""
    return list(docs.keys())
    


@mcp.resource("docs://documents/{doc_name}",
                mime_type="application/json")
def read_doc(doc_name: str):
    """Read a specific document."""
    if doc_name in docs:
        return {"name": doc_name, "content": docs[doc_name]}
    else:
        raise mcp.ResourceNotFound(f"Document '{doc_name}' not found.")
    


mcp_app = mcp.streamable_http_app()