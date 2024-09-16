def calculate_bins_with_neighbors(processed_bins):
    """
    Calculate the start and end bins for each processed bin range along with neighboring bins.
    """
    result = []

    for bin_range in processed_bins:
        bin_range = bin_range.strip()  # Clean up any extra spaces

        # Check if the bin_range is a range
        if '-' in bin_range:
            start_bin, end_bin = bin_range.split('-')
            start_bin = start_bin.strip().ljust(15, '0')  # Pad the start_bin with '0' to make it 15 characters
            end_bin = end_bin.strip().ljust(15, '9')    # Pad the end_bin with '9' to make it 15 characters

            # Calculate neighbors for the start and end bins
            start_bin_int = int(start_bin.strip())
            end_bin_int = int(end_bin.strip())
            neighbor_minus_1 = str(start_bin_int - 1).ljust(15, '9')  # Decrement start_bin and pad with '9'
            neighbor_plus_1 = str(end_bin_int + 1).ljust(15, '0')   # Increment end_bin and pad with '0'
        else:
            start_bin = end_bin = bin_range.strip()
            start_bin = start_bin.ljust(15, '0')  # Pad the bin with '0' to make it 15 characters
            end_bin = end_bin.ljust(15, '9')     # Pad the bin with '9' to make it 15 characters

            # Calculate neighbors for a single bin
            bin_int = int(bin_range.strip())
            neighbor_minus_1 = str(bin_int - 1).ljust(15, '9')  # Decrement bin and pad with '9'
            neighbor_plus_1 = str(bin_int + 1).ljust(15, '0')   # Increment bin and pad with '0'

        result.append((start_bin, end_bin, neighbor_minus_1, neighbor_plus_1))

    return result
