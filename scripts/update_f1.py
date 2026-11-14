"""
Fetch the latest Formula 1 race result and write it into the profile README.

Extract: call the Jolpica F1 API for the most recent race.
Transform: keep the top three finishers and format them as a Markdown table.
Load: replace the text between the F1 markers in README.md.

If the API fails or returns no race (for example between seasons),
the script exits without touching the README, so the old result stays up.
"""

import json
import re
import sys
import urllib.request
from datetime import datetime, timezone

API_URL = "https://api.jolpi.ca/ergast/f1/current/last/results.json"
README_PATH = "README.md"
START_MARKER = "<!-- F1:START -->"
END_MARKER = "<!-- F1:END -->"


def fetch_latest_race():
    """Extract: return the most recent race as a dictionary."""
    request = urllib.request.Request(
        API_URL,
        headers={"User-Agent": "Sitina-Celine-profile-readme/1.0"},
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        data = json.load(response)

    races = data["MRData"]["RaceTable"]["Races"]
    if not races:
        raise ValueError("The API returned no races for the current season yet.")
    return races[0]


def build_section(race):
    """Transform: turn the race data into Markdown text."""
    lines = [
        f"**{race['raceName']}** (season {race['season']}, round {race['round']}, {race['date']})",
        "",
        "| Pos | Driver | Team | Time / Status |",
        "| --- | --- | --- | --- |",
    ]

    for result in race["Results"][:3]:
        driver = result["Driver"]
        full_name = f"{driver['givenName']} {driver['familyName']}"
        team = result["Constructor"]["name"]
        finish = result.get("Time", {}).get("time", result["status"])
        lines.append(f"| {result['position']} | {full_name} | {team} | {finish} |")

    refreshed = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines.append("")
    lines.append(f"<sub>Pipeline last ran: {refreshed}. Source: Jolpica F1 API.</sub>")
    return "\n".join(lines)


def update_readme(section):
    """Load: write the new section between the markers in README.md."""
    with open(README_PATH, encoding="utf-8") as file:
        readme = file.read()

    pattern = re.compile(
        re.escape(START_MARKER) + r".*?" + re.escape(END_MARKER),
        re.DOTALL,
    )
    if not pattern.search(readme):
        sys.exit("Could not find the F1 markers in README.md.")

    replacement = f"{START_MARKER}\n\n{section}\n\n{END_MARKER}"
    updated = pattern.sub(lambda match: replacement, readme)

    with open(README_PATH, "w", encoding="utf-8") as file:
        file.write(updated)


def main():
    try:
        race = fetch_latest_race()
    except Exception as error:
        print(f"Skipping update, could not fetch race data: {error}")
        return

    update_readme(build_section(race))
    print(f"README updated with {race['raceName']}.")


if __name__ == "__main__":
    main()
