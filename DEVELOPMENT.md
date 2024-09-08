# DEVELOPMENT PIPE

Use `/scripts/*` for get chunks by `parsing data`

## Clean_breakspaces

```python
import sys

if len(sys.argv) != 2:
    print("Usage: python3 script.py <file_path>")
    sys.exit(1)

file_path = sys.argv[1]

try:
    with open(file_path, 'r') as file:
        lines = file.readlines()
except FileNotFoundError:
    print(f"File {file_path} not found.")
    sys.exit(1)

filtered_lines = [line for line in lines if line.strip() != '']

with open(file_path, 'w') as file:
    file.writelines(filtered_lines)

print(f"Empty lines removed from {file_path}.")
```
## Prod_server

- [ ] наполнять каталог `/lib/{year}` от билда из `/dist/sermons/`
