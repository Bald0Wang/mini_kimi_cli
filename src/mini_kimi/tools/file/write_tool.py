class WriteFileTool:
    name = "WriteFile"
    description = "Write content to a file."

    schema = {
        "type": "function",
        "function": {
            "name": "WriteFile",
            "description": "Write content to a file. Overwrites existing file.",
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {
                        "type": "string",
                        "description": "The file path to write to."
                    },
                    "content": {
                        "type": "string",
                        "description": "The content to write."
                    }
                },
                "required": ["path", "content"]
            }
        }
    }

    def __call__(self, path: str, content: str) -> str:
        print(f"\033[90m[System] Writing to file: {path}\033[0m")
        try:
            if ".." in path:
                return "Error: Path cannot contain '..'"
            
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)
            return f"Successfully wrote to {path}"
        except Exception as e:
            return f"Error writing file: {str(e)}"

