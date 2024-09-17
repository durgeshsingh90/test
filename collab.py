<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Workflow Steps</title>
<!-- Bootstrap CSS -->
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
<style>
  body {
    background-color: #121212;
    color: #e0e0e0;
  }
  .container {
    margin-top: 20px;
  }
  .copy-btn {
    margin-top: 10px;
  }
  .copied-btn {
    background-color: green;
    color: white;
  }
  .textarea-container {
    display: flex;
    width: 100%;
    position: relative;
  }
  .line-numbers {
    padding: 10px;
    background: #1e1e1e;
    border-right: 1px solid #ddd;
    text-align: right;
    user-select: none;
    color: #888;
    min-width: 40px;
    height: 250px;
    overflow: hidden;
  }
  .textarea {
    width: 100%;
    border: none;
    resize: none;
    padding: 10px;
    font-family: monospace;
    white-space: pre;
    background: #1e1e1e;
    color: #e0e0e0;
    height: 250px;
    overflow-y: scroll;
    margin-left: -1px;
  }
  .textarea:focus {
    outline: none;
  }
  .status-bar {
    background: #1e1e1e;
    border-top: 1px solid #ddd;
    padding: 5px;
    font-size: 12px;
    color: #888;
    display: flex;
    justify-content: space-between;
  }
</style>
</head>
<body>
<div class="container">
  <div class="row g-3">
    <div class="col-md-6">
      <div class="card bg-dark text-white">
        <div class="card-body">
          <h5 class="card-title">1. Processed Bins</h5>
          <div class="textarea-container">
            <div id="lineNumbers1" class="line-numbers"></div>
            <textarea id="processedBins" class="form-control textarea" rows="12" placeholder="Enter details..." oninput="updateLineNumbers(this, 'lineNumbers1')">{{ processed_bins }}</textarea>          
          </div>
          <div id="statusBar1" class="status-bar">Total Lines: 0 | Selected: 0 characters</div>
          <button onclick="copyText('processedBins', this)" class="btn btn-primary copy-btn">Copy</button>
        </div>        
      </div>
    </div>
    <!-- Repeat similar structure for Production Data, UAT Data, and Insert Statement sections -->
  </div>
</div>
<!-- JavaScript functions as needed -->
</body>
</html>




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

        # Load the generated Prod SQL statements (assume they are stored in a list or file)
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
