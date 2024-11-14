import subprocess

# Command to run ollama
command = ["ollama", "run", "llama3.2", "--input", "What is an Atom ?"]

# Run the command and capture output in real-time
process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Stream the output
try:
    for line in process.stdout:
        print(line, end="")  # Print each line as it's received
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    process.stdout.close()
    process.wait()

