
import subprocess

def query_medllama(prompt):
    result = subprocess.run(
        ["ollama", "run", "medllama2", "--prompt", prompt],
        capture_output=True,
        text=True
    )
    return result.stdout.strip()
