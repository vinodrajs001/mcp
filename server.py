from fastmcp import FastMCP
# from mcp.server.fastmcp import FastMCP

mcp = FastMCP("MyServer")

docs = {
    "deposition.md": "This deposition covers the testimony of Angela Smith, P.E.",
    "report.pdf": "The report details the state of a 20m condenser tower.",
    "financials.docx": "These financials outline the project's budget and expenditures.",
    "outlook.pdf": "This document presents the projected future performance of the system.",
    "plan.md": "The plan outlines the steps for the project's implementation.",
    "spec.txt": "These specifications define the technical requirements for the equipment.",
}


@mcp.tool()
def hello(name: str) -> str:
    return f"Hello, {name}!"

@mcp.tool()
def get_employees() -> list[dict]:
    """Return a list of employees."""
    return [
        {
            "emp_id": "E001",
            "name": "John",
            "department": "Engineering"
        },
        {
            "emp_id": "E002",
            "name": "Alice",
            "department": "Finance"
        }
    ]


if __name__ == "__main__":
    mcp.run()