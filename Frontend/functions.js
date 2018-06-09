function getValueFromCookies(key) {
    var cookie = document.cookie.split("; ").filter(function (c) { return !c.split("=")[0].localeCompare(key); } );
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
            if(!this.responseText.localeCompare("LOGINFAIL"))
                window.alert("Login failed, incorrect username or password.");
            else {
                putValueInCookies("userHash", this.responseText.split("?")[1]);
                gotoPage("profilePage");
            }
        }
    };

    xhttp.open("GET", requestText, true);
    xhttp.send();
}


function logout() {
    var requestText = "LOGOUT" + "?" + getValueFromCookies("userHash");

    var xhttp = new XMLHttpRequest();

    xhttp.onreadystatechange = function () {
        if (this.readyState === 4 && this.status === 200){
            if(!this.responseText.localeCompare("LOGOUTFAIL"))
                window.alert("Logout failed. User might already be logged out.");
            else {
                putValueInCookies("userHash", "");
                gotoPage("index");
            }
        }
    };

    xhttp.open("GET", requestText, true);
    xhttp.send();
}


function getLoggedInUserIndexInfo() {
     var requestText = "GETPROFILEINFO?" + getValueFromCookies("userHash");

    var xhttp = new XMLHttpRequest();

    xhttp.onreadystatechange = function () {
        if (this.readyState === 4 && this.status === 200){

            var profileFields = this.responseText.split("?");

            var firstName = profileFields[0];
            var lastName  = profileFields[1];
            var email     = profileFields[2];
            var username  = profileFields[3];
            var country   = profileFields[4];
            var city      = profileFields[5];
            var tel       = profileFields[6];
            var picLink   = profileFields[7];

            document.getElementById("loginArea").innerHTML =
                "<div align='right' onclick = \"gotoPage('profilePage')\">" +
                    username +
                    "<br><br><br>" +
                    "<button id='logoutButton' onclick='logout()'>Logout</button>"
                "</div>";
            document.getElementById("loginAreaHeader").innerHTML = "Logged in:";
        }
    };

    xhttp.open("GET", requestText, true);
    xhttp.send();
}

function getLoggedInUserProfileInfo() {
    var requestText = "GETPROFILEINFO?" + getValueFromCookies("userHash");

    var xhttp = new XMLHttpRequest();

    xhttp.onreadystatechange = function () {
        if (this.readyState === 4 && this.status === 200){

            var profileFields = this.responseText.split("?");

            var firstName = profileFields[0];
            var lastName  = profileFields[1];
            var email     = profileFields[2];
            var username  = profileFields[3];
            var country   = profileFields[4];
            var city      = profileFields[5];
            var tel       = profileFields[6];
            var picLink   = profileFields[7];

            document.getElementById("userFirstName").innerHTML = firstName;
            document.getElementById("userLastName").innerHTML = lastName;
            document.getElementById("userCountryID").innerHTML = email;
            document.getElementById("userCity").innerHTML = country;
            document.getElementById("userEmail").innerHTML = city;
            document.getElementById("userTel").innerHTML = tel;
            document.getElementById("userImage").innerHTML = "<img src = '" + picLink + "'></img>";
        }
    };

    xhttp.open("GET", requestText, true);
    xhttp.send();
}

function isUserLoggedIn() {
    return getValueFromCookies("userHash").localeCompare("");
}