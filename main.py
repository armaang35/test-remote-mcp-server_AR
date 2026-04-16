from fastmcp import FastMCP
import random

# Initialize MCP server
mcp = FastMCP("Simple Calculator Server")

# Tool 1: Add two numbers
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two given numbers and return the result."""
    return a + b

# Tool 2: Generate random number
@mcp.tool()
def random_number(min_val: int, max_val: int) -> int:
    """Generate a random number within a given range."""
    return random.randint(min_val, max_val)

# Resource: Server info
@mcp.resource("server://info", mime_type="application/json")
def server_info():
    """Get information about this MCP server."""
    return {
        "name": "Simple Calculator Server",
        "version": "1.0.0",
        "description": "A basic remote MCP server for testing"
    }

# Run as REMOTE server (HTTP)
if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)