window.onload = function() {
    element = document.getElementsByClassName("ltx_page_navbar")[0];
    var details = document.createElement('details');
    var summary = document.createElement('summary');
    summary.textContent = "Show Table of Contents";
    details.appendChild(summary);
    if (element != null)
        {
            details.appendChild(element.cloneNode(true));
            element.replaceWith(details);
        }
};
