/**
 * Renders the different building blocks for the game level, based on the data received from the back-end.
 * Components for each level are: 
 *  - Title         [mandatory]
 *  - Description   [mandatory]
 *  - Image         [optional]
 *  - Questions     [optional]
 *  - Buttons       [mandatory]
 * @param {*} data - Data structure with all the relevant game data
 */
function renderLevel(data) {          
    // Log the data received
    console.log("Render level:", data);  

    // Generate the page for the level base on the data
    const level = data.level
    setLevelTitle(level.name, level.summary);
    setLevelDescription(level.description);
    setLevelImage(level.image);
    setLevelQuestions(level.type, level.questions, level.idx, data.player_at_level_idx);            
    setLevelButtons(level.type, level.questions, level.idx, data.player_at_level_idx);            
}

/**
 * Sets the mandaory title to the page and puts the summary behind the info button.
 * @param {string} title 
 * @param {string} summary 
 */
function setLevelTitle(title,summary){
    // Set the title and info icon
    const titleContainer = document.getElementById('levelTitle');
    titleContainer.innerHTML = `
        <div class="title-bar">
            <span class="title-text">${title}</span>
            <span class="tooltip-icon" onclick="showSummaryModal()">ℹ️</span>
        </div>
    `;

    // Set the summary text for the pop-up message
    document.getElementById("summaryMessage").innerText = summary;
}

/**
 * Sets the level description text on the page
 * @param {string} description 
 */
function setLevelDescription(description){
    // Set the description of the level
    document.getElementById('levelDescription').innerText = description;
}

/**
 * Sets the (optional) level image on the page.
 * Note: Images need to be located in the folder '/static/decision_problems/'
 * @param {string} image 
 */
function setLevelImage(image){
    // Clear the image container
    const image_container = document.getElementById('levelImage');
    image_container.innerHTML =''
    
    // Set the (optional) image for the level 
    if( image ) {
        const img = document.createElement('img');
        img.src = "/static/decision_problems/" + image;
        image_container.append(img);
    }
}

/**
 * Places a list of questions and input fields on the page
 * @param {string} type 
 * @param {*} questions 
 * @param {int} level_idx 
 * @param {int} player_at_level_idx 
 */
function setLevelQuestions(type, questions, level_idx, player_at_level_idx){
    if (type === 'NONE'){
        create_none_questions();
    }
    else if (type === 'NUMERIC'){
        create_numeric_questions(questions, level_idx, player_at_level_idx);
    }
    else if (type === 'OPTIONS'){
        create_option_questions(questions, level_idx, player_at_level_idx);
    }
}

/**
 * If questions are not on the level, clear the question container
 */
function create_none_questions(){
    // Clear question container 
    const question_container = document.getElementById('levelQuestions');
    question_container.innerHTML = '';
}

/**
 * Generates the questions if they are numeric
 * @param {*} questions 
 * @param {int} level_idx 
 * @param {int} player_at_level_idx 
 */
function create_numeric_questions(questions, level_idx, player_at_level_idx){
    // Clear the question container
    const question_container = document.getElementById('levelQuestions');
    question_container.innerHTML = '';

    // Set the questions
    if (questions && questions.length > 0) {
        // Create a table
        const table = document.createElement('table');
        table.className = 'question-table'; // For styling
        
        questions.forEach((q, index) => {
            const row = document.createElement('tr');

            // Question cell (label)
            const labelCell = document.createElement('td');
            const label = document.createElement('label');
            labelCell.className = 'label-cell';
            label.textContent = q.question;
            label.setAttribute('for', `question-${index}`);
            labelCell.appendChild(label);

            // Input cell
            const inputCell = document.createElement('td');
            const input = document.createElement('input');
            inputCell.className = 'input-cell';
            input.id = `question-${index}`;
            input.name = `question-${index}`;
            
            // Make it only accept numeric values
            input.type = 'text';
            input.inputMode = 'decimal';
            input.pattern = '-?[0-9]*[.,]?[0-9]*';
            input.addEventListener('input', () => {
            input.value = input.value
                .replace(/[^0-9.-]/g, '')     // keep digits, one "-" and one "."
                .replace(/(?!^)-/g, '')       // only allow "-" at start
                .replace(/(\..*?)\..*/g, '$1'); // only one "."
            });
                    

            // 🔒 Disable the input if the user is not at this level and show the right answer
            if (level_idx < player_at_level_idx) {
                input.disabled = true;
                input.value = q.answer;
            }

           inputCell.appendChild(input);

            // Add both cells to the row
            row.appendChild(labelCell);
            row.appendChild(inputCell);

            // Add row to the table
            table.appendChild(row);
        });

        // Add table to the container
        question_container.appendChild(table);
    }
}

/**
 * Generates the questions if they are drop-downs
 * @param {*} questions 
 * @param {int} level_idx 
 * @param {int} player_at_level_idx 
 */
function create_option_questions(questions, level_idx, player_at_level_idx){
    // Clear the question container
    const question_container = document.getElementById('levelQuestions');
    question_container.innerHTML = '';
    
    // Set the questions
    if (questions && questions.length > 0) {
        // Create a table
        const table = document.createElement('table');
        table.className = 'question-table'; // For styling
        
        questions.forEach((q, index) => {
            const row = document.createElement('tr');

            // Question cell (label)
            const labelCell = document.createElement('td');
            const label = document.createElement('label');
            labelCell.className = 'label-cell';
            label.textContent = q.question;
            label.setAttribute('for', `question-${index}`);
            labelCell.appendChild(label);

            // Input cell
            const inputCell = document.createElement('td');
            const select = document.createElement('select');
            inputCell.className = 'input-cell';
            select.id = `question-${index}`;
            select.name = `question-${index}`;

            const options = q.options; // Assuming this is the array of options
            options.forEach(option => {
                const optionElement = document.createElement('option');
                optionElement.value = option;
                optionElement.textContent = option;
                select.appendChild(optionElement);
            });
           

            // 🔒 Disable the input if the user is not at this level
            if (level_idx < player_at_level_idx) {
                // Disable the selection
                select.disabled = true;
                // Set the answer
                select.value = q.answer;
            }

           inputCell.appendChild(select);

            // Add both cells to the row
            row.appendChild(labelCell);
            row.appendChild(inputCell);

            // Add row to the table
            table.appendChild(row);
        });

        // Add table to the container
        question_container.appendChild(table);
    }
}

/**
 * Generate all (optional) buttons:
 * 1. previous
 * 2. next
 * 3. check (submit answer)
 * @param {*} type 
 * @param {*} questions
 * @param {*} level_idx 
 * @param {*} player_level_idx 
 */
function setLevelButtons(type, questions, level_idx, player_level_idx){
    // Clear the button container
    const buttons_container = document.getElementById('levelButtons');
    buttons_container.innerHTML = ''

    // Create previous button
    if (level_idx > 0){
        const previousButton = document.createElement('button');
        previousButton.textContent = 'Previous';
        previousButton.style.marginRight = '8px';

        // Call fuction to go-to level + 1
        previousButton.onclick = () => gotoLevel(level_idx - 1);
        
        buttons_container.appendChild(previousButton);
    }

    // Create a button to submit the answer
    if( level_idx == player_level_idx){
        const checkButton = document.createElement('button');
        checkButton.textContent = '';
        if (type === 'NONE'){
            checkButton.textContent = 'Next';
        }
        else{
            checkButton.textContent = 'Check';
        }
        checkButton.style.marginRight = '8px';

        // Assign the submit level function to the button
        checkButton.onclick = () => submitLevel(level_idx, questions);
        
        buttons_container.appendChild(checkButton);
    }

    // Create next button
    if (level_idx < player_level_idx){
        const nextButton = document.createElement('button');
        nextButton.textContent = 'Next';
        nextButton.style.marginRight = '8px';
        
        // Call fuction to go-to level + 1
        nextButton.onclick = () => gotoLevel(level_idx + 1);

        buttons_container.appendChild(nextButton);
    }              
}

/**
 * Request level data. Called when pressing 'previous' or 'next'
 * @param {int} level_idx - Index of the level requested 
 */
function gotoLevel(level_idx){
    console.log("Go to Level:", level_idx);

    // Request the game data for the previous level
    socket.emit('get_level_data', { username: username, game_session_id: gameSessionId, level_idx: level_idx });
}

/**
 * Submit the aswers to the questions. To be checked by the back-end.
*/
function submitLevel(level_idx, questions) {

    const inputs = document.querySelectorAll('#levelQuestions input');
    
    let submission;
    if (questions){

        submission = questions.map((question, index) => {
            const input = document.getElementById(`question-${index}`);

            return {
                question: question,
                submission: input ? input.value : ''
            };
         });            
    }

    // Check for empty fields using a `for` loop so we can return early
    if( submission){
        for (let q of submission) {
            if (!q.submission) {
                alert("⛔ Make sure all questions are answered");
                return; // Exits the whole function
            }
        }
    }
        
    console.log("Submitting answer: ", submission);

    socket.emit('submit_level', {
        game_session_id: gameSessionId,
        level_idx:level_idx,
        username,
        submission
    });
}

