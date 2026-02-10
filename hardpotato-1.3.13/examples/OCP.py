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
ttot = 1        # s, total time
dt = 0.01       # s, time increment
fileName = 'OCP' # base file name for data file
header = 'OCP'   # header for data file

# initialize experiment:
ocp = hp.potentiostat.OCP(ttot, dt, fileName, header)
# Run experiment:
ocp.run()

# Load recently acquired data
data = hp.load_data.OCP(fileName +'.txt', folder, model)
E = data.E
t = data.t

# Plot OCP with softpotato
sp.plotting.plot(t, E, xlab='$t$ / s', ylab='$E$ / V', fig=1, show=1)

