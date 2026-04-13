import json

with open("stats.json") as f:
    raw = json.load(f)

data = raw["data"]

total = data.get("human_readable_total", "0")
languages = data.get("languages", [])

# top 5 languages
lines = []
for lang in languages[:5]:
    name = lang.get("name", "Unknown")
    time = lang.get("text", "0")
    percent = lang.get("percent", 0)
    lines.append(f"- {name}: {time} ({percent:.1f}%)")

lang_section = "\n".join(lines) if lines else "- No data"

section = f"""## ⏱ Hackatime Stats

**Total Time:** {total}

### Top Languages
{lang_section}
"""

start = "<!--START_SECTION:hackatime-->"
end = "<!--END_SECTION:hackatime-->"

with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

if start not in readme:
    readme += f"\n\n{start}\n{end}"

before = readme.split(start)[0]
after = readme.split(end)[1]

with open("README.md", "w", encoding="utf-8") as f:
    f.write(before + start + "\n" + section + "\n" + end + after)
