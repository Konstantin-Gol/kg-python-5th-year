// switch-content.js 

function showContent(contentId) { 

    // Hide all content elements 

    let contents = document.getElementsByClassName("content"); 

    for (let i = 0; i < contents.length; i++) { 

        contents[i].style.display = "none"; 

    } 

// Show the selected content element 

document.getElementById(contentId).style.display = "block"; 

} 
