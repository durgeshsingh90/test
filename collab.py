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
    margin-left: -1px; /* To remove the gap between line numbers and textarea */
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
            <div id="statusBar1" class="status-bar">Total Lines: 0 | Selected: 0 characters</div>
          <button onclick="copyText('processedBins', this)" class="btn btn-primary copy-btn">Copy</button>
        </div>        
      </div>
    </div>
    <div class="col-md-6">
      <div class="card bg-dark text-white">
        <div class="card-body">
          <h5 class="card-title">2. Production Table Export</h5>
          <div class="textarea-container">
            <div id="lineNumbers2" class="line-numbers"></div>
            <textarea id="productionExport" class="form-control textarea" rows="12" placeholder="Enter details..." oninput="updateLineNumbers(this, 'lineNumbers2')">{{ production_data }}</textarea>
            <div id="statusBar2" class="status-bar">Total Lines: 0 | Selected: 0 characters</div>
          <button onclick="copyText('productionExport', this)" class="btn btn-primary copy-btn">Copy</button>
        </div>
      </div>
    </div>
    <div class="col-md-6">
      <div class="card bg-dark text-white">
        <div class="card-body">
          <h5 class="card-title">3. UAT Table Export</h5>
          <div class="textarea-container">
            <div id="lineNumbers3" class="line-numbers"></div>
            <textarea id="uatExport" class="form-control textarea" rows="12" placeholder="Enter details..." oninput="updateLineNumbers(this, 'lineNumbers3')">{{ uat_data }}</textarea>
            <div id="statusBar3" class="status-bar">Total Lines: 0 | Selected: 0 characters</div>
          <button onclick="copyText('uatExport', this)" class="btn btn-primary copy-btn">Copy</button>
        </div>
      </div>
    </div>
    <div class="col-md-6">
      <div class="card bg-dark text-white">
        <div class="card-body">
          <h5 class="card-title">4. Processed Insert Statement</h5>
          <div class="textarea-container">
            <div id="lineNumbers4" class="line-numbers"></div>
            <textarea id="insertStatement" class="form-control textarea" rows="12" placeholder="Enter details..." oninput="updateLineNumbers(this, 'lineNumbers4')">{{ insert_statement }}</textarea>
          </div>
          <div id="statusBar4" class="status-bar">Total Lines: 0 | Selected: 0 characters</div>
          <button onclick="copyText('insertStatement', this)" class="btn btn-primary copy-btn">Copy</button>
        </div>
      </div>
    </div>
    
      
  </div>
</div>

<script>
  function updateLineNumbers(textarea, lineNumberId) {
    const lines = textarea.value.split('\n').length;
    const lineNumberElement = document.getElementById(lineNumberId);
    lineNumberElement.innerHTML = '';
    for (let i = 1; i <= lines; i++) {
      lineNumberElement.innerHTML += i + '<br>';
    }
  
    // Update status bar
    updateStatusBar(textarea, lineNumberId.replace('lineNumbers', 'statusBar'));
  }
  
  function updateStatusBar(textarea, statusBarId) {
    const selectedTextLength = textarea.selectionEnd - textarea.selectionStart;
    const lines = textarea.value.split('\n').length;
    const statusBarElement = document.getElementById(statusBarId);
    statusBarElement.innerHTML = `Total Lines: ${lines} | Selected: ${selectedTextLength} characters`;
  }
  
  // Initialize line numbers and status bar when the page loads
  window.onload = function() {
    document.querySelectorAll('.textarea').forEach((textarea, index) => {
      const lineNumberId = 'lineNumbers' + (index + 1);
      const statusBarId = 'statusBar' + (index + 1);
      
      updateLineNumbers(textarea, lineNumberId);
  
      // Add event listener for input change and selection change
      textarea.addEventListener('input', function() {
        updateLineNumbers(textarea, lineNumberId);
      });
  
      textarea.addEventListener('select', function() {
        updateStatusBar(textarea, statusBarId);
      });
  
      textarea.addEventListener('mouseup', function() {
        updateStatusBar(textarea, statusBarId);
      });
  
      textarea.addEventListener('keyup', function() {
        updateStatusBar(textarea, statusBarId);
      });
    });
  };
  
  function copyText(elementId, buttonElement) {
    const copyText = document.getElementById(elementId);
    copyText.select();
    document.execCommand("copy");
    
    // Change button text and color
    buttonElement.textContent = "Copied!";
    buttonElement.classList.add("copied-btn");
  
    // Reset button text and color after 3 seconds
    setTimeout(function() {
      buttonElement.textContent = "Copy";
      buttonElement.classList.remove("copied-btn");
    }, 1000);
  }
  
</script>

<!-- Bootstrap Bundle with Popper -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
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
            'processed_bins': processed_bins,  # Or 'combined_bins' if you need the combined version
            'production_data': production_data,
            'uat_data': uat_data,
            'insert_statement': insert_statement,
            'prod_distinct_list': prod_distinct_list,
        }

        return render(request, 'binblock/binblocker.html', context)
