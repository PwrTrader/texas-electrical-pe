import math

def absorption_current(I0, time, constant):
    """
    Calculate the absorption current given initial current, time, and a constant.
    
    Parameters:
    I0 (float): Initial current in amperes (A)
    time (float): Time in seconds (s)
    constant (float): Absorption constant
    
    Returns:
    float: Absorption current in amperes (A)
    """
    return I0 * math.exp(-constant * time)

def minimum_insulation_resistance(V, I):
    """
    Calculate the minimum insulation resistance.
    
    Parameters:
    V (float): Voltage in volts (V)
    I (float): Current in amperes (A)
    
    Returns:
    float: Insulation resistance in ohms (Ω)
    """
    if I == 0:
        raise ValueError("Current cannot be zero.")
    
    return V / I

def effect_of_temperature_on_insulation_resistance(R0, T, T0, k):
    """
    Calculate the effect of temperature on insulation resistance.
    
    Parameters:
    R0 (float): Insulation resistance at reference temperature T0 in ohms (Ω)
    T (float): Temperature in degrees Celsius (°C)
    T0 (float): Reference temperature in degrees Celsius (°C)
    k (float): Temperature coefficient
    
    Returns:
    float: Insulation resistance at temperature T in ohms (Ω)
    """
    return R0 * math.exp(-k * (T - T0))

def coefficient_k_thermosetting(T):
    """
    Calculate the coefficient k for thermosetting insulation systems.
    
    Parameters:
    T (float): Temperature in degrees Celsius (°C)
    
    Returns:
    float: Coefficient k
    """
    return 0.5 * (T / 100)

def coefficient_k_thermoplastic(T):
    """
    Calculate the coefficient k for thermoplastic insulation systems.
    
    Parameters:
    T (float): Temperature in degrees Celsius (°C)
    
    Returns:
    float: Coefficient k
    """
    return 0.6 * (T / 100)

def polarization_index(R60, R10):
    """
    Calculate the polarization index.
    
    Parameters:
    R60 (float): Insulation resistance at 60 seconds in ohms (Ω)
    R10 (float): Insulation resistance at 10 seconds in ohms (Ω)
    
    Returns:
    float: Polarization index
    """
    if R10 == 0:
        raise ValueError("Insulation resistance at 10 seconds cannot be zero.")
    
    return R60 / R10

if __name__ == "__main__":
    pass
