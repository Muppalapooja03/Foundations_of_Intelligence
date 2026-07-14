"""
Day 9 – Search Automation
Using DuckDuckGo free Python library instead of Google API
"""

from ddgs import DDGS
from datetime import datetime

# Collect dorks interactively
dorks = []
print("Enter your search queries (dorks). Type 'exit' when finished:")

while True:
    dork = input("Dork> ").strip()
    if dork.lower() == "exit":
        break
    if dork:
        dorks.append(dork)

log_file = "search_results_duckduckgo.log"

# Use append mode ("a") so logs grow over time
with open(log_file, "a", encoding="utf-8") as file:
    file.write("\n\n")
    file.write("Day 9 – Search Automation Run\n")
    file.write(f"Generated: {datetime.now()}\n")
    file.write("="*70 + "\n\n")

    total_results = 0

    with DDGS() as ddgs:
        for dork in dorks:
            file.write(f"\nDork: {dork}\n")
            file.write("-"*60 + "\n")

            try:
                results = ddgs.text(dork, max_results=5)
                count = 0
                for r in results:
                    count += 1
                    total_results += 1
                    file.write(f"{count}. {r['title']} - {r['href']}\n")
                if count == 0:
                    file.write("No results found.\n")
            except Exception as e:
                file.write(f"Error: {e}\n")

    # Add summary at the very bottom
    file.write("\n")
    file.write("="*70 + "\n")
    file.write(f"Summary: {len(dorks)} dorks searched, {total_results} results found.\n")
    file.write("="*70 + "\n")

print("Search completed.")
print(f"Results appended to {log_file}")
