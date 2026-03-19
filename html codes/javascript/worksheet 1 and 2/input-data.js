// Radio Button Function 
function getSelectedAnswer() { 
    let answers = document.getElementsByName('question'); 
    for (let i = 0; i < answers.length; i++) { 
        if (answers[i].checked) { 
            alert("Selected answer: " + answers[i].value); 
            return; 
        } 
    } 
    alert("No answer selected"); 
} 