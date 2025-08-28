from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.prompts import base
from mcp.types import PromptMessage, TextContent
from pydantic import Field

mcp = FastMCP(name="Prompt Example", stateless_http=True)

docs = {
    "plan.md": "The plan outlines the steps for the project's implementation.",
    "spec.txt": "These specifications define the technical requirements for the equipment.",
}

@mcp.prompt(name= "format", description="Format the given document into a markdown table.")
def format_document(
    document_name: str = Field(..., description="The name of the document to format."),
) -> PromptMessage:
    if document_name not in docs:
        return PromptMessage(
            role="assistant",
            content=TextContent(text=f"Document '{document_name}' not found."),
        )

    content = docs[document_name]
    prompt = base.SystemPrompt(
        text="You are a helpful assistant that formats documents into markdown tables."
    ) + base.UserPrompt(
        text=f"Format the following document into a markdown table:\n\n{content}"
    )

    return PromptMessage(role="user", content=TextContent(type="text", text=prompt.render()))

@mcp.prompt(name="summarize", description="Summarize the given document.")
def summarize_document(
    document_name: str = Field(..., description="The name of the document to summarize."),
) -> PromptMessage:
    if document_name not in docs:
        return PromptMessage(
            role="assistant",
            content=TextContent(text=f"Document '{document_name}' not found."),
        )

    content = docs[document_name]
    prompt = base.SystemPrompt(
        text="You are a helpful assistant that summarizes documents."
    ) + base.UserPrompt(
        text=f"Summarize the following document:\n\n{content}"
    )

    return PromptMessage(role="user", content=TextContent(type="text", text=prompt.render()))

mcp_app = mcp.streamable_http_app()
