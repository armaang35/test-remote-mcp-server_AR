from fastmcp import FastMCP

REMOTE_URL = "https://mcpserverAR.fastmcp.app/mcp"

mcp = FastMCP.as_proxy(
    REMOTE_URL,
    name="My Remote MCP Proxy"
)

if __name__ == "__main__":
    mcp.run()