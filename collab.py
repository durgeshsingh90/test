{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bin Blocking Editor</title>
    <!-- Bootstrap CSS from CDN -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <!-- CodeMirror CSS from CDN -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.5/codemirror.min.css">
    <!-- CodeMirror Theme (optional) -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.5/theme/monokai.min.css">
    <!-- Custom CSS -->
    <link rel="stylesheet" href="{% static 'binblock/styles.css' %}">
</head>
<body>
    <div class="container py-4">
        <div class="row">
            <div class="col-lg-8 mb-4">
                <div class="editor-container">
                    <h1 class="form-title">Bin Blocking Editor</h1>
                    <form method="POST" action="{% url 'binblock:binblocking_editor' %}">
                        {% csrf_token %}
                        <div class="mb-3">
                            <textarea id="code-editor" name="bins" class="form-control" rows="10" placeholder="Enter card BINs here, one per line..."></textarea>
                        </div>
                        <div id="status-bar" class="status-bar bg-light p-2 rounded border">
                            <span id="total-lines">Total lines: 0</span>
                            <span id="selected-length" class="float-end">Selected text length: 0</span>
                        </div>
                <!-- Blocked Item and Search Items in Columns -->
<div class="d-flex justify-content-between mt-3">
    <div class="form-section me-2">
        <h4>Blocked Item</h4>
        {% if prod_distinct_list %}
            {% for item in prod_distinct_list %}
                <div class="form-check">
                    <input class="form-check-input" type="radio" name="blocked_item" value="{{ item }}" id="blocked_{{ forloop.counter }}">
                    <label class="form-check-label" for="blocked_{{ forloop.counter }}">
                        {{ item }}
                    </label>
                </div>
            {% endfor %}
        {% else %}
            <p>No items available for selection.</p>
        {% endif %}
    </div>
</div>
          <!-- Single Process Button -->
                        <button class="btn btn-primary mt-3" type="submit">Process</button>
                    </form>
                </div>
            </div>
        </div>
    </div>

    <!-- Bootstrap Bundle with Popper from CDN -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
    <!-- CodeMirror JS from CDN -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.5/codemirror.min.js"></script>
    <!-- CodeMirror Modes (add more if needed) -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.5/mode/javascript/javascript.min.js"></script>
    <!-- CodeMirror KeyMap (optional) -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.5/keymap/sublime.min.js"></script>

    <!-- Include your custom JavaScript file -->
    <script src="{% static 'binblock/binblock.js' %}"></script>
</body>
</html>



def bin_blocking_editor(request):
    logger.info("Bin blocking editor view accessed")
    result = None
    log_with_delays = None
    prod_distinct_list = []
    categorized_list = []

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

        # Process Prod SQL statements
        prod_modified_sql, prod_remaining_sql = duplicate_and_modify_sql(
            prod_sql_statements, bins_with_neighbors, blocked_item
        )
        prod_merged_sorted_sql = merge_and_sort_sql(prod_modified_sql, prod_remaining_sql)

        # Save the new merged insert statements
        save_sql_statements_to_file(prod_merged_sorted_sql, os.path.join(OUTPUT_DIR, 'final_prod_insert_statements.sql'))

        # Log final merged SQL statements for Prod
        logger.info(f"Final merged Prod SQL statements: {prod_merged_sorted_sql}")

        context = {
            'result': processed_bins,
            'bins_with_neighbors': bins_with_neighbors,
            'prod_sql_statements': prod_merged_sorted_sql,
            'log_with_delays': log_with_delays,
            'prod_distinct_list': prod_distinct_list  # Correctly pass the prod_distinct_list
        }
        logger.info("Rendering binblocker.html with context data after processing")
        return render(request, 'binblock/binblocker.html', context)

    context = {
        'result': result,
        'log_with_delays': log_with_delays,
        'prod_distinct_list': prod_distinct_list  # Correctly pass the prod_distinct_list
    }
    logger.info("Rendering binblocker.html with initial context data")
    return render(request, 'binblock/binblocker.html', context)
