import cmath
import math  # Import the math module

def phasor(magnitude, phase_angle):
    """
    Create a phasor given magnitude and phase angle.
    
    Parameters:
    magnitude (float): Magnitude of the phasor
    phase_angle (float): Phase angle in degrees
    
    Returns:
    complex: Phasor represented as a complex number
    """
    phase_radians = math.radians(phase_angle)
    return cmath.rect(magnitude, phase_radians)

def impedance(resistance, reactance):
    """
    Calculate the impedance of a circuit element.
    
    Parameters:
    resistance (float): Resistance in ohms (Ω)
    reactance (float): Reactance in ohms (Ω)
    
    Returns:
    complex: Impedance represented as a complex number
    """
    return complex(resistance, reactance)

def complex_to_polar(z):
    """
    Convert a complex number to its polar form.
    
    Parameters:
    z (complex): Complex number
    
    Returns:
    tuple: Magnitude and phase angle in degrees
    """
    magnitude = abs(z)
    phase_angle = math.degrees(cmath.phase(z))
    return magnitude, phase_angle

if __name__ == "__main__":
    pass
