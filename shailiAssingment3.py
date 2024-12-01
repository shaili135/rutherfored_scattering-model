shailiAssingment3.py
import math
from math import sqrt,log,cos,sin,pi,tan
from random import random
import matplotlib.pyplot as plt

# Constants defining the experiment parameters
Z = 79                      # Atomic number of the target material (gold in this case)
e = 1.602e-19               # Elementary charge in coulombs
E = 7.7e6*e                 # Kinetic energy of the incident particles in joules
epsilonO = 8.854e-12        # Vacuum permittivity in farads per meter
a0 = 5.292e-11              # Bohr radius in meters
sigma = a0/100              # Standard deviation for Gaussian distribution
N = 1000000                 # Number of incident particles

# Function to generate two Gaussian random numbers for the scattering experiment
def gaussian():
    r = sqrt(-2*sigma*sigma*log(1-random()))  # Generate r from Gaussian distribution
    theta = 2*pi*random()                      # Generate theta from uniform distribution
    x = r*cos(theta)                          # Convert to Cartesian coordinates
    y = r*sin(theta)
    return x, y

# Function to simulate the scattering experiment and calculate fraction of scattered particles
def fraction(theta):
    count = 0
    for i in range(N):
        x, y = gaussian()                                    # Generate random position
        b = sqrt(x*x + y*y)                                  # Calculate impact parameter
        if b < Z*e*e/(2*pi*epsilonO*E*tan(theta/2)):         # Check if particle is scattered
            count += 1
    return count / N                                         # Return fraction of scattered particles

# Define a range of scattering angles in degrees , taken as 4 angles as given in question
theta_degrees = [ 30, 45, 90, 120 ]

# Convert degrees to radians and calculate the fraction of scattered particles for each angle
scattering_particles = []
for angle in theta_degrees:
    n = fraction(math.radians(angle))                        # Convert angle to radians
    scattering_particles.append(n)

# Plot the results
plt.plot(theta_degrees, scattering_particles, marker='o')
plt.xlabel("Scattering angle (in degrees)")
plt.ylabel("Fraction of particles scattered")
plt.title("Rutherford Experiment")
plt.grid(True)  # Add grid lines

# Display the plot
plt.show()
