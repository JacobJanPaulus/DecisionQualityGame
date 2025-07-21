function showWrongAnswerModal(message) {
    document.getElementById("wrongAnswerMessage").innerText = message;
    document.getElementById("wrongAnswerModal").style.display = "block";
}

function closeWrongAnswerModal() {
    document.getElementById("wrongAnswerModal").style.display = "none";
}