def validate_inputs(pickup, dropoff):
    if not pickup or not dropoff:
        raise ValueError("Pickup and dropoff cannot be empty")
