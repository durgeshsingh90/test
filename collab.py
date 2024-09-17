from django.shortcuts import render, redirect  # Import redirect

def bin_blocking_editor(request):
    if request.method == 'POST':
        # Get user inputs
        bin_input = request.POST.get('bins', '').splitlines()
        blocked_item = request.POST.get('blocked_item')

        # Process BIN numbers
        processed_bins = process_bins(bin_input)

        # Calculate neighbors for processed bins
        bins_with_neighbors = calculate_bins_with_neighbors(processed_bins)

        # Load the generated Prod SQL statements
        prod_sql_statements = generate_sql_insert_statements_for_prod()

        # Process Prod SQL statements
        prod_modified_sql, prod_remaining_sql = duplicate_and_modify_sql(
            prod_sql_statements, bins_with_neighbors, blocked_item
        )
        prod_merged_sorted_sql = merge_and_sort_sql(prod_modified_sql, prod_remaining_sql)

        # Save the new merged insert statements
        save_sql_statements_to_file(prod_merged_sorted_sql, os.path.join(OUTPUT_DIR, 'final_prod_insert_statements.sql'))

        # Load the contents of the output files
        with open(os.path.join(OUTPUT_DIR, 'prod_insert_statements.sql'), 'r') as file:
            production_data = file.read()

        with open(os.path.join(OUTPUT_DIR, 'uat_insert_statements.sql'), 'r') as file:
            uat_data = file.read()

        with open(os.path.join(OUTPUT_DIR, 'final_prod_insert_statements.sql'), 'r') as file:
            insert_statement = file.read()

        context = {
            'processed_bins': processed_bins,
            'production_data': production_data,
            'uat_data': uat_data,
            'insert_statement': insert_statement,
            'prod_distinct_list': prod_distinct_list,
        }

        # Render the output page with the context data
        return render(request, 'binblock/binblocker_output.html', context)

    # Render the bin blocker page initially
    context = {
        'result': None,
        'prod_distinct_list': prod_distinct_list
    }
    return render(request, 'binblock/binblocker.html', context)
