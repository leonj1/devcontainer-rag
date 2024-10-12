import asyncio
from fetcher import fetch_all_contents
from database import create_database, add_documents, query_database

URLS = [
    "https://containers.dev/implementors/spec/",
    "https://containers.dev/implementors/features/",
    "https://containers.dev/implementors/reference/",
    "https://containers.dev/implementors/json_schema/",
    "https://containers.dev/implementors/json_reference/",
    "https://containers.dev/implementors/features-distribution/",
    "https://containers.dev/implementors/templates/"
]

async def main():
    # Fetch contents
    contents = await fetch_all_contents(URLS)

    # Create and populate database
    db = create_database()
    add_documents(db, contents)

    # Example query
    query = "What are dev containers?"
    results = query_database(db, query)
    print(f"Query: {query}")
    print("Results:")
    for result in results:
        print(f"- {result}")

if __name__ == "__main__":
    asyncio.run(main())
