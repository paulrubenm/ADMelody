// JavaScript Document
// Get the modal
var modalImg = document.getElementById("img01");
var captionText = document.getElementById("caption");
var modal = document.getElementById("myModal");
var span = document.getElementsByClassName("close")[0];

// When the user clicks on <span> (x), close the modal
span.onclick = function () {
    modal.style.display = "none";
}

function BindClickEventForImage(obj)
{

    // Get the image and insert it inside the modal - use its "alt" text as a caption
    
    modal.style.display = "block";
    modalImg.src = obj.src;
    captionText.innerHTML = obj.alt;

    // Get the <span> element that closes the modal
}
