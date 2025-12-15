import subprocess

class BashTool:
    name = "Bash"
    description = "Execute a shell command on the local machine."
    
    schema = {
        "type": "function",
        "function": {
            "name": "Bash",
            "description": "Execute a shell command. Use this to explore filesystem or run scripts.",
            "parameters": {
                "type": "object",
                "properties": {
                    "command": {
                        "type": "string",
                        "description": "The shell command to execute."
                    }
                },
                "required": ["command"]
            }
        }
    }

    def __call__(self, command: str) -> str:
        print(f"\033[90m[System] Executing: {command}\033[0m")
        try:
            result = subprocess.run(
                command, 
                shell=True, 
                capture_output=True, 
                text=True, 
                timeout=30,
                encoding='utf-8',
                errors='replace'
            )
            output = result.stdout + result.stderr
            if not output:
                return "(No output)"
            return output
        except subprocess.TimeoutExpired:
            return "Error: Command timed out."
        except Exception as e:
            return f"Error: {str(e)}"

