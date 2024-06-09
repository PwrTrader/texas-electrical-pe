import math
import cmath

def sinusoidal_voltage(V_max, frequency, time, phase_angle=0):
    """
    Calculate the instantaneous value of a sinusoidal voltage.
    
    Parameters:
    V_max (float): Maximum voltage (amplitude)
    frequency (float): Frequency in Hz
    time (float): Time in seconds
    phase_angle (float): Phase angle in degrees (default is 0)
    
    Returns:
    float: Instantaneous voltage value
    """
    omega = 2 * math.pi * frequency
    phase_radians = math.radians(phase_angle)
    return V_max * math.sin(omega * time + phase_radians)

def average_full_wave_rectified(V_max):
    """
    Calculate the average value of a full-wave rectified sinusoid.
    
    Parameters:
    V_max (float): Maximum voltage (amplitude)
    
    Returns:
    float: Average value of the full-wave rectified sinusoid
    """
    return (2 * V_max) / math.pi

def rms_periodic_waveform(values):
    """
    Calculate the RMS value of a periodic waveform.
    
    Parameters:
    values (list of float): List of instantaneous values of the waveform
    
    Returns:
    float: RMS value of the periodic waveform
    """
    squared_values = [v**2 for v in values]
    mean_squared = sum(squared_values) / len(values)
    return math.sqrt(mean_squared)

def rms_sinusoidal_waveform(V_max):
    """
    Calculate the RMS value of a sinusoidal waveform.
    
    Parameters:
    V_max (float): Maximum voltage (amplitude)
    
    Returns:
    float: RMS value of the sinusoidal waveform
    """
    return V_max / math.sqrt(2)

def rms_half_wave_rectified(V_max):
    """
    Calculate the RMS value of a half-wave rectified sinusoid.
    
    Parameters:
    V_max (float): Maximum voltage (amplitude)
    
    Returns:
    float: RMS value of the half-wave rectified sinusoid
    """
    return V_max / 2

def sine_cosine_relations(angle_degrees):
    """
    Calculate the sine and cosine of an angle using trigonometric identities.
    
    Parameters:
    angle_degrees (float): Angle in degrees
    
    Returns:
    tuple: Sine and cosine of the angle
    """
    angle_radians = math.radians(angle_degrees)
    return math.sin(angle_radians), math.cos(angle_radians)

def phasor_transform(V_max, phase_angle=0):
    """
    Transform a sinusoidal waveform to its phasor representation.
    
    Parameters:
    V_max (float): Maximum voltage (amplitude)
    phase_angle (float): Phase angle in degrees (default is 0)
    
    Returns:
    complex: Phasor representation of the sinusoidal waveform
    """
    phase_radians = math.radians(phase_angle)
    return V_max * cmath.exp(1j * phase_radians)

def resistive_impedance(resistance):
    """
    Calculate the impedance of a resistive element.
    
    Parameters:
    resistance (float): Resistance in ohms (Ω)
    
    Returns:
    complex: Resistive impedance
    """
    return complex(resistance, 0)

def capacitive_impedance(capacitance, frequency):
    """
    Calculate the impedance of a capacitive element.
    
    Parameters:
    capacitance (float): Capacitance in farads (F)
    frequency (float): Frequency in Hz
    
    Returns:
    complex: Capacitive impedance
    """
    omega = 2 * math.pi * frequency
    return complex(0, -1 / (omega * capacitance))

def inductive_impedance(inductance, frequency):
    """
    Calculate the impedance of an inductive element.
    
    Parameters:
    inductance (float): Inductance in henries (H)
    frequency (float): Frequency in Hz
    
    Returns:
    complex: Inductive impedance
    """
    omega = 2 * math.pi * frequency
    return complex(0, omega * inductance)

def capacitive_reactance(capacitance, frequency):
    """
    Calculate the reactance of a capacitive element.
    
    Parameters:
    capacitance (float): Capacitance in farads (F)
    frequency (float): Frequency in Hz
    
    Returns:
    float: Capacitive reactance in ohms (Ω)
    """
    omega = 2 * math.pi * frequency
    return -1 / (omega * capacitance)

def inductive_reactance(inductance, frequency):
    """
    Calculate the reactance of an inductive element.
    
    Parameters:
    inductance (float): Inductance in henries (H)
    frequency (float): Frequency in Hz
    
    Returns:
    float: Inductive reactance in ohms (Ω)
    """
    omega = 2 * math.pi * frequency
    return omega * inductance

def real_power(V_rms, I_rms, power_factor):
    """
    Calculate the real power in an AC circuit.
    
    Parameters:
    V_rms (float): RMS voltage in volts (V)
    I_rms (float): RMS current in amperes (A)
    power_factor (float): Power factor (0 to 1)
    
    Returns:
    float: Real power in watts (W)
    """
    return V_rms * I_rms * power_factor

def power_factor(real_power, apparent_power):
    """
    Calculate the power factor in an AC circuit.
    
    Parameters:
    real_power (float): Real power in watts (W)
    apparent_power (float): Apparent power in volt-amperes (VA)
    
    Returns:
    float: Power factor (0 to 1)
    """
    return real_power / apparent_power

def reactive_power(V_rms, I_rms, power_factor):
    """
    Calculate the reactive power in an AC circuit.
    
    Parameters:
    V_rms (float): RMS voltage in volts (V)
    I_rms (float): RMS current in amperes (A)
    power_factor (float): Power factor (0 to 1)
    
    Returns:
    float: Reactive power in volt-amperes reactive (VAR)
    """
    return V_rms * I_rms * math.sqrt(1 - power_factor**2)

def complex_power(V_rms, I_rms):
    """
    Calculate the complex power in an AC circuit.
    
    Parameters:
    V_rms (float): RMS voltage in volts (V)
    I_rms (float): RMS current in amperes (A)
    
    Returns:
    complex: Complex power in volt-amperes (VA)
    """
    return complex(V_rms * I_rms, V_rms * I_rms * math.sqrt(1 - (real_power(V_rms, I_rms, power_factor(V_rms * I_rms, V_rms * I_rms)) / (V_rms * I_rms))**2))

if __name__ == "__main__":
    pass
