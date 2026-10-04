from fastmcp import FastMCP
import os
import asyncpg
import json
from dotenv import load_dotenv

load_dotenv()

# ============================================================
# PostgreSQL Configuration
# ============================================================

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL environment variable is not set")

print("PostgreSQL database configured")


# ============================================================
# MCP Server
# ============================================================

mcp = FastMCP("ExpenseTracker")


# ============================================================
# Database Initialization
# ============================================================

async def init_db():
    try:
        conn = await asyncpg.connect(DATABASE_URL)

        await conn.execute("""
            CREATE TABLE IF NOT EXISTS expenses(
                id SERIAL PRIMARY KEY,
                date TEXT NOT NULL,
                amount DOUBLE PRECISION NOT NULL,
                category TEXT NOT NULL,
                subcategory TEXT DEFAULT '',
                note TEXT DEFAULT ''
            )
        """)

        await conn.close()

        print("PostgreSQL database initialized successfully")

    except Exception as e:
        print(f"Database initialization error: {e}")
        raise


# ============================================================
# Add Expense
# ============================================================

@mcp.tool()
async def add_expense(
    date,
    amount,
    category,
    subcategory="",
    note=""
):
    """Add a new expense entry to the database."""

    try:
        conn = await asyncpg.connect(DATABASE_URL)

        row = await conn.fetchrow(
            """
            INSERT INTO expenses
            (date, amount, category, subcategory, note)
            VALUES ($1, $2, $3, $4, $5)
            RETURNING id
            """,
            date,
            amount,
            category,
            subcategory,
            note
        )

        await conn.close()

        return {
            "status": "success",
            "id": row["id"],
            "message": "Expense added successfully"
        }

    except Exception as e:
        return {
            "status": "error",
            "message": f"Database error: {str(e)}"
        }


# ============================================================
# List Expenses
# ============================================================

@mcp.tool()
async def list_expenses(start_date, end_date):
    """List expense entries within an inclusive date range."""

    try:
        conn = await asyncpg.connect(DATABASE_URL)

        rows = await conn.fetch(
            """
            SELECT
                id,
                date,
                amount,
                category,
                subcategory,
                note
            FROM expenses
            WHERE date BETWEEN $1 AND $2
            ORDER BY date DESC, id DESC
            """,
            start_date,
            end_date
        )

        await conn.close()

        return [dict(row) for row in rows]

    except Exception as e:
        return {
            "status": "error",
            "message": f"Error listing expenses: {str(e)}"
        }


# ============================================================
# Summarize Expenses
# ============================================================

@mcp.tool()
async def summarize(start_date, end_date, category=None):
    """Summarize expenses by category within an inclusive date range."""

    try:
        conn = await asyncpg.connect(DATABASE_URL)

        if category:

            rows = await conn.fetch(
                """
                SELECT
                    category,
                    SUM(amount) AS total_amount,
                    COUNT(*) AS count
                FROM expenses
                WHERE date BETWEEN $1 AND $2
                AND category = $3
                GROUP BY category
                ORDER BY total_amount DESC
                """,
                start_date,
                end_date,
                category
            )

        else:

            rows = await conn.fetch(
                """
                SELECT
                    category,
                    SUM(amount) AS total_amount,
                    COUNT(*) AS count
                FROM expenses
                WHERE date BETWEEN $1 AND $2
                GROUP BY category
                ORDER BY total_amount DESC
                """,
                start_date,
                end_date
            )

        await conn.close()

        return [dict(row) for row in rows]

    except Exception as e:
        return {
            "status": "error",
            "message": f"Error summarizing expenses: {str(e)}"
        }


# ============================================================
# Categories Resource
# ============================================================

CATEGORIES_PATH = os.path.join(
    os.path.dirname(__file__),
    "categories.json"
)


@mcp.resource(
    "expense:///categories",
    mime_type="application/json"
)
def categories():

    try:

        default_categories = {
            "categories": [
                "Food & Dining",
                "Transportation",
                "Shopping",
                "Entertainment",
                "Bills & Utilities",
                "Healthcare",
                "Travel",
                "Education",
                "Business",
                "Other"
            ]
        }

        try:

            with open(
                CATEGORIES_PATH,
                "r",
                encoding="utf-8"
            ) as f:

                return f.read()

        except FileNotFoundError:

            return json.dumps(
                default_categories,
                indent=2
            )

    except Exception as e:

        return json.dumps({
            "error": f"Could not load categories: {str(e)}"
        })


# ============================================================
# Start Server
# ============================================================

if __name__ == "__main__":

    import asyncio

    # Initialize PostgreSQL database
    asyncio.run(init_db())

    # Start MCP server
    mcp.run(
        transport="http",
        host="0.0.0.0",
        port=8000
    )