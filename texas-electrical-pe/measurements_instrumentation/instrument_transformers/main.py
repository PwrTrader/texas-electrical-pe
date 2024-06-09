import math
import cmath

def calculate_power_factor(method, P=None, S=None, theta=None):
    """
    Calculate the power factor using either real power (P) and apparent power (S) or cos(theta).
    
    Parameters:
    method (str): Method to calculate power factor, either 'ratio' for P/S or 'cos' for cos(theta)
    P (float): Real power in watts (W), required if method is 'ratio'
    S (float): Apparent power in volt-amperes (VA), required if method is 'ratio'
    theta (float): Phase angle in degrees, required if method is 'cos'
    
    Returns:
    float: Power factor (cosine of the phase angle)
    float: Phase angle in degrees (only applicable for 'ratio' method)
    """
    if method == 'ratio':
        if P is None or S is None:
            raise ValueError("Real power (P) and apparent power (S) must be provided for 'ratio' method.")
        if S == 0:
            raise ValueError("Apparent power (S) cannot be zero.")
        
        power_factor = P / S
        power_factor = max(min(power_factor, 1.0), -1.0)
        phase_angle_radians = math.acos(power_factor)
        phase_angle_degrees = math.degrees(phase_angle_radians)
        
        return power_factor, phase_angle_degrees
    
    elif method == 'cos':
        if theta is None:
            raise ValueError("Phase angle (theta) must be provided for 'cos' method.")
        
        power_factor = math.cos(math.radians(theta))
        return power_factor, theta
    
    else:
        raise ValueError("Invalid method. Use 'ratio' for P/S or 'cos' for cos(theta).")

def calculate_complex_power(V=None, I=None, P=None, Q=None, theta=None):
    """
    Calculate the complex power given voltage (V), current (I), and optionally the phase angle (theta),
    or given real power (P) and reactive power (Q).
    
    Parameters:
    V (float): Voltage in volts (V), required if P and Q are not provided
    I (float): Current in amperes (A), required if P and Q are not provided
    P (float): Real power in watts (W), required if V and I are not provided
    Q (float): Reactive power in VAR (var), required if V and I are not provided
    theta (float): Phase angle in degrees (optional)
    
    Returns:
    complex: Complex power (S) as a complex number
    """
    if V is not None and I is not None:
        if theta is not None:
            # Calculate complex power using phase angle
            theta_radians = math.radians(theta)
            S = V * I * (cmath.cos(theta_radians) + 1j * cmath.sin(theta_radians))
        else:
            # Calculate complex power without phase angle
            S = V * I
    elif P is not None and Q is not None:
        # Calculate complex power using real power and reactive power
        S = complex(P, Q)
    else:
        raise ValueError("Either V and I, or P and Q must be provided.")
    
    return S

def two_wattmeter_method(W1, W2):
    """
    Calculate the total power (P), reactive power (Q), and apparent power (S) using the Two-Wattmeter Method.
    
    Parameters:
    W1 (float): Power measured by the first wattmeter (W1)
    W2 (float): Power measured by the second wattmeter (W2)
    
    Returns:
    tuple: Total power (P), reactive power (Q), and apparent power (S)
    """
    P = W1 + W2
    Q = math.sqrt((W1 - W2) ** 2)
    S = math.sqrt(P ** 2 + Q ** 2)
    
    return P, Q, S

def power_triangle(S=None, P=None, Q=None):
    """
    Calculate the sides of the power triangle given any two of the values S (apparent power), P (real power), and Q (reactive power).
    
    Parameters:
    S (float): Apparent power in volt-amperes (VA), optional if P and Q are provided
    P (float): Real power in watts (W), optional if S and Q are provided
    Q (float): Reactive power in VAR (var), optional if S and P are provided
    
    Returns:
    tuple: Apparent power (S), real power (P), and reactive power (Q)
    """
    if S is None:
        if P is None or Q is None:
            raise ValueError("Either S, or both P and Q must be provided.")
        S = math.sqrt(P ** 2 + Q ** 2)
    elif P is None:
        if S is None or Q is None:
            raise ValueError("Either P, or both S and Q must be provided.")
        P = math.sqrt(S ** 2 - Q ** 2)
    elif Q is None:
        if S is None or P is None:
            raise ValueError("Either Q, or both S and P must be provided.")
        Q = math.sqrt(S ** 2 - P ** 2)
    
    return S, P, Q

def calculate_ct_ratio(primary_current, secondary_current):
    """
    Calculate the current transformer ratio (CTR).
    
    Parameters:
    primary_current (float): Primary current in amperes (A)
    secondary_current (float): Secondary current in amperes (A)
    
    Returns:
    float: Current transformer ratio (CTR)
    """
    if secondary_current == 0:
        raise ValueError("Secondary current cannot be zero.")
    
    return primary_current / secondary_current

def select_tap_setting(relay_current, ct_ratio):
    """
    Select the appropriate tap setting for a relay in a protection circuit.
    
    Parameters:
    relay_current (float): Desired relay current in amperes (A)
    ct_ratio (float): Current transformer ratio (CTR)
    
    Returns:
    float: Tap setting
    """
    return relay_current / ct_ratio

def calculate_vt_ratio(primary_voltage, secondary_voltage):
    """
    Calculate the voltage transformer ratio (VTR).
    
    Parameters:
    primary_voltage (float): Primary voltage in volts (V)
    secondary_voltage (float): Secondary voltage in volts (V)
    
    Returns:
    float: Voltage transformer ratio (VTR)
    """
    if secondary_voltage == 0:
        raise ValueError("Secondary voltage cannot be zero.")
    
    return primary_voltage / secondary_voltage

if __name__ == "__main__":
    pass
