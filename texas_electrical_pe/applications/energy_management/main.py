def efficiency(output_energy, input_energy):
    """
    Calculate the efficiency of a system.
    
    Parameters:
    output_energy (float): Output energy in joules (J)
    input_energy (float): Input energy in joules (J)
    
    Returns:
    float: Efficiency as a percentage
    """
    if input_energy == 0:
        raise ValueError("Input energy cannot be zero.")
    
    return (output_energy / input_energy) * 100

def energy_conversion(value, from_unit, to_unit):
    """
    Convert energy between different units.
    
    Parameters:
    value (float): Value of energy to be converted
    from_unit (str): Current unit of energy
    to_unit (str): Desired unit of energy
    
    Returns:
    float: Converted energy value
    """
    units = {
        'J': 1,
        'kJ': 1e3,
        'MJ': 1e6,
        'GJ': 1e9,
        'Wh': 3600,
        'kWh': 3.6e6,
        'MWh': 3.6e9,
        'GWh': 3.6e12,
        'BTU': 1055.06,
        'kBTU': 1055.06e3
    }
    
    if from_unit not in units or to_unit not in units:
        raise ValueError("Invalid unit for conversion.")
    
    return value * (units[to_unit] / units[from_unit])

def power_conversion(value, from_unit, to_unit):
    """
    Convert power between different units.
    
    Parameters:
    value (float): Value of power to be converted
    from_unit (str): Current unit of power
    to_unit (str): Desired unit of power
    
    Returns:
    float: Converted power value
    """
    units = {
        'W': 1,
        'kW': 1e3,
        'MW': 1e6,
        'GW': 1e9,
        'hp': 745.7
    }
    
    if from_unit not in units or to_unit not in units:
        raise ValueError("Invalid unit for conversion.")
    
    return value * (units[to_unit] / units[from_unit])

def doubling_time(growth_rate):
    """
    Calculate the doubling time given the growth rate.
    
    Parameters:
    growth_rate (float): Growth rate as a percentage
    
    Returns:
    float: Doubling time in years
    """
    if growth_rate <= 0:
        raise ValueError("Growth rate must be greater than zero.")
    
    return 70 / growth_rate

def per_unit_growth_rate(initial_value, final_value, periods):
    """
    Calculate the per-unit growth rate.
    
    Parameters:
    initial_value (float): Initial value
    final_value (float): Final value
    periods (int): Number of periods
    
    Returns:
    float: Per-unit growth rate
    """
    if initial_value == 0 or periods == 0:
        raise ValueError("Initial value and periods must be greater than zero.")
    
    return ((final_value / initial_value) ** (1 / periods)) - 1

if __name__ == "__main__":
    pass
