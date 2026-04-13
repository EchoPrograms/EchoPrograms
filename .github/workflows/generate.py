import json

with open("stats.json") as f:
    raw = json.load(f)

data = raw.get("data", raw)

total = data.get("human_readable_total", "0 hrs")
languages = data.get("languages", [])

lines = []
for lang in languages[:5]:
    name = lang.get("name", "Unknown")
    time = lang.get("text", "0")
    lines.append(f"- {name}: {time}")

lang_section = "\n".join(lines) if lines else "- No data"

section = f"""## ⏱ Hackatime Stats

**Total Time:** {total}

### Top Languages
{lang_section}
"""

with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

start = "<!--START_SECTION:hackatime-->"
end = "<!--END_SECTION:hackatime-->"

if start not in readme:
    readme += f"\n\n{start}\n{end}"

before = readme.split(start)[0]
after = readme.split(end)[1]

new_readme = before + start + "\n" + section + "\n" + end + after

with open("README.md", "w", encoding="utf-8") as f:
    f.write(new_readme)
