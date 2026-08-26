import asyncio
from fastmcp import Client

client = Client("http://localhost:8000/mcp")

async def main():
    async with client:
        # 1. Fetch available tools
        tools = await client.list_tools()
        print("--- Available Tools ---")
        for tool in tools:
            print(f"Name: {tool.name}")
            print(f"Description: {tool.description}")
            print(f"Schema: {tool.inputSchema}\n")

        # 2. Call the available tool ('hello')
        # Check tool.inputSchema above to see if 'hello' accepts arguments
        # result = await client.call_tool("hello", {})
        # print("--- Tool Result ---")
        # print(result)

asyncio.run(main())