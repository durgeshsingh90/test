def bin_blocking_editor(request):
    logger.info("Bin blocking editor view accessed")
    result = None
    log_with_delays = None
    prod_distinct_list = []

    try:
        distinct_command = "sqlplus oasis77/ist0py@istu2"
        distinct_query = "SELECT DISTINCT description FROM oasis77.SHCEXTBINDB ORDER BY DESCRIPTION;"
        distinct_output_file = os.path.join(OUTPUT_DIR, 'prod_distinct_output.txt')
        run_sqlplus_command(distinct_command, distinct_query, distinct_output_file, "Distinct")

        prod_distinct_list = clean_distinct_file(distinct_output_file)
        categorized_list, _ = categorize_and_expand_items(prod_distinct_list)

        run_background_queries()

    except Exception as e:
        logger.error(f"Error running distinct query: {e}")
        categorized_list = []

    if request.method == 'POST':
        # Get user inputs
        bin_input = request.POST.get('bins', '').splitlines()
        blocked_item = request.POST.get('blocked_item')
        search_items = request.POST.getlist('search_items')

        # Process BIN numbers
        processed_bins = process_bins(bin_input)
        logger.info(f"Processed BINs: {processed_bins}")

        # Other processing (e.g., logging user selections)
        _, expanded_search_items = categorize_and_expand_items(prod_distinct_list, search_items)
        logger.info(f"User selected blocked item: {blocked_item} and expanded search items: {expanded_search_items}")

        context = {
            'result': processed_bins,
            'log_with_delays': log_with_delays,
            'prod_distinct_list': categorized_list
        }
        logger.info("Rendering binblocker.html with context data after processing")
        return render(request, 'binblock/binblocker.html', context)

    context = {
        'result': result,
        'log_with_delays': log_with_delays,
        'prod_distinct_list': categorized_list
    }
    logger.info("Rendering binblocker.html with initial context data")
    return render(request, 'binblock/binblocker.html', context)


def process_bins(bins):
    """Process BIN numbers to remove duplicates, handle subsets, and combine consecutive ranges."""
    logger.debug("Starting to process BIN numbers")

    # Convert input into a sorted list of unique BINs
    bins = sorted(set(int(bin.strip()) for bin in bins if bin.strip().isdigit()))
    
    # Check if bins list is empty
    if not bins:
        logger.info("No BIN numbers provided by the user.")
        return ["No BIN numbers provided."]

    logger.debug(f"Sorted and deduplicated BINs: {bins}")

    # Combine consecutive bins into ranges
    combined_bins = []
    start = bins[0]
    previous = bins[0]

    for current in bins[1:]:
        if current == previous + 1:
            previous = current
        else:
            if start == previous:
                combined_bins.append(str(start))
            else:
                combined_bins.append(f"{start}-{previous}")
            start = current
            previous = current

    # Add the final range or bin
    if start == previous:
        combined_bins.append(str(start))
    else:
        combined_bins.append(f"{start}-{previous}")

    # Log the processed bins
    logger.info(f"Processed BINs: {combined_bins}")

    return combined_bins
