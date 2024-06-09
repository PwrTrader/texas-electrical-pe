import cmath

def delta_voltage_current_relationships(V_line):
    """
    Calculate the voltage and current relationships in a delta-connected circuit.
    
    Parameters:
    V_line (complex): Line voltage in volts (V)
    
    Returns:
    tuple: Phase voltage in volts (V), Line current in amperes (A)
    """
    V_phase = V_line
    I_line = V_phase / cmath.sqrt(3)
    return V_phase, I_line

def wye_voltage_current_relationships(V_line):
    """
    Calculate the voltage and current relationships in a wye-connected circuit.
    
    Parameters:
    V_line (complex): Line voltage in volts (V)
    
    Returns:
    tuple: Phase voltage in volts (V), Line current in amperes (A)
    """
    V_phase = V_line / cmath.sqrt(3)
    I_line = V_phase
    return V_phase, I_line

def apparent_power_rectangular(S_real, S_imag):
    """
    Calculate the apparent power in rectangular form.
    
    Parameters:
    S_real (float): Real power in watts (W)
    S_imag (float): Imaginary power in volt-amperes reactive (VAR)
    
    Returns:
    complex: Apparent power in volt-amperes (VA)
    """
    return complex(S_real, S_imag)

def apparent_power_phase_line(V_phase, I_phase):
    """
    Calculate the apparent power using phase voltage and phase current.
    
    Parameters:
    V_phase (complex): Phase voltage in volts (V)
    I_phase (complex): Phase current in amperes (A)
    
    Returns:
    complex: Apparent power in volt-amperes (VA)
    """
    return 3 * V_phase * I_phase.conjugate()

def apparent_power_combination(V_line, I_line, power_factor):
    """
    Calculate the apparent power using line voltage, line current, and power factor.
    
    Parameters:
    V_line (complex): Line voltage in volts (V)
    I_line (complex): Line current in amperes (A)
    power_factor (float): Power factor (0 to 1)
    
    Returns:
    complex: Apparent power in volt-amperes (VA)
    """
    S_line = 3 * V_line * I_line.conjugate()
    S_phase = S_line * power_factor
    return S_phase

def three_phase_wye_connected(V_ln, power_factor, S_total):
    """
    Calculate the 3-phase wye-connected source or load with line-to-neutral voltages and positive ABC phase sequence.
    
    Parameters:
    V_ln (complex): Line-to-neutral voltage in volts (V)
    power_factor (float): Power factor (0 to 1)
    S_total (complex): Total apparent power in volt-amperes (VA)
    
    Returns:
    tuple: Phase voltages and phase currents for A, B, and C phases, Line-to-line voltages
    """
    I_phase = S_total / (3 * V_ln * power_factor)
    V_phase_A = V_ln
    V_phase_B = V_ln * cmath.exp(-1j * 2 * cmath.pi / 3)
    V_phase_C = V_ln * cmath.exp(1j * 2 * cmath.pi / 3)
    
    V_AB = V_phase_A - V_phase_B
    V_BC = V_phase_B - V_phase_C
    V_CA = V_phase_C - V_phase_A
    
    return V_phase_A, V_phase_B, V_phase_C, I_phase, V_AB, V_BC, V_CA

def delta_to_wye(R_A, R_B, R_C):
    """
    Convert equivalent delta to wye resistances.
    
    Parameters:
    R_A (float): Delta resistance A
    R_B (float): Delta resistance B
    R_C (float): Delta resistance C
    
    Returns:
    tuple: Equivalent wye resistances R1, R2, R3
    """
    R_sum = R_A + R_B + R_C
    R1 = (R_B * R_C) / R_sum
    R2 = (R_A * R_C) / R_sum
    R3 = (R_A * R_B) / R_sum
    return R1, R2, R3

def wye_to_delta(R1, R2, R3):
    """
    Convert equivalent wye to delta resistances.
    
    Parameters:
    R1 (float): Wye resistance 1
    R2 (float): Wye resistance 2
    R3 (float): Wye resistance 3
    
    Returns:
    tuple: Equivalent delta resistances R_A, R_B, R_C
    """
    R_A = (R1 * R2 + R2 * R3 + R3 * R1) / R3
    R_B = (R1 * R2 + R2 * R3 + R3 * R1) / R1
    R_C = (R1 * R2 + R2 * R3 + R3 * R1) / R2
    return R_A, R_B, R_C

if __name__ == "__main__":
    pass
