import math

def surge_impedance_loading(V, Zc):
    """
    Calculate the surge impedance loading.
    
    Parameters:
    V (float): Voltage in volts (V)
    Zc (float): Characteristic impedance in ohms (Ω)
    
    Returns:
    float: Surge impedance loading in watts (W)
    """
    return V**2 / Zc

def characteristic_impedance(L, C):
    """
    Calculate the characteristic impedance of a transmission line.
    
    Parameters:
    L (float): Inductance per unit length in henries per meter (H/m)
    C (float): Capacitance per unit length in farads per meter (F/m)
    
    Returns:
    float: Characteristic impedance in ohms (Ω)
    """
    return math.sqrt(L / C)

def protection_quality_index(protected_value, unprotected_value):
    """
    Calculate the protection quality index.
    
    Parameters:
    protected_value (float): Value of the protected parameter
    unprotected_value (float): Value of the unprotected parameter
    
    Returns:
    float: Protection quality index
    """
    if unprotected_value == 0:
        raise ValueError("Unprotected value cannot be zero.")
    
    return protected_value / unprotected_value

def protective_margin(design_margin, actual_margin):
    """
    Calculate the protective margin.
    
    Parameters:
    design_margin (float): Design margin
    actual_margin (float): Actual margin
    
    Returns:
    float: Protective margin
    """
    return design_margin - actual_margin

if __name__ == "__main__":
    pass
