import hardpotato as hp
import numpy as np
import sys

# --- Configuration ---
model = 'chi1205b'
path = r'C:\CHI1205B\chi1205b.exe' 
folder = r'C:\coding\chi\data_test' # Update to your data folder

# Fixed CP Parameters
eh = 0.485
el = 0
tc = 10
ta = 10
pn = 'n'
si = 0.1
cl = 7

# --- Mode Selection ---
# 1: Hardcoded arrays
# 2: User input
mode = 1 

if mode == 1:
    # Example ic/ia values (Amps)
    ic_vals = np.array([0.001, 0.002, 0.003584])
    ia_vals = np.array([0.001, 0.002, 0.003584])
else:
    try:
        raw_ic = input("Enter ic values in mA (comma separated): ")
        raw_ia = input("Enter ia values in mA (comma separated): ")
        ic_vals = np.array([float(x.strip()) for x in raw_ic.split(',')]) / 1000.0
        ia_vals = np.array([float(x.strip()) for x in raw_ia.split(',')]) / 1000.0
    except ValueError:
        print("Invalid input. Please enter numbers separated by commas.")
        sys.exit(1)

# --- Validation ---
if len(ic_vals) != len(ia_vals):
    raise ValueError(f"Length mismatch: ic_vals ({len(ic_vals)}) and ia_vals ({len(ia_vals)}) must be the same length.")

# --- Setup and Run ---
hp.potentiostat.Setup(model, path, folder)

print(f"Starting batch CP measurement for {len(ic_vals)} cases...")

for k in range(len(ic_vals)):
    fileName = f"GCD-{k+1:02d}"
    print(f"\n--- Running {fileName} (ic={ic_vals[k]:.6f} A, ia={ia_vals[k]:.6f} A) ---")
    
    cp = hp.potentiostat.CP(
        ic=ic_vals[k], 
        ia=ia_vals[k], 
        eh=eh, 
        el=el, 
        tc=tc, 
        ta=ta, 
        pn=pn, 
        si=si, 
        cl=cl, 
        fileName=fileName, 
        header=f"GCD Batch {fileName} ic={ic_vals[k]}"
    )
    
    # Run the measurement
    # This will generate GCD-01.mcr, run chi.exe, and load GCD-01.txt for plotting
    cp.writeToFile()

print("\nBatch measurement complete.")
