def annual_load_factor(average_load, peak_load):
    """
    Calculate the annual load factor.
    
    Parameters:
    average_load (float): Average load in kW
    peak_load (float): Peak load in kW
    
    Returns:
    float: Annual load factor
    """
    if peak_load == 0:
        raise ValueError("Peak load cannot be zero.")
    
    return average_load / peak_load

def coincidence_factor(peak_demand_combined, sum_individual_peaks):
    """
    Calculate the coincidence factor.
    
    Parameters:
    peak_demand_combined (float): Combined peak demand in kW
    sum_individual_peaks (float): Sum of individual peak demands in kW
    
    Returns:
    float: Coincidence factor
    """
    if sum_individual_peaks == 0:
        raise ValueError("Sum of individual peaks cannot be zero.")
    
    return peak_demand_combined / sum_individual_peaks

def demand_utilization_factor(connected_load, actual_load):
    """
    Calculate the demand and utilization factor.
    
    Parameters:
    connected_load (float): Connected load in kW
    actual_load (float): Actual load in kW
    
    Returns:
    float: Utilization factor
    """
    if connected_load == 0:
        raise ValueError("Connected load cannot be zero.")
    
    return actual_load / connected_load

def diversity_factor(sum_individual_peaks, peak_demand_combined):
    """
    Calculate the diversity factor.
    
    Parameters:
    sum_individual_peaks (float): Sum of individual peak demands in kW
    peak_demand_combined (float): Combined peak demand in kW
    
    Returns:
    float: Diversity factor
    """
    if peak_demand_combined == 0:
        raise ValueError("Combined peak demand cannot be zero.")
    
    return sum_individual_peaks / peak_demand_combined

def loss_factor(average_loss, peak_loss):
    """
    Calculate the loss factor.
    
    Parameters:
    average_loss (float): Average loss in kW
    peak_loss (float): Peak loss in kW
    
    Returns:
    float: Loss factor
    """
    if peak_loss == 0:
        raise ValueError("Peak loss cannot be zero.")
    
    return average_loss / peak_loss

def plant_factor(actual_output, maximum_output):
    """
    Calculate the plant factor.
    
    Parameters:
    actual_output (float): Actual output in kWh
    maximum_output (float): Maximum possible output in kWh
    
    Returns:
    float: Plant factor
    """
    if maximum_output == 0:
        raise ValueError("Maximum output cannot be zero.")
    
    return actual_output / maximum_output

if __name__ == "__main__":
    pass
