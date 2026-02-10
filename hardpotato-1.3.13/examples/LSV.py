import hardpotato as hp
import softpotato as sp

# Select the potentiostat model to use:
#model = 'chi760e'
model = 'chi1205b'
#model = 'emstatpico'

# Path to the chi software, including extension .exe
path = r'C:\CHI1205B\chi1205b.exe' 
folder = r'C:\coding\chi\data_test' # Update to your data folder


# Initialization:
hp.potentiostat.Setup(model, path, folder)

# Experimental parameters:
Eini = -0.5     # V, initial potential
Efin = 0.5      # V, final potential
sr = 1          # V/s, scan rate
dE = 0.001      # V, potential increment
sens = 1e-6     # A/V, current sensitivity
E2 = 0.5        # V, potential of the second working electrode
sens2 = 1e-9    # A/V, current sensitivity of the second working electrode
fileName = 'LSV'# base file name for data file
header = 'LSV'  # header for data file

# initialize experiment:
lsv = hp.potentiostat.LSV(Eini, Efin, sr, dE, sens, fileName, header)
# Run experiment:
lsv.run()

# Load recently acquired data
data = hp.load_data.LSV(fileName +'.txt', folder, model)
i = data.i
E = data.E

# Plot CV with softpotato
sp.plotting.plot(E, i, fig=1, show=1)

