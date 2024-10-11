import nmrglue as ng
import matplotlib.pyplot as plt

# Load the Varian data
dic, data = ng.varian.read('/Users/fionnferreira/Library/CloudStorage/GoogleDrive-fionnferreira@gmail.com/My Drive/RUG shared/Master Project/Experiment files/FF006/FF006b_20231003_1H_20231003082340.fid')

# Perform Fourier Transform
data = ng.proc_base.fft(data)

# Apply automatic phase correction
data, phase_params = ng.proc_autophase.autops(data, 'acme', return_phases=True)

# Create a unit dictionary from the data
udic = ng.varian.guess_udic(dic, data)

# Generate a unit conversion object
uc = ng.fileiobase.uc_from_udic(udic)

# Get ppm values
ppm_values = uc.ppm_scale()

# Plot the spectrum
plt.figure()
plt.plot(ppm_values, data.real)
plt.xlabel('Chemical Shift (ppm)')
plt.ylabel('Intensity')
plt.title('1D NMR Spectrum')
plt.gca().invert_xaxis()  # Invert x-axis for NMR spectra
plt.show()