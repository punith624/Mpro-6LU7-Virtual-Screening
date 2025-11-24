from pymol import cmd
import os

# ✅ Input and output paths
PROTEIN = "data/protein_prepared.pdb"
POSE = "docking/poses/pose0_out.pdbqt"
OUT = "results/images/pose0.png"

# ✅ Create output folder if not exists
os.makedirs("results/images", exist_ok=True)

# ✅ Load protein and ligand
cmd.load(PROTEIN, "mpro")
cmd.load(POSE, "pose0")

# ✅ Visual styles
cmd.show("cartoon", "mpro")
cmd.color("cyan", "mpro")

cmd.show("sticks", "pose0")
cmd.color("yellow", "pose0")

# ✅ Center and render
cmd.orient()

# ✅ Save image
cmd.png(OUT, dpi=300, ray=1)

print("✅ Image saved at:", OUT)
