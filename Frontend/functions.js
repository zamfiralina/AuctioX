function getValueFromCookies(key) {
    var cookie = document.cookie.split("; ").filter(function (c) { return !c.split("=")[0].localeCompare("ceva"); } );
    if (cookie.length == 0)
        return "";
    else
        return cookie[0].split("=")[1];
}

function putValueInCookies(key, value) {
    document.cookie = key + "=" + value;
}

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
                    putValueInCookies("userHash=", this.responseText.split("?")[1]);

                    window.alert(getValueFromCookies("userHash"));
                }
            };

    xhttp.open("GET", requestText, true);
    xhttp.send();
}

function gotoMyProfile() {



}