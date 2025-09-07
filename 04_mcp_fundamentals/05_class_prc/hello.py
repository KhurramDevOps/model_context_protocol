from mcp.server.fastmcp import FastMCP

mcp = FastMCP(stateless_http=True)

@mcp.prompt(name="weather_instructions", description="Instructions for weather agent")
def weather_agent_instructions(city:str):
    return f"""You are a helpful assistant that provides weather information of the {city}."""

mcp_app = mcp.streamable_http_app()