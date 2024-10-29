def seats_in_row(N, R, x, min_seats_innermost=24, growth_factor=1.2):
    """
    Calculate the number of seats in a specific row (x) in a semi-circle layout given total seats (N),
    number of rows (R), and the row index (x).
    
    Parameters:
    N (int): Total number of seats.
    R (int): Total number of rows.
    x (int): Row index, where 1 is the innermost row and R is the outermost row.
    min_seats_innermost (int): Minimum seats in the innermost row.
    growth_factor (float): The growth factor for seat progression per row.
    
    Returns:
    float: The approximate number of seats in row x.
    """
    # Calculate normalization factor to ensure seat total matches N
    normalization_factor = N / (min_seats_innermost * (growth_factor**R - 1) / (growth_factor - 1))
    
    # Calculate seats in row x
    seats_in_x = min_seats_innermost * (growth_factor ** (x)) * normalization_factor
    
    return round(seats_in_x)

# Test cases
# Example: total seats N = 2000, total rows R = 7, test for various x values
N, R = 2000, 7
test_results = [seats_in_row(N, R, x) for x in range(1, R + 1)]
test_results, sum(test_results)

def test(N, R):
    test_results = [seats_in_row(N, R, x) for x in range(0, R)]
    return test_results, sum(test_results)