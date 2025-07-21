/**
 * Function to render the leaderboard in a table.
 * @param {*} leaderboard_data - The data structure with leaderboard data as received from the back-end
 */
function renderLeaderboard(leaderboard_data) {
    // Clear previous content
    const container = document.getElementById('leaderboard');
    container.innerHTML = '';

    // Create the header
    const header = document.createElement('h2')
    header.textContent = "🏆 Leaderboard"
    container.append(header)

    // Create the table
    const table = document.createElement('table')
    table.className = 'leaderboard-table'; // For styling via CSS

    // Create table header
    const thead = document.createElement('thead');
    const headerRow = document.createElement('tr');
    ['Player', 'Progress', 'Score'].forEach(headerText => {
        const th = document.createElement('th');
        th.textContent = headerText;
        headerRow.appendChild(th);
    });
    thead.appendChild(headerRow);
    table.appendChild(thead);

    // Create table body
    const tbody = document.createElement('tbody');
    
    // One row per player
    leaderboard_data.forEach(([name, progress, score], index) => {
        const row = document.createElement('tr');
        
        // Assign gold, silver, bronze medals to 1st, 2nd, 3rd place
        let medal = '';
        if (index === 0) medal = '🥇 ';
        else if (index === 1) medal = '🥈 ';
        else if (index === 2) medal = '🥉 ';

        // Column - Name
        const nameCell = document.createElement('td');
        nameCell.textContent = medal + name;
        row.appendChild(nameCell);

        // Column - Progress
        const progressCell = document.createElement('td');
        progressCell.textContent = progress;
        row.appendChild(progressCell);

        // Column - Score
        const scoreCell = document.createElement('td');
        scoreCell.textContent = score;
        row.appendChild(scoreCell);

        tbody.appendChild(row);
    });

    table.appendChild(tbody);
    container.appendChild(table);
};