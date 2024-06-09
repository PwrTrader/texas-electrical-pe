import math

def annual_lightning_strike_frequency(Ng, Ae, C):
    """
    Calculate the annual lightning strike frequency to a structure.
    
    Parameters:
    Ng (float): Ground flash density (flashes per square kilometer per year)
    Ae (float): Equivalent collection area in square meters (m²)
    C (float): Environment factor
    
    Returns:
    float: Annual lightning strike frequency
    """
    return Ng * Ae * C

def equivalent_collection_area(length, width, height):
    """
    Calculate the equivalent collection area of a rectangular structure.
    
    Parameters:
    length (float): Length of the structure in meters (m)
    width (float): Width of the structure in meters (m)
    height (float): Height of the structure in meters (m)
    
    Returns:
    float: Equivalent collection area in square meters (m²)
    """
    return length * width + 2 * height * (length + width) + math.pi * height**2

def tolerable_lightning_frequency(Nd, Nc):
    """
    Calculate the tolerable lightning frequency.
    
    Parameters:
    Nd (float): Number of dangerous events per year
    Nc (float): Number of tolerated lightning strikes per year
    
    Returns:
    float: Tolerable lightning frequency
    """
    if Nc == 0:
        raise ValueError("Number of tolerated lightning strikes per year cannot be zero.")
    
    return Nd / Nc

if __name__ == "__main__":
    pass
