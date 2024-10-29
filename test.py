import math


def seats_in_row(N, R, x, th=24, growth_factor=1.2):
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
    row_factor = (x)**2   
    numerator = (N - R * th) * 6
    denominator = (R - 1) * R * (2*R-1) 
    # Calculate seats in row x
    seats_in_x = (numerator / denominator) * row_factor + th
    
    return round(seats_in_x)

def distribute_seats_quadratic(N, R, min_seats_innermost=24):
    """
    Distribute seats across rows in a visually balanced manner using a quadratic growth approach.
    
    Parameters:
    N (int): Total number of seats.
    R (int): Number of rows.
    min_seats_innermost (int): Minimum seats in the innermost row.
    
    Returns:
    list: Number of seats per row where outer rows have more seats and inner rows have fewer,
          following a quadratic progression.
    """
    # Calculate the constants a and b for the quadratic growth formula: S(x) = a * (x - 1)^2 + b
    # Set b as the minimum seat count for the innermost row
    b = min_seats_innermost
    
    # Sum of seats if distributed quadratically with a to be determined
    sum_of_squares = sum((i - 1) ** 2 for i in range(1, R + 1))
    
    # Calculate a based on desired total seat count N
    a = (N - R * b) / sum_of_squares
    
    # Calculate seat distribution for each row using the quadratic formula
    seats_per_row = [round(a * (x - 1) ** 2 + b) for x in range(1, R + 1)]
        
    return seats_per_row

def partial_sum_quadratic(N, R, k, min_seats_innermost=24):
    """
    Calculates the partial sum of the quadratic seat distribution up to row k.

    Args:
        N: Total number of seats.
        R: Total number of rows.
        k: The row up to which we want to calculate the sum.
        min_seats_innermost: Minimum seats in the innermost row.

    Returns:
        The total number of seats in the first k rows.
    """

    # Calculate the constants a and b as in the `distribute_seats_quadratic` function
    b = min_seats_innermost
    sum_of_squares = sum((i - 1) ** 2 for i in range(1, R + 1))
    a = (N - R * b) / sum_of_squares

    # Calculate the partial sum using the formula for the sum of squares
    partial_sum = a * sum((i - 1) ** 2 for i in range(1, k + 1)) + k * b

    return round(partial_sum)

# Example usage

# verify if the partial sum of the quadratic distribution up to row k is correct
def verpar(total, k):
    rows = total // 40
    print(partial_sum_quadratic(total, rows, k))
    print(sum(distribute_seats_quadratic(total, rows)[:k]))

def verify(total, row):
    rows = math.ceil(total / 40)
    seats = seats_in_row(total, rows, row)
    print([seats_in_row(total, rows, x) for x in range(0, rows)])
    print(distribute_seats_quadratic(total, rows))
    print(seats, sum([seats_in_row(total, rows, x) for x in range(0, rows)]))