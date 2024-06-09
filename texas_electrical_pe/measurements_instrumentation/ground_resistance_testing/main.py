import math

def wenner_method(V, I, spacing):
    """
    Calculate the ground resistance using the Wenner method.
    
    Parameters:
    V (float): Voltage in volts (V)
    I (float): Current in amperes (A)
    spacing (float): Spacing between electrodes in meters (m)
    
    Returns:
    float: Ground resistance in ohms (Ω)
    """
    if I == 0:
        raise ValueError("Current cannot be zero.")
    
    resistance = (2 * math.pi * spacing * V) / I
    return resistance

def schlumberger_method(V, I, spacing_a, spacing_b):
    """
    Calculate the ground resistance using the Schlumberger method.
    
    Parameters:
    V (float): Voltage in volts (V)
    I (float): Current in amperes (A)
    spacing_a (float): Spacing between current electrodes in meters (m)
    spacing_b (float): Spacing between voltage electrodes in meters (m)
    
    Returns:
    float: Ground resistance in ohms (Ω)
    """
    if I == 0:
        raise ValueError("Current cannot be zero.")
    
    resistance = (V / I) * (math.pi * (spacing_a**2 - spacing_b**2) / (2 * spacing_b))
    return resistance

def driven_rod_method(R1, L1, R2, L2):
    """
    Calculate the ground resistance using the Driven Rod method.
    
    Parameters:
    R1 (float): Ground resistance with one length of rod in ohms (Ω)
    L1 (float): Length of the first rod in meters (m)
    R2 (float): Ground resistance with a different length of rod in ohms (Ω)
    L2 (float): Length of the second rod in meters (m)
    
    Returns:
    float: Ground resistance in ohms (Ω)
    """
    if L1 == L2:
        raise ValueError("The lengths of the rods cannot be the same.")
    
    rho = (R2 * L2 - R1 * L1) / (L2 - L1)
    R = rho / L1
    return R

if __name__ == "__main__":
    pass
