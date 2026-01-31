# Nash Equilibrium Negotiation Logic

def nash_negotiation(player1_range, player2_range):
    """
    Simulate a simple price negotiation using Nash equilibrium.
    Each player proposes a price in their acceptable range.
    Returns the agreed price and both players' utilities.
    """
    # For simplicity, use the midpoint as Nash solution for two-person bargaining
    p1_min, p1_max = player1_range
    p2_min, p2_max = player2_range
    # Overlap check
    agree_min = max(p1_min, p2_min)
    agree_max = min(p1_max, p2_max)
    if agree_min > agree_max:
        return None, (0, 0)  # No agreement possible
    price = (agree_min + agree_max) / 2
    # Utility: difference from their best/worst
    p1_utility = (p1_max - price) / (p1_max - p1_min) if p1_max != p1_min else 0
    p2_utility = (price - p2_min) / (p2_max - p2_min) if p2_max != p2_min else 0
    return price, (p1_utility, p2_utility)
