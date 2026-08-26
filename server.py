from mcp.server.fastmcp import FastMCP
from pydantic import Field
from mcp.server.fastmcp.prompts import base


mcp = FastMCP("DocumentMCP", log_level="ERROR")

@mcp.tool(
        name="get_employee_details",
        description="Get employee details using an employee ID."
)
def get_employee(employee_id: str) -> dict:
    """Get employee details using employee ID."""

    employees = {
        "E001": {"employee_id": "E001", "name": "John", "department": "IT", "skill": "AWS"},
        "E002": {"employee_id": "E002", "name": "Sarah", "department": "HR", "skill": "Recruitment"},
        "E003": {"employee_id": "E003", "name": "David", "department": "Finance", "skill": "SAP"},
        "E004": {"employee_id": "E004", "name": "Priya", "department": "IT", "skill": "Python"}
    }

    return employees.get(
        employee_id,
        {"error": f"Employee {employee_id} not found"}
    )


if __name__ == "__main__":
    mcp.run(transport="stdio")