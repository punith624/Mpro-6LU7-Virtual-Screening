import os
import subprocess

# ✅ Path to Vina executable (Windows)
VINA = r"C:\Program Files (x86)\Vina\vina.exe"

# ✅ Input / Output paths
CONFIG = "docking/config.txt"
LIGAND = "data/pose0.pdbqt"
OUT = "docking/poses/pose0_out.pdbqt"

# ✅ Build the command
cmd = [
    VINA,
    "--config", CONFIG,
    "--ligand", LIGAND,
    "--out", OUT
]

print("Running:", " ".join(cmd))
subprocess.run(cmd, check=True)
print("✅ Docking complete!")

