def reliability_series(components):
    """
    Calculate the reliability of independent components connected in series.
    
    Parameters:
    components (list of float): List of reliabilities of individual components
    
    Returns:
    float: System reliability
    """
    reliability = 1.0
    for r in components:
        reliability *= r
    return reliability

def reliability_parallel(components):
    """
    Calculate the reliability of independent components connected in parallel.
    
    Parameters:
    components (list of float): List of reliabilities of individual components
    
    Returns:
    float: System reliability
    """
    unreliability = 1.0
    for r in components:
        unreliability *= (1 - r)
    return 1 - unreliability

def mean_time_to_failure(failure_rates):
    """
    Calculate the mean time to failure (MTTF).
    
    Parameters:
    failure_rates (list of float): List of failure rates of individual components
    
    Returns:
    float: Mean time to failure
    """
    total_failure_rate = sum(failure_rates)
    if total_failure_rate == 0:
        raise ValueError("Total failure rate cannot be zero.")
    return 1 / total_failure_rate

def calculate_reliability(mttf, time):
    """
    Calculate the reliability of a system.
    
    Parameters:
    mttf (float): Mean time to failure
    time (float): Time period for which reliability is calculated
    
    Returns:
    float: Reliability
    """
    return math.exp(-time / mttf)

def system_availability(mtbf, mttr):
    """
    Calculate the system availability.
    
    Parameters:
    mtbf (float): Mean time between failures
    mttr (float): Mean time to repair
    
    Returns:
    float: System availability
    """
    if mtbf + mttr == 0:
        raise ValueError("Sum of MTBF and MTTR cannot be zero.")
    return mtbf / (mtbf + mttr)

if __name__ == "__main__":
    pass
