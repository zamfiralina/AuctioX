function gotoPage(page) {
    //document.getElementById("elementID").onclick.apply(location.href, location.href = page.toString().concat(".html"));

    //window.alert("S-a apelat macar :)");

    //document.getElementById("testID").onclick.apply(location.href, location.href = page.toString().concat(".html"));

    window.location.href = page.toString().concat(".html");
}

function getInput(elementID) {
    var input = document.getElementById(elementID).value;

    var response = window.confirm("Press ok to continue");

    if (response === false)
        window.alert(input);
    else
        window.alert(input);

    console.log(input);
}

function testSearch() {
            var xhttp = new XMLHttpRequest();

            xhttp.onreadystatechange = function () {
                if (this.readyState === 4 && this.status === 200){
                    //document.getElementById("getText").innerHTML = this.responseText
                    window.alert(this.responseText)
                }
            };

            var requestText = "SEARCH" +
                    "?" + document.getElementById("index_search").value;

            xhttp.open("GET", requestText, true);
            xhttp.send();
}

function login() {
    var requestText = "LOGIN" + "?" + document.getElementById("username_id").value + "?"
                    + document.getElementById("password_id").value;

    var xhttp = new XMLHttpRequest();

            xhttp.onreadystatechange = function () {
                if (this.readyState === 4 && this.status === 200){
                    //document.getElementById("getText").innerHTML = this.responseText
                    window.alert(this.responseText)
                }
            };

    xhttp.open("GET", requestText, true);
    xhttp.send();
}