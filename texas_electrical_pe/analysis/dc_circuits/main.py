import math
import cmath
import numpy as np

def rc_circuit_transient_capacitor_voltage(V0, R, C, t):
    """
    Calculate the transient voltage across the capacitor in an RC circuit.
    
    Parameters:
    V0 (float): Initial voltage across the capacitor
    R (float): Resistance in ohms (Ω)
    C (float): Capacitance in farads (F)
    t (float): Time in seconds (s)
    
    Returns:
    float: Voltage across the capacitor at time t
    """
    tau = R * C
    return V0 * math.exp(-t / tau)

def rc_circuit_transient_current(V0, R, C, t):
    """
    Calculate the transient current in an RC circuit.
    
    Parameters:
    V0 (float): Initial voltage across the capacitor
    R (float): Resistance in ohms (Ω)
    C (float): Capacitance in farads (F)
    t (float): Time in seconds (s)
    
    Returns:
    float: Current at time t
    """
    tau = R * C
    return (V0 / R) * math.exp(-t / tau)

def rc_circuit_transient_resistor_voltage(V0, R, C, t):
    """
    Calculate the transient voltage across the resistor in an RC circuit.
    
    Parameters:
    V0 (float): Initial voltage across the capacitor
    R (float): Resistance in ohms (Ω)
    C (float): Capacitance in farads (F)
    t (float): Time in seconds (s)
    
    Returns:
    float: Voltage across the resistor at time t
    """
    return V0 - rc_circuit_transient_capacitor_voltage(V0, R, C, t)

def rl_circuit_transient_current(V0, R, L, t):
    """
    Calculate the transient current in an RL circuit.
    
    Parameters:
    V0 (float): Initial voltage across the inductor
    R (float): Resistance in ohms (Ω)
    L (float): Inductance in henries (H)
    t (float): Time in seconds (s)
    
    Returns:
    float: Current at time t
    """
    tau = L / R
    return (V0 / R) * (1 - math.exp(-t / tau))

def rl_circuit_transient_resistor_voltage(V0, R, L, t):
    """
    Calculate the transient voltage across the resistor in an RL circuit.
    
    Parameters:
    V0 (float): Initial voltage across the inductor
    R (float): Resistance in ohms (Ω)
    L (float): Inductance in henries (H)
    t (float): Time in seconds (s)
    
    Returns:
    float: Voltage across the resistor at time t
    """
    I_t = rl_circuit_transient_current(V0, R, L, t)
    return I_t * R

def rl_circuit_transient_inductor_voltage(V0, R, L, t):
    """
    Calculate the transient voltage across the inductor in an RL circuit.
    
    Parameters:
    V0 (float): Initial voltage across the inductor
    R (float): Resistance in ohms (Ω)
    L (float): Inductance in henries (H)
    t (float): Time in seconds (s)
    
    Returns:
    float: Voltage across the inductor at time t
    """
    return V0 - rl_circuit_transient_resistor_voltage(V0, R, L, t)

def resistance(voltage, current):
    """
    Calculate the resistance using Ohm's law.
    
    Parameters:
    voltage (float): Voltage in volts (V)
    current (float): Current in amperes (A)
    
    Returns:
    float: Resistance in ohms (Ω)
    """
    return voltage / current

def equivalent_resistance_series(resistors):
    """
    Calculate the equivalent resistance for resistors in series.
    
    Parameters:
    resistors (list of float): List of resistances in ohms (Ω)
    
    Returns:
    float: Equivalent resistance in ohms (Ω)
    """
    return sum(resistors)

def equivalent_resistance_parallel(resistors):
    """
    Calculate the equivalent resistance for resistors in parallel.
    
    Parameters:
    resistors (list of float): List of resistances in ohms (Ω)
    
    Returns:
    float: Equivalent resistance in ohms (Ω)
    """
    return 1 / sum(1 / R for R in resistors)

def ohms_law(voltage=None, current=None, resistance=None):
    """
    Calculate one of the variables using Ohm's law.
    
    Parameters:
    voltage (float): Voltage in volts (V) (optional)
    current (float): Current in amperes (A) (optional)
    resistance (float): Resistance in ohms (Ω) (optional)
    
    Returns:
    float: Calculated value (voltage, current, or resistance)
    """
    if voltage is not None and current is not None:
        return voltage / current  # Calculate resistance
    elif voltage is not None and resistance is not None:
        return voltage / resistance  # Calculate current
    elif current is not None and resistance is not None:
        return current * resistance  # Calculate voltage
    else:
        raise ValueError("Two parameters must be provided")

def kirchhoffs_current_law(currents):
    """
    Verify Kirchhoff's Current Law (KCL) by summing currents at a node.
    
    Parameters:
    currents (list of float): List of currents entering (+) or leaving (-) a node
    
    Returns:
    float: Sum of currents (should be close to 0)
    """
    return sum(currents)

def kirchhoffs_voltage_law(voltages):
    """
    Verify Kirchhoff's Voltage Law (KVL) by summing voltages around a loop.
    
    Parameters:
    voltages (list of float): List of voltages in the loop
    
    Returns:
    float: Sum of voltages (should be close to 0)
    """
    return sum(voltages)

def thevenin_equivalent(voltage, resistance):
    """
    Calculate the Thevenin equivalent voltage and resistance.
    
    Parameters:
    voltage (float): Voltage in volts (V)
    resistance (float): Resistance in ohms (Ω)
    
    Returns:
    tuple: Thevenin equivalent voltage and resistance
    """
    return voltage, resistance

def norton_equivalent(current, resistance):
    """
    Calculate the Norton equivalent current and resistance.
    
    Parameters:
    current (float): Current in amperes (A)
    resistance (float): Resistance in ohms (Ω)
    
    Returns:
    tuple: Norton equivalent current and resistance
    """
    return current, resistance

def node_voltage_method(nodes, admittance_matrix, current_vector):
    """
    Solve for node voltages using the node voltage method.
    
    Parameters:
    nodes (list of str): List of node names
    admittance_matrix (2D list): Admittance matrix (Y-matrix)
    current_vector (list of float): Current vector
    
    Returns:
    dict: Node voltages
    """
    Y = np.array(admittance_matrix)
    I = np.array(current_vector)
    V = np.linalg.solve(Y, I)
    return {nodes[i]: V[i] for i in range(len(nodes))}

def superposition(circuits, sources):
    """
    Apply the superposition theorem to solve a linear circuit with multiple sources.
    
    Parameters:
    circuits (list of callable): List of functions representing individual circuits
    sources (list of float): List of source values
    
    Returns:
    float: Total response of the circuit
    """
    return sum(circuit(source) for circuit, source in zip(circuits, sources))

if __name__ == "__main__":
    pass
