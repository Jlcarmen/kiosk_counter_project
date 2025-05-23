def session_counter():
    """Simulates a session-specific counter that resets for each customer."""
    counter = 0  # Local variable resets every time the function is called
    counter += 1
    print(f"Session visits: {counter}")

def kiosk_usage():
    """Simulates a global usage counter that keeps a running total of users served."""
    # Initialize the static-like variable on the first call
    if not hasattr(kiosk_usage, "total_users"):
        kiosk_usage.total_users = 0
    # Increment the persistent counter
    kiosk_usage.total_users += 1
    print(f"Total users today: {kiosk_usage.total_users}")

def simulate_customer_sessions(num_customers):
    """Simulates multiple customer sessions using the kiosk system."""
    for i in range(num_customers):
        print("New Customer Session:")
        session_counter()    # Resets for every customer
        kiosk_usage()        # Persists and increments across sessions
        print("-" * 30)

def demonstrate_session_reset(times):
    """Shows that the session counter resets with each function call."""
    print("\nDemonstrating session resets:")
    for _ in range(times):
        session_counter()  # Should always print "Session visits: 1"

def demonstrate_persistent_kiosk_usage(times):
    """Shows that the kiosk usage counter keeps increasing across calls."""
    print("\nDemonstrating persistent kiosk usage:")
    for _ in range(times):
        kiosk_usage()  # Should continue counting from where it left off

# --- Simulate three customers using the kiosk ---
simulate_customer_sessions(3)

# --- Show session counter always resets to 1 ---
demonstrate_session_reset(5)

# --- Show kiosk usage counter continues from previous state ---
demonstrate_persistent_kiosk_usage(5)
