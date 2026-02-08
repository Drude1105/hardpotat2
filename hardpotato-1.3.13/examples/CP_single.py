import hardpotato as hp

# Setup the potentiostat
# Replace 'chi.exe' path and save folder as needed
model = 'chi1205b'
path = r'C:\CHI_Data\chi6273e.exe'
folder = r'C:\CHI_Data\GuoZhu'

hp.potentiostat.Setup(model, path, folder)

# Create CP object
# Parameters: ic, ia, eh, el, tc, ta, pn, si, cl
cp = hp.potentiostat.CP(
    ic=0.000003584, 
    ia=0.000003584, 
    eh=0.8, 
    el=0, 
    tc=10, 
    ta=10, 
    pn='p', 
    si=0.001, 
    cl=7, 
    fileName='GCD-01', 
    header='Lab CP Measurement'
)

# Run the measurement
# This will:
# 1. Write the macro to ./data/GCD-01.mcr
# 2. Call chi1205b.exe to run the macro
# 3. Load the results from ./data/GCD-01.txt and plot them
# cp.writeToFile()
cp.run()
