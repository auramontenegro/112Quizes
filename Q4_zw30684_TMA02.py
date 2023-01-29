# Function to calculate the received frequency of a mobile phone during Doppler shift

def calculate_frequency_fr(car_speed, frequency_transmission, is_towards):
    """calculates the received frequency of a mobile phone during Doppler shift.
car_speed is in m/s, frequency_transmission is in MHz and is_towards is True if the car is moving toward the transmitter, is_towards is
False if the car is moving away the transmitter"""

    # set doppler_shift to the value of the formula applied to the inputs
    doppler_shift = (frequency_transmission * 1000000 * car_speed * 1.01203) / (3 * 100000000)
    
    # if the car is moving towar the transmitter:
    if is_towards == True:
        # add frequency_transmission and doppler_shift to calculate received_frequency
        received_frequency = frequency_transmission + doppler_shift
    # otherwise
    else:
        # subtract doppler_shift from frequency_transmission to calculate received_frequency
        received_frequency = frequency_transmission - doppler_shift
        
    return received_frequency


    

    
    
