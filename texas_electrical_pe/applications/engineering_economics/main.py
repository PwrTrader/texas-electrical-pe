import math

def present_worth_cash_flows(cash_flows, interest_rate):
    """
    Calculate the present worth of cash flows.
    
    Parameters:
    cash_flows (list of float): List of cash flows (inflow positive, outflow negative)
    interest_rate (float): Interest rate per period
    
    Returns:
    float: Present worth of cash flows
    """
    present_worth = 0
    for t, cash_flow in enumerate(cash_flows):
        present_worth += cash_flow / ((1 + interest_rate) ** t)
    return present_worth

def future_worth_cash_flows(cash_flows, interest_rate):
    """
    Calculate the future worth of cash flows.
    
    Parameters:
    cash_flows (list of float): List of cash flows (inflow positive, outflow negative)
    interest_rate (float): Interest rate per period
    
    Returns:
    float: Future worth of cash flows
    """
    future_worth = 0
    for t, cash_flow in enumerate(cash_flows):
        future_worth += cash_flow * ((1 + interest_rate) ** (len(cash_flows) - 1 - t))
    return future_worth

def annual_worth_cash_flows(cash_flows, interest_rate):
    """
    Calculate the annual worth of cash flows.
    
    Parameters:
    cash_flows (list of float): List of cash flows (inflow positive, outflow negative)
    interest_rate (float): Interest rate per period
    
    Returns:
    float: Annual worth of cash flows
    """
    n = len(cash_flows)
    present_worth = present_worth_cash_flows(cash_flows, interest_rate)
    annual_worth = present_worth * (interest_rate * (1 + interest_rate) ** n) / ((1 + interest_rate) ** n - 1)
    return annual_worth

def straight_line_depreciation(initial_cost, salvage_value, useful_life):
    """
    Calculate straight-line depreciation.
    
    Parameters:
    initial_cost (float): Initial cost of the asset
    salvage_value (float): Salvage value of the asset
    useful_life (float): Useful life of the asset in years
    
    Returns:
    float: Annual depreciation amount
    """
    return (initial_cost - salvage_value) / useful_life

def declining_balance_depreciation(initial_cost, salvage_value, useful_life, rate):
    """
    Calculate declining balance depreciation.
    
    Parameters:
    initial_cost (float): Initial cost of the asset
    salvage_value (float): Salvage value of the asset
    useful_life (float): Useful life of the asset in years
    rate (float): Depreciation rate
    
    Returns:
    list of float: Depreciation amounts per year
    """
    depreciation_amounts = []
    book_value = initial_cost
    for year in range(1, useful_life + 1):
        depreciation = book_value * rate
        if book_value - depreciation < salvage_value:
            depreciation = book_value - salvage_value
        depreciation_amounts.append(depreciation)
        book_value -= depreciation
        if book_value <= salvage_value:
            break
    return depreciation_amounts

def nomenclature():
    """
    Return a dictionary of common engineering economics nomenclature.
    
    Returns:
    dict: Dictionary of nomenclature
    """
    return {
        'P': 'Present worth',
        'F': 'Future worth',
        'A': 'Annual worth',
        'i': 'Interest rate',
        'n': 'Number of periods',
        'd': 'Depreciation',
        'SV': 'Salvage value',
        'IC': 'Initial cost'
    }

def cash_flow_diagram(cash_flows):
    """
    Generate a cash flow diagram.
    
    Parameters:
    cash_flows (list of float): List of cash flows (inflow positive, outflow negative)
    
    Returns:
    str: Cash flow diagram
    """
    diagram = "Time:   " + " ".join([f"{t:>6}" for t in range(len(cash_flows))]) + "\n"
    diagram += "Cash:   " + " ".join([f"{cf:>6.2f}" for cf in cash_flows]) + "\n"
    return diagram

def single_payment_compound_amount(P, i, n):
    """
    Calculate the future value of a single payment using the compound amount formula.
    
    Parameters:
    P (float): Present value
    i (float): Interest rate per period
    n (int): Number of periods
    
    Returns:
    float: Future value
    """
    return P * (1 + i) ** n

def single_payment_present_worth(F, i, n):
    """
    Calculate the present value of a single payment using the present worth formula.
    
    Parameters:
    F (float): Future value
    i (float): Interest rate per period
    n (int): Number of periods
    
    Returns:
    float: Present value
    """
    return F / (1 + i) ** n

def uniform_series_sinking_fund(F, i, n):
    """
    Calculate the annual payment using the sinking fund formula.
    
    Parameters:
    F (float): Future value
    i (float): Interest rate per period
    n (int): Number of periods
    
    Returns:
    float: Annual payment
    """
    return F * (i / ((1 + i) ** n - 1))

def capital_recovery(P, i, n):
    """
    Calculate the annual payment using the capital recovery formula.
    
    Parameters:
    P (float): Present value
    i (float): Interest rate per period
    n (int): Number of periods
    
    Returns:
    float: Annual payment
    """
    return P * (i * (1 + i) ** n) / ((1 + i) ** n - 1)

def uniform_series_compound_amount(A, i, n):
    """
    Calculate the future value of a uniform series using the compound amount formula.
    
    Parameters:
    A (float): Annual payment
    i (float): Interest rate per period
    n (int): Number of periods
    
    Returns:
    float: Future value
    """
    return A * (((1 + i) ** n - 1) / i)

def uniform_series_present_worth(A, i, n):
    """
    Calculate the present value of a uniform series using the present worth formula.
    
    Parameters:
    A (float): Annual payment
    i (float): Interest rate per period
    n (int): Number of periods
    
    Returns:
    float: Present value
    """
    return A * (((1 + i) ** n - 1) / (i * (1 + i) ** n))

def uniform_gradient_present_worth(G, i, n):
    """
    Calculate the present value of a uniform gradient using the present worth formula.
    
    Parameters:
    G (float): Gradient payment
    i (float): Interest rate per period
    n (int): Number of periods
    
    Returns:
    float: Present value
    """
    return G * ((1 / i) - (n / ((1 + i) ** n - 1)))

def uniform_gradient_future_worth(G, i, n):
    """
    Calculate the future value of a uniform gradient using the future worth formula.
    
    Parameters:
    G (float): Gradient payment
    i (float): Interest rate per period
    n (int): Number of periods
    
    Returns:
    float: Future value
    """
    return G * (((1 + i) ** n - 1 - i * n) / (i ** 2))

def uniform_gradient_uniform_series(G, i, n):
    """
    Calculate the annual payment of a uniform gradient using the uniform series formula.
    
    Parameters:
    G (float): Gradient payment
    i (float): Interest rate per period
    n (int): Number of periods
    
    Returns:
    float: Annual payment
    """
    return G * (((1 + i) ** n - 1) / (i * (1 + i) ** n) - (n / ((1 + i) ** n - 1)))

def non_annual_compounding(P, i, n, m):
    """
    Calculate the future value with non-annual compounding.
    
    Parameters:
    P (float): Present value
    i (float): Nominal annual interest rate
    n (int): Number of years
    m (int): Number of compounding periods per year
    
    Returns:
    float: Future value
    """
    return P * (1 + i / m) ** (n * m)

def inflation_adjusted_value(P, f, n):
    """
    Calculate the inflation-adjusted value.
    
    Parameters:
    P (float): Present value
    f (float): Inflation rate per period
    n (int): Number of periods
    
    Returns:
    float: Inflation-adjusted value
    """
    return P * (1 + f) ** n

def modified_accelerated_cost_recovery_system(initial_cost, years):
    """
    Calculate the depreciation using the Modified Accelerated Cost Recovery System (MACRS).
    
    Parameters:
    initial_cost (float): Initial cost of the asset
    years (int): Number of years
    
    Returns:
    list of float: Depreciation amounts per year
    """
    macrs_rates = [0.2, 0.32, 0.192, 0.1152, 0.1152, 0.0576]  # Example rates for 5-year property
    if years != len(macrs_rates):
        raise ValueError("Unsupported number of years for MACRS.")
    
    depreciation_amounts = [initial_cost * rate for rate in macrs_rates]
    return depreciation_amounts

def book_value(initial_cost, depreciation_amounts, year):
    """
    Calculate the book value of an asset after a certain number of years.
    
    Parameters:
    initial_cost (float): Initial cost of the asset
    depreciation_amounts (list of float): List of annual depreciation amounts
    year (int): Number of years
    
    Returns:
    float: Book value of the asset
    """
    if year > len(depreciation_amounts):
        raise ValueError("Year exceeds the number of depreciation periods.")
    
    return initial_cost - sum(depreciation_amounts[:year])

def benefit_cost_analysis(benefits, costs):
    """
    Calculate the benefit-cost ratio.
    
    Parameters:
    benefits (list of float): List of benefits
    costs (list of float): List of costs
    
    Returns:
    float: Benefit-cost ratio
    """
    if sum(costs) == 0:
        raise ValueError("Total costs cannot be zero.")
    
    return sum(benefits) / sum(costs)

if __name__ == "__main__":
    pass
