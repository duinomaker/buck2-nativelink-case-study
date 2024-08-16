import sys
import subprocess

rustc_version_string = subprocess.run(
    ["rustc", "--version"], capture_output=True, text=True, check=True
).stdout.strip()
output_file = sys.argv[1]

with open(output_file, "w") as f:
    f.write(rustc_version_string + "\n")
