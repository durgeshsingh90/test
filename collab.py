function modifyNumbers() {
    const input = document.getElementById('inputNumbers').value;
    localStorage.setItem('inputNumbers', input); // Save input to local storage

    const addIndex = document.getElementById('addIndex').checked;
    const addHost1 = document.getElementById('addHost1').checked;
    const addHost2 = document.getElementById('addHost2').checked;
    const addHost3 = document.getElementById('addHost3').checked;
    const addHost4 = document.getElementById('addHost4').checked;
    const addHost5 = document.getElementById('addHost5').checked;

    const lines = input.split('\n').filter(line => line.trim() !== ''); // Filter out empty lines
    let modifiedLines = [];
    let useAnd = false; // To keep track if "AND" should be used between lines

    for (let i = 0; i < lines.length; i++) {
        let line = lines[i].replace(/\s/g, ''); // Remove spaces from each line
        let modifiedLine = line;

        // Check if the line contains more than 30 digits
        if (line.length > 30) {
            let cleanedNumber = '';
            // Remove '3' before every digit (hexadecimal removal)
            for (let j = 0; j < line.length; j += 2) {
                if (line[j] === '3') {
                    cleanedNumber += line[j + 1];
                }
            }
            modifiedLines.push(cleanedNumber); // Just push the cleaned number
            continue; // Skip further processing for this line
        }

        // Check for 12-digit number
        let match12 = line.match(/"(\d{12})"/) || line.match(/(\d{12})/);
        if (match12) {
            let originalNumber = match12[1];
            let modifiedNumber = '';
            for (let j = 0; j < originalNumber.length; j++) {
                modifiedNumber += '3' + originalNumber[j];
            }
            if (line.includes(`"${originalNumber}"`)) {
                modifiedLine = line.replace(`"${originalNumber}"`, `"${originalNumber}" OR "${modifiedNumber}"`);
            } else {
                modifiedLine = line.replace(originalNumber, `"${originalNumber}" OR "${modifiedNumber}"`);
            }
        }

        // Check for 24-digit number
        let match24 = line.match(/"(\d{24})"/) || line.match(/(\d{24})/);
        if (match24) {
            let originalNumber = match24[1];
            let cleanedNumber = '';

            // Remove '3' before every digit (hexadecimal removal)
            for (let j = 0; j < originalNumber.length; j += 2) {
                if (originalNumber[j] === '3') {
                    cleanedNumber += originalNumber[j + 1];
                }
            }

            // Replace in the line if applicable
            if (line.includes(`"${originalNumber}"`)) {
                modifiedLine = line.replace(`"${originalNumber}"`, `"${cleanedNumber}"`);
            } else {
                modifiedLine = line.replace(originalNumber, `"${cleanedNumber}"`);
            }
        }

        // Check if the current line contains "AND" after a number
        if (line.trim().endsWith(" AND")) {
            useAnd = true; // Set flag to use "AND" for the next line
            modifiedLine = modifiedLine.replace(" AND", ""); // Remove the "AND" from the line
        }

        modifiedLines.push(modifiedLine);
    }

    // Construct the output with the correct separators
    let output = "";
    for (let i = 0; i < modifiedLines.length; i++) {
        output += modifiedLines[i];
        if (i < modifiedLines.length - 1) {
            output += useAnd ? ' AND ' : ' OR ';
            useAnd = false; // Reset the flag after using "AND"
        }
    }

    // Add index and host options if checkboxes are checked
    if (addIndex) {
        let hosts = '';
        if (addHost1) hosts += ' host = a4pvap068';
        if (addHost2) hosts += ' host = a5pvap039';
        if (addHost3) hosts += ' host = a5pvap040';
        if (addHost4) hosts += ' host = a4pvap1003';
        if (addHost5) hosts += ' host = a4pvap1004';
        output = `index = "application_omnipay" ${hosts} ${output} | reverse`;
    }

    document.getElementById('outputNumbers').value = output;
}