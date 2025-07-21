/**
 * Function to call when player clicks the button to join the game.
 */
function joinGame() {
    // Gather the inputs
    username = document.getElementById('username').value.trim();            
    gameSessionId = document.getElementById('gameSessionId').value.trim().toUpperCase();
    
    // Check the inputs
    if (!username) {
        alert("⛔ Please enter your name");
        return;
    }
    if (!gameSessionId) {
        alert("⛔ Please enter the Game ID");
        return;
    }
    
    // Store data in the cookie - To allow page refreshes
    setCookie('username', username, 1);
    setCookie('gameSessionId', gameSessionId, 1);

    // Inform the back-end
    socket.emit('join_game', { username: username, game_session_id: gameSessionId });
}


/**
 * Function to call when player clicks the button to leave the game.
 */
function leaveGame() {
    // Clear the cookies
    clearCookies()

    // Clear memory
    username = ""
    gameSessionId = ""  
    
    // Clear input fields of the join form for the next game
    document.getElementById('username').value = '';
    document.getElementById('gameSessionId').value = '';

    // Go back to displaying the join form
    display('joinForm')
}