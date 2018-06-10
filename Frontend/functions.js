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
            document.getElementById("userCountryID").innerHTML = country;
            document.getElementById("userCity").innerHTML = city;
            document.getElementById("userEmail").innerHTML = email;
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

function isAlphaNumeric(str) {
  var code, i, len;

  for (i = 0, len = str.length; i < len; i++) {
    code = str.charCodeAt(i);
    if (!(code > 47 && code < 58) && // numeric (0-9)
        !(code > 64 && code < 91) && // upper alpha (A-Z)
        !(code > 96 && code < 123)) { // lower alpha (a-z)
      return false;
    }
  }
  return true;
}

function register() {

    if (document.getElementById("your_fsname").value.length <= 5) {
        window.alert("First name is too short(min. 5 characters).");
        return;
    }

    if (isAlphaNumeric(document.getElementById("your_fsname").value) === false)
    {
        window.alert("Enter only alpha numeric values.");
        return;
    }

    if (document.getElementById("your_lsname").value.length <= 5)
    {
        window.alert("Last name is too short(min. 5 characters).");
        return;
    }

    if (isAlphaNumeric(document.getElementById("your_lsname").value) === false)
    {
        window.alert("Enter only alphanumeric values.");
        return;
    }

    if (document.getElementById("your_username").value.length <= 4)
    {
        window.alert("Username too short(min. 4 characters).");
        return;
    }

    if (isAlphaNumeric(document.getElementById("your_username").value) === false)
    {
        window.alert("Enter only alphanumeric values.");
        return;
    }

    if (document.getElementById("your_pass").value.length <= 6)
    {
        window.alert("Password too short(min. 6 characters).");
        return;
    }

    if (isAlphaNumeric(document.getElementById("your_pass").value) === false)
    {
        window.alert("Enter only alphanumeric values.");
        return;
    }

    var n = document.getElementById("your_pass").value.localeCompare(document.getElementById("your_pass_conf").value);
    if (n !== 0)
    {
        window.alert("Password doesn't match.");
        return;
    }

    if (document.getElementById("your_city").value.length < 4)
    {
        window.alert("City name too short(min. 4 characters).");
        return;
    }

    if (isAlphaNumeric(document.getElementById("your_city").value) === false)
    {
        window.alert("Enter only alphanumeric values.");
        return;
    }

    if (document.getElementById("your_tel").value.length < 6)
    {
        window.alert("Telephone number too short(min. 6 characters).");
        return;
    }

    if (isAlphaNumeric(document.getElementById("your_tel").value) === false)
    {
        window.alert("Enter only alphanumeric values.");
        return;
    }

    if (document.getElementById("your_email").value.length < 4)
    {
        window.alert("Email too short(min. 5 characters).");
        return;
    }

    if (document.getElementById("your_picture").value.length < 5)
    {
        window.alert("Link too short(min. 5 characters).");
        return;
    }




    var xhttp = new XMLHttpRequest();

            xhttp.onreadystatechange = function () {
                if (this.readyState === 4 && this.status === 200){
                    //document.getElementById("getText").innerHTML = this.responseText
                    window.alert(this.responseText)
                    if (this.responseText === "INSERT SUCCES.")
                        gotoPage('index');
                }
            };

            var requestText = "REGISTER" +
                    "?" + document.getElementById("your_fsname").value +
                    "?" + document.getElementById("your_lsname").value +
                    "?" + document.getElementById("your_username").value +
                    "?" + document.getElementById("your_pass").value +
                    "?" + document.getElementById("your_country").value +
                    "?" + document.getElementById("your_city").value +
                    "?" + document.getElementById("your_tel").value +
                    "?" + document.getElementById("your_email").value +
                    "?" + document.getElementById("your_picture").value;

            xhttp.open("GET", requestText, true);
            xhttp.send();
}

function changeInfo() {
    window.alert("iei");
     if (isAlphaNumeric(document.getElementById("f_name").value) === false)
    {
        window.alert("Enter only alpha numeric values.");
        return;
    }
    if (isAlphaNumeric(document.getElementById("l_name").value) === false)
    {
        window.alert("Enter only alpha numeric values.");
        return;
    }
    if (isAlphaNumeric(document.getElementById("city").value) === false)
    {
        window.alert("Enter only alpha numeric values.");
        return;
    }
    if (document.getElementById("tel").value.length < 6)
    {
        window.alert("Telephone number too short(min. 6 characters).");
        return;
    }

    if (isAlphaNumeric(document.getElementById("tel").value) === false)
    {
        window.alert("Enter only alphanumeric values.");
        return;
    }
    if (document.getElementById("email").value.length < 4)
    {
        window.alert("Email too short(min. 5 characters).");
        return;
    }
    if (document.getElementById("link").value.length < 5)
    {
        window.alert("Link too short(min. 5 characters).");
        return;
    }



     var xhttp= new XMLHttpRequest();

    xhttp.onreadystatechange=function() {
        if (this.readyState === 4 && this.status === 200) {
            //document.getElementById("getText").innerHTML = this.responseText
            window.alert(this.responseText);
        }
    };

    var requestText= "CHANGE" +
        "?" + document.getElementById("f_name").value +
        "?" + document.getElementById("l_name").value +
        "?" + document.getElementById("city").value +
        "?" + document.getElementById("tel").value +
        "?" + document.getElementById("email").value +
        "?" + document.getElementById("link").value;

    xhttp.open("GET", requestText, true);
    xhttp.send();
}