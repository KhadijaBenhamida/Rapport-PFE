import re
with open("10-Implementation-EN.tex", "r", encoding="utf-8") as f:
    content = f.read()
pattern = r"\s*\\begin\{figure\}\[H\].*?\\end\{figure\}"
content = re.sub(pattern, "", content, flags=re.DOTALL)
content = re.sub(r"\n\n\n+", "\n\n", content)
with open("10-Implementation-EN.tex", "w", encoding="utf-8") as f:
    f.write(content)
print("Success")
