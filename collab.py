{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bin Blocking Editor</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.5/codemirror.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.5/theme/monokai.min.css">
    <link rel="stylesheet" href="{% static 'binblock/styles.css' %}">
</head>
<body>
    <div class="container py-4">
        <div class="row">
            <div class="col-lg-8 mb-4">
                <div class="editor-container">
                    <h1 class="form-title">Bin Blocking Editor</h1>

                    <!-- Display success or failure message -->
                    {% if success is not None %}
                        {% if success %}
                            <div class="alert alert-success" role="alert">
                                Process completed successfully!
                            </div>
                        {% else %}
                            <div class="alert alert-danger" role="alert">
                                Process failed. Please try again.
                            </div>
                        {% endif %}
                    {% endif %}

                    <form method="POST" action="{% url 'binblock:binblocking_editor' %}">
                        {% csrf_token %}
                        <div class="mb-3">
                            <textarea id="code-editor" name="bins" class="form-control" rows="10" placeholder="Enter card BINs here, one per line..."></textarea>
                        </div>
                        <div id="status-bar" class="status-bar bg-light p-2 rounded border">
                            <span id="total-lines">Total lines: 0</span>
                            <span id="selected-length" class="float-end">Selected text length: 0</span>
                        </div>

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

                        <button class="btn btn-primary mt-3" type="submit">Process</button>
                    </form>
                </div>
            </div>
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.5/codemirror.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.5/mode/javascript/javascript.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.5/keymap/sublime.min.js"></script>
    <script src="{% static 'binblock/binblock.js' %}"></script>
</body>
</html>




def binblocking_editor(request):
    logger.info("Bin blocking editor view accessed")
    result = None
    prod_distinct_list = []
    success = None

    try:
        # Fetch distinct items from the database
        distinct_command = "sqlplus oasis77/ist0py@istu2"
        distinct_query = "SELECT DISTINCT description FROM oasis77.SHCEXTBINDB ORDER BY DESCRIPTION;"
        distinct_output_file = os.path.join(OUTPUT_DIR, 'prod_distinct_output.txt')
        run_sqlplus_command(distinct_command, distinct_query, distinct_output_file, "Distinct")
        prod_distinct_list = clean_distinct_file(distinct_output_file)
        logger.info(f"prod_distinct_list: {prod_distinct_list}")

        # Run background processing
        run_background_queries()

    except Exception as e:
        logger.error(f"Error running distinct query: {e}")

    if request.method == 'POST':
        # Process the submitted form data
        bin_input = request.POST.get('bins', '').splitlines()
        blocked_item = request.POST.get('blocked_item')

        try:
            # Log the blocked_item for debugging
            logger.info(f"Blocked Item selected: {blocked_item}")

            # Process BIN numbers
            processed_bins = process_bins(bin_input)
            logger.info(f"Processed BINs: {processed_bins}")

            # Calculate neighbors for processed bins
            bins_with_neighbors = calculate_bins_with_neighbors(processed_bins)
            logger.info(f"Bins with neighbors: {bins_with_neighbors}")

            # Retrieve and modify Prod SQL statements
            prod_sql_statements = generate_sql_insert_statements_for_prod()
            prod_modified_sql, prod_remaining_sql = duplicate_and_modify_sql(
                prod_sql_statements, bins_with_neighbors, blocked_item
            )
            prod_merged_sorted_sql = merge_and_sort_sql(prod_modified_sql, prod_remaining_sql)
            save_sql_statements_to_file(prod_merged_sorted_sql, os.path.join(OUTPUT_DIR, 'final_prod_insert_statements.sql'))
            logger.info(f"Final merged Prod SQL statements: {prod_merged_sorted_sql}")

            # Set success to True if no errors occurred
            success = True

        except Exception as e:
            logger.error(f"Error during processing: {e}")
            success = False

    context = {
        'result': result,
        'prod_distinct_list': prod_distinct_list,
        'success': success
    }
    return render(request, 'binblock/binblocker.html', context)
