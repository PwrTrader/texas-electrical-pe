import math

def permissible_body_current_limit(body_weight, duration):
    """
    Calculate the permissible body current limit.
    
    Parameters:
    body_weight (float): Body weight in kg
    duration (float): Duration in seconds
    
    Returns:
    float: Permissible body current limit in amperes (A)
    """
    return 0.116 / math.sqrt(body_weight) * math.sqrt(duration)

def maximum_allowable_step_voltage(current, step_resistance):
    """
    Calculate the maximum allowable step voltage.
    
    Parameters:
    current (float): Body current in amperes (A)
    step_resistance (float): Step resistance in ohms (Ω)
    
    Returns:
    float: Maximum allowable step voltage in volts (V)
    """
    return current * step_resistance

def maximum_allowable_touch_voltage(current, touch_resistance):
    """
    Calculate the maximum allowable touch voltage.
    
    Parameters:
    current (float): Body current in amperes (A)
    touch_resistance (float): Touch resistance in ohms (Ω)
    
    Returns:
    float: Maximum allowable touch voltage in volts (V)
    """
    return current * touch_resistance

def min_substation_grounding_resistance_uniform_soil(depth, resistivity):
    """
    Calculate the minimum value of substation grounding resistance in uniform soil for grounding depth less than 0.25m.
    
    Parameters:
    depth (float): Grounding depth in meters (m)
    resistivity (float): Soil resistivity in ohm-meters (Ω⋅m)
    
    Returns:
    float: Minimum grounding resistance in ohms (Ω)
    """
    return resistivity / (4 * math.pi * depth)

def upper_limit_substation_grounding_resistance_uniform_soil(depth, resistivity):
    """
    Calculate the upper limit of substation grounding resistance in uniform soil for grounding grid depth less than 0.25m.
    
    Parameters:
    depth (float): Grounding depth in meters (m)
    resistivity (float): Soil resistivity in ohm-meters (Ω⋅m)
    
    Returns:
    float: Upper limit grounding resistance in ohms (Ω)
    """
    return 2 * resistivity / (4 * math.pi * depth)

def substation_grounding_grid_resistance(depth, resistivity):
    """
    Calculate the substation grounding grid resistance for grid depths between 0.25m and 2.5m.
    
    Parameters:
    depth (float): Grid depth in meters (m)
    resistivity (float): Soil resistivity in ohm-meters (Ω⋅m)
    
    Returns:
    float: Grounding grid resistance in ohms (Ω)
    """
    return resistivity / (4 * math.pi * depth) * (1 + (depth / (2.5 - depth)))

def total_resistance_horizontal_grid_vertical_rods(grid_resistance, rod_resistance):
    """
    Calculate the total resistance of a system consisting of a combination of horizontal grid and vertical rods.
    
    Parameters:
    grid_resistance (float): Horizontal grid resistance in ohms (Ω)
    rod_resistance (float): Vertical rod resistance in ohms (Ω)
    
    Returns:
    float: Total system resistance in ohms (Ω)
    """
    return (grid_resistance * rod_resistance) / (grid_resistance + rod_resistance)

def resistance_single_ground_rod(length, diameter, resistivity):
    """
    Calculate the resistance of a single ground rod.
    
    Parameters:
    length (float): Length of the rod in meters (m)
    diameter (float): Diameter of the rod in meters (m)
    resistivity (float): Soil resistivity in ohm-meters (Ω⋅m)
    
    Returns:
    float: Ground rod resistance in ohms (Ω)
    """
    return (resistivity / (2 * math.pi * length)) * math.log(4 * length / diameter)

def effective_resistance_vertical_rod_concrete(length, diameter, resistivity, concrete_resistivity):
    """
    Calculate the effective resistance of a vertical rod encased in concrete.
    
    Parameters:
    length (float): Length of the rod in meters (m)
    diameter (float): Diameter of the rod in meters (m)
    resistivity (float): Soil resistivity in ohm-meters (Ω⋅m)
    concrete_resistivity (float): Concrete resistivity in ohm-meters (Ω⋅m)
    
    Returns:
    float: Effective resistance in ohms (Ω)
    """
    return (resistivity / (2 * math.pi * length)) * math.log(4 * length / diameter) + (concrete_resistivity / (2 * math.pi * length)) * math.log(4 * length / diameter)

if __name__ == "__main__":
    pass
