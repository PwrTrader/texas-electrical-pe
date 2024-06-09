import math

def per_unit_summary(V_actual, V_base, S_actual, S_base):
    """
    Calculate per unit values for voltage and apparent power.
    
    Parameters:
    V_actual (float): Actual voltage in volts (V)
    V_base (float): Base voltage in volts (V)
    S_actual (float): Actual apparent power in volt-amperes (VA)
    S_base (float): Base apparent power in volt-amperes (VA)
    
    Returns:
    tuple: Per unit voltage and per unit apparent power
    """
    V_pu = V_actual / V_base
    S_pu = S_actual / S_base
    return V_pu, S_pu

def base_current_single_phase(S_base, V_base):
    """
    Calculate the base current for a single-phase system.
    
    Parameters:
    S_base (float): Base apparent power in volt-amperes (VA)
    V_base (float): Base voltage in volts (V)
    
    Returns:
    float: Base current in amperes (A)
    """
    return S_base / V_base

def base_impedance_single_phase(V_base, S_base):
    """
    Calculate the base impedance for a single-phase system.
    
    Parameters:
    V_base (float): Base voltage in volts (V)
    S_base (float): Base apparent power in volt-amperes (VA)
    
    Returns:
    float: Base impedance in ohms (Ω)
    """
    return V_base**2 / S_base

def base_current_three_phase(S_base, V_base):
    """
    Calculate the base current for a three-phase system.
    
    Parameters:
    S_base (float): Base apparent power in volt-amperes (VA)
    V_base (float): Base voltage in volts (V)
    
    Returns:
    float: Base current in amperes (A)
    """
    return S_base / (math.sqrt(3) * V_base)

def base_impedance_three_phase(V_base, S_base):
    """
    Calculate the base impedance for a three-phase system.
    
    Parameters:
    V_base (float): Base voltage in volts (V)
    S_base (float): Base apparent power in volt-amperes (VA)
    
    Returns:
    float: Base impedance in ohms (Ω)
    """
    return V_base**2 / S_base

def change_of_base_per_unit(Z_pu_old, S_base_old, S_base_new, V_base_old, V_base_new):
    """
    Calculate the change of base for per unit impedance.
    
    Parameters:
    Z_pu_old (float): Old per unit impedance
    S_base_old (float): Old base apparent power in volt-amperes (VA)
    S_base_new (float): New base apparent power in volt-amperes (VA)
    V_base_old (float): Old base voltage in volts (V)
    V_base_new (float): New base voltage in volts (V)
    
    Returns:
    float: New per unit impedance
    """
    Z_base_old = V_base_old**2 / S_base_old
    Z_base_new = V_base_new**2 / S_base_new
    Z_pu_new = Z_pu_old * (Z_base_old / Z_base_new)
    return Z_pu_new

if __name__ == "__main__":
    pass
