def bin_blocking_editor(request):
    logger.info("Bin blocking editor view accessed")
    result = None
    log_with_delays = None
    prod_distinct_list = []
    categorized_list = []
    processed_bins = []  # To store processed bins
    bins_with_neighbors = []  # To store bins with neighbors
    prod_sql_statements = []  # Production SQL insert statements
    uat_sql_statements = []  # UAT SQL insert statements
    prod_merged_sorted_sql = []  # Final merged production SQL insert statements

    try:
        distinct_command = "sqlplus oasis77/ist0py@istu2"
        distinct_query = "SELECT DISTINCT description FROM oasis77.SHCEXTBINDB ORDER BY DESCRIPTION;"
        distinct_output_file = os.path.join(OUTPUT_DIR, 'prod_distinct_output.txt')
        run_sqlplus_command(distinct_command, distinct_query, distinct_output_file, "Distinct")

        prod_distinct_list = clean_distinct_file(distinct_output_file)

        logger.info(f"prod_distinct_list: {prod_distinct_list}")  # Debug log to check the list

        run_background_queries()

    except Exception as e:
        logger.error(f"Error running distinct query: {e}")
        categorized_list = []

    if request.method == 'POST':
        # Get user inputs
        bin_input = request.POST.get('bins', '').splitlines()
        blocked_item = request.POST.get('blocked_item')

        # Log the blocked_item to see if it's captured correctly
        logger.info(f"Blocked Item selected: {blocked_item}")

        # Process BIN numbers
        processed_bins = process_bins(bin_input)
        logger.info(f"Processed BINs: {processed_bins}")

        # Calculate neighbors for processed bins
        bins_with_neighbors = calculate_bins_with_neighbors(processed_bins)
        logger.info(f"Bins with neighbors: {bins_with_neighbors}")

        # Load the generated Prod SQL statements
        prod_sql_statements = generate_sql_insert_statements_for_prod()
        uat_sql_statements = generate_sql_insert_statements_for_uat()  # Assuming you have a similar function for UAT

        # Process Prod SQL statements
        prod_modified_sql, prod_remaining_sql = duplicate_and_modify_sql(
            prod_sql_statements, bins_with_neighbors, blocked_item
        )
        prod_merged_sorted_sql = merge_and_sort_sql(prod_modified_sql, prod_remaining_sql)

        # Save the new merged insert statements
        save_sql_statements_to_file(prod_merged_sorted_sql, os.path.join(OUTPUT_DIR, 'final_prod_insert_statements.sql'))

        # Log final merged SQL statements for Prod
        logger.info(f"Final merged Prod SQL statements: {prod_merged_sorted_sql}")

        # Prepare context for rendering the output page
        context = {
            'processed_bins': '\n'.join(processed_bins),  # Convert to string format
            'production_data': '\n'.join(prod_sql_statements),  # Convert to string format
            'uat_data': '\n'.join(uat_sql_statements),  # Convert to string format
            'insert_statement': '\n'.join(prod_merged_sorted_sql)  # Convert to string format
        }
        logger.info("Rendering binblocker_output.html with processed data context")
        return render(request, 'binblocker_output.html', context)

    # Render initial form or page if GET request or processing fails
    context = {
        'result': result,
        'log_with_delays': log_with_delays,
        'prod_distinct_list': prod_distinct_list  # Correctly pass the prod_distinct_list
    }
    logger.info("Rendering binblocker.html with initial context data")
    return render(request, 'binblock/binblocker.html', context)
