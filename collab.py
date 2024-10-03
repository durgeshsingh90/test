<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Splunk RRN</title>
    <!-- Bootstrap CSS CDN -->
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
    <style>
        /* Flexbox container and input styling */
        .flex-container {
            display: flex;
            flex-direction: row;
            align-items: flex-start;
        }

        .input-section, .output-section {
            flex: 1;
            margin-right: 20px;
        }

        .line-numbers {
            border: 1px solid #ced4da;
            background-color: #f8f9fa;
            padding: 8px;
            text-align: right;
            color: #6c757d;
            user-select: none;
            width: 30px;
            height: 100%;
            overflow: hidden;
            position: absolute;
            left: 0;
            top: 0;
        }

        .textarea-wrapper {
            position: relative;
            display: flex;
            height: 500px;
        }

        #inputNumbers, #outputNumbers {
            width: 100%;
            resize: none;
            height: 100%;
        }

        .btn-container {
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 10px;
            margin-top: 20px;
        }

        .form-section {
            margin-top: 10px;
        }

        .line-status {
            margin-top: 5px;
            font-size: 14px;
            color: #6c757d;
        }
    </style>
</head>
<body class="bg-light d-flex justify-content-center align-items-center vh-100">
    <a href="{% url 'first_page:home' %}" class="btn btn-primary position-fixed" style="top: 10px; left: 10px;">Home</a>
    
    <div class="container bg-white p-4 rounded shadow w-75">
        <div class="row">
            <div class="col-md-6">
                <div class="input-section">
                    <label for="inputNumbers" class="font-weight-bold">Enter RRN numbers:</label>
                    <div class="textarea-wrapper">
                        <div id="lineNumbers" class="line-numbers">1</div>
                        <textarea id="inputNumbers" class="form-control" rows="10" oninput="modifyNumbers(); updateLineNumbers();"></textarea>
                    </div>
                    <!-- Status for Total Number of Lines -->
                    <div id="lineStatus" class="line-status">Total Lines: 1</div>
                    <!-- Form section for Checkboxes -->
                    <div class="form-section">
                        <!-- Checkbox for Additional Options -->
                        <div class="form-check">
                            <input type="checkbox" id="addIndex" class="form-check-input" onchange="modifyNumbers()" checked>
                            <label for="addIndex" class="form-check-label">Add "index = 'application_omnipay'"</label>
                        </div>
                        <!-- Checkboxes for Host Options -->
                        <div class="form-check">
                            <input type="checkbox" id="addHost1" class="form-check-input" onchange="modifyNumbers()">
                            <label for="addHost1" class="form-check-label">Add "host = a4pvap068"</label>
                        </div>
                        <div class="form-check">
                            <input type="checkbox" id="addHost2" class="form-check-input" onchange="modifyNumbers()">
                            <label for="addHost2" class="form-check-label">Add "host = a5pvap039"</label>
                        </div>
                        <div class="form-check">
                            <input type="checkbox" id="addHost3" class="form-check-input" onchange="modifyNumbers()">
                            <label for="addHost3" class="form-check-label">Add "host = a5pvap040"</label>
                        </div>
                        <div class="form-check">
                            <input type="checkbox" id="addHost4" class="form-check-input" onchange="modifyNumbers()">
                            <label for="addHost4" class="form-check-label">Add "host = a4pvap1003"</label>
                        </div>
                        <div class="form-check">
                            <input type="checkbox" id="addHost5" class="form-check-input" onchange="modifyNumbers()">
                            <label for="addHost5" class="form-check-label">Add "host = a4pvap1004"</label>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-md-6">
                <div class="output-section">
                    <label for="outputNumbers" class="font-weight-bold">Splunk Search:</label>
                    <!-- Enlarged Output Textarea -->
                    <textarea id="outputNumbers" class="form-control" readonly></textarea>
                </div>
            </div>
        </div>

        <!-- Buttons Section -->
        <div class="btn-container">
            <button class="btn btn-secondary" onclick="removeEmptyLines()">Remove Empty Lines</button>
            <button id="copyButton" class="btn btn-primary" onclick="copyToClipboard()">Copy</button>
        </div>
    </div>

    <!-- Bootstrap JS, Popper.js, and jQuery -->
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.3/dist/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>

    <script>
        document.addEventListener('DOMContentLoaded', (event) => {
            // Load input from local storage
            const savedInput = localStorage.getItem('inputNumbers');
            if (savedInput) {
                document.getElementById('inputNumbers').value = savedInput;
                modifyNumbers();
                updateLineNumbers(); // Update line numbers on load
            }
        });

        function modifyNumbers() {
            // Your existing modifyNumbers function logic
        }

        function updateLineNumbers() {
            const input = document.getElementById('inputNumbers');
            const lineNumbers = document.getElementById('lineNumbers');
            const lines = input.value.split('\n').filter(line => line.trim() !== ''); // Exclude empty lines
            const totalLines = lines.length;

            // Generate line numbers
            lineNumbers.innerHTML = Array(totalLines).fill(0).map((_, i) => i + 1).join('<br>');

            // Update total line count status
            document.getElementById('lineStatus').textContent = `Total Lines: ${totalLines}`;
        }

        function removeEmptyLines() {
            const input = document.getElementById('inputNumbers');
            const nonEmptyLines = input.value.split('\n').filter(line => line.trim() !== ''); // Remove empty lines
            input.value = nonEmptyLines.join('\n');
            updateLineNumbers(); // Update line numbers after removing empty lines
            modifyNumbers(); // Update Splunk search after removing empty lines
        }

        function copyToClipboard() {
            const output = document.getElementById('outputNumbers');
            output.select();
            output.setSelectionRange(0, 99999); // For mobile devices

            document.execCommand('copy');

            const copyButton = document.getElementById('copyButton');
            copyButton.textContent = 'Copied!';
            setTimeout(() => {
                copyButton.textContent = 'Copy';
            }, 1000);
        }
    </script>
</body>
</html>