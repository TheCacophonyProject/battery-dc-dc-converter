import subprocess
import os

dir_path = "./generated-pcbs/battery-dc-dc-panel"

os.makedirs(dir_path, exist_ok=True)

command = [
    "kikit", "panelize",
    "--layout", "grid; rows: 5; cols: 2; space: 3mm; renameref: {orig}-{n}",
    "--tabs", "annotation",
    "--cuts", "mousebites; offset: -0.1mm",
    "--post", "millradius: 1mm",
    "--framing", "frame",
    "--fiducials", "type: 4fid; hoffset: 3.85mm; voffset:6mm",
    "--tooling", "type: 4hole; hoffset: 3mm; voffset: 3mm; size: 2mm",
    "--copperfill", "type: solid; layers: all",
    "./battery-dc-dc/battery-dc-dc.kicad_pcb",
    f"{dir_path}/battery-dc-dc-panel.kicad_pcb"
]

# Run the command
result = subprocess.run(command, capture_output=True, text=True)

# Check if the command was successful
if result.returncode == 0:
    print("Command succeeded.")
    print("Output:", result.stdout)
else:
    print("Command failed.")
    print("Error:", result.stderr)


# replace '"lib_footprint_issues": "warning",'
# with '"lib_footprint_issues": "ignore",'
# in {dir_path}/battery-dc-dc-panel.kicad_pro

with open(f"{dir_path}/battery-dc-dc-panel.kicad_pro", "r") as file:
    content = file.read()

content = content.replace('"lib_footprint_issues": "warning",', '"lib_footprint_issues": "ignore",')

with open(f"{dir_path}/battery-dc-dc-panel.kicad_pro", "w") as file:
    file.write(content)
