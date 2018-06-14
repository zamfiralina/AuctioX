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

            var profileFields = this.responseText.split("???");

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
    if(isUserLoggedIn()) {
        var requestText = "GETPROFILEINFO?" + getValueFromCookies("userHash");

        var xhttp = new XMLHttpRequest();

        xhttp.onreadystatechange = function () {
            if (this.readyState === 4 && this.status === 200) {

                var profileFields = this.responseText.split("???");

                var firstName = profileFields[0];
                var lastName = profileFields[1];
                var email = profileFields[2];
                var username = profileFields[3];
                var country = profileFields[4];
                var city = profileFields[5];
                var tel = profileFields[6];
                var picLink = profileFields[7];

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
        //window.alert("<" + requestText+ ">");
    }
    else {
        window.alert("You are not logged in.");
        gotoPage("index");
    }



}

function isUserLoggedIn() {
    //return getValueFromCookies("userHash").localeCompare("");

    // if user hash is empty
    if(!getValueFromCookies("userHash").localeCompare("")) {
        //window.alert("nohash");
        return false;
    }
    else {
        var requestText = "ISUSERLOGGEDIN?" + getValueFromCookies("userHash");
        var result = true;

        var xhttp = new XMLHttpRequest();

        xhttp.onreadystatechange = function () {
            if (this.readyState === 4 && this.status === 200) {
                //window.alert(this.responseText);
                result = (!this.responseText.localeCompare("USERLOGGEDINSUCCESS"));
            }
        };

        xhttp.open("GET", requestText, false);
        xhttp.send();


        //window.alert("result " + result);
        return result;
    }
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

    if (document.getElementById("your_fsname").value.length < 3) {
        window.alert("First name is too short(min. 3 characters).");
        return;
    }

    if (isAlphaNumeric(document.getElementById("your_fsname").value) === false)
    {
        window.alert("Enter only alpha numeric values.");
        return;
    }

    if (document.getElementById("your_lsname").value.length < 4)
    {
        window.alert("Last name is too short(min. 4 characters).");
        return;
    }

    if (isAlphaNumeric(document.getElementById("your_lsname").value) === false)
    {
        window.alert("Enter only alphanumeric values.");
        return;
    }

    if (document.getElementById("your_username").value.length < 4)
    {
        window.alert("Username too short(min. 4 characters).");
        return;
    }

    if (isAlphaNumeric(document.getElementById("your_username").value) === false)
    {
        window.alert("Enter only alphanumeric values.");
        return;
    }

    if (document.getElementById("your_pass").value.length < 5)
    {
        window.alert("Password too short(min. 5 characters).");
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
    if (document.getElementById("tel").value.length < 6 && document.getElementById("tel").value.length > 0)
    {
        window.alert("Telephone number too short(min. 6 characters).");
        return;
    }

    if (isAlphaNumeric(document.getElementById("tel").value) === false)
    {
        window.alert("Enter only alphanumeric values.");
        return;
    }
    if (document.getElementById("email").value.length < 4 && document.getElementById("email").value.length > 0 )
    {
        window.alert("Email too short(min. 5 characters).");
        return;
    }
    if (document.getElementById("link").value.length < 5 && document.getElementById("link").value.length > 0)
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
        "?" + document.getElementById("link").value +
        "?" + getValueFromCookies("userHash");

    xhttp.open("GET", requestText, true);
    xhttp.send();
}

function newAuction(){

    var xhttp = new XMLHttpRequest();

            xhttp.onreadystatechange = function () {
                if (this.readyState === 4 && this.status === 200){
                    //document.getElementById("getText").innerHTML = this.responseText
                    window.alert(this.responseText);
                    gotoPage("index");
                }
            };
    var requestText = "NEWAUCTION" + "???" + "PNAME::::" + document.getElementById("prod_name").value + "???"
                    + "CATEGORY::::" + document.getElementById("category").value + "???"
                    + "PICTURE::::" + document.getElementById("prod_pic").value + "???"
                    + "S_PRICE::::" + document.getElementById("start_price").value + "???"
                    + "S_DATE::::" + document.getElementById("start_date").value + "???"
                    + "END_DATE::::" + document.getElementById("end_date").value + "???"
                    + "DESCRIPTION::::" + document.getElementById("description").value + "???"
                    + "FABRICATION_COUNTRY::::" + document.getElementById("fab_country").value + "???"
                    + "FABRICATION_YEAR::::" + document.getElementById("fab_year").value + "???"
                    + "CONDITION::::" + document.getElementById("condition").value + "???"
                    + "MATERIAL::::" + document.getElementById("material").value + "???"
                    + "COLOR::::" + document.getElementById("color").value + "???"
                    + "OTHER_SPEC::::" + document.getElementById("spec_carac").value + "???"
                    + getValueFromCookies("userHash");


    xhttp.open("GET", requestText, true);
    xhttp.send();
}

function getSimpleSearchResultsPage(searchedText, page) {
    var requestText = "GETSIMPLESEARCHRESULTSPAGE?" + page + "?" + searchedText;

    var xhttp = new XMLHttpRequest();

    xhttp.onreadystatechange = function () {
        if (this.readyState === 4 && this.status === 200){

            result      = this.responseText;

            splitResult = result.split("!");


            hasPrevPage = splitResult[0];
            hasNextPage = splitResult[1];

            curPage = splitResult[2];
            maxPage = splitResult[3];

            items = splitResult[4];
            items = items.split("#").map(function (itemString) { return itemString.replace("%20", " ").split("???") });

            for (i = 0; i < items.length; i++) {
                currItem = items[i];
                itemView = "";
                itemView = itemView + "<a id = \"itemImage1\"><img src = \"" + currItem[4] + "\" height=\"150\" width=\"150\"></a> ";
                itemView = itemView + "<p><a id = \"itemName1\">" + currItem[2] + "</a></p> ";
                itemView = itemView + "<p><span>Last price: </span><a id = \"itemPrice1\">" + currItem[5] + "</a></p> ";
                itemView = itemView + "<p><span>End date: </span><a id = \"itemEndDate1\">" + currItem[7] + "</a></p> ";
                itemView = itemView + "<a href = \"#\" onclick=\"putValueInCookies('currItemId', '" + currItem[0] + "');gotoPage('ItemPage')\"> Read more... </a> ";
                document.getElementById("td" + (i+1)).innerHTML = itemView;
            }

            for (i = items.length; i < 9; i++)
                document.getElementById("td" + (i+1)).innerHTML = "";

            document.getElementById("searched_text").innerHTML = "<br>" + "You searched for: " + searchedText + "<br><br>";

            if (!hasPrevPage.localeCompare("1"))
                document.getElementById("button_prev").innerHTML =
                    "<button onclick='getSimpleSearchResultsPage(\"" + searchedText + "\", " + (page-1) + ")'>Previous</button>";
            else
                document.getElementById("button_prev").innerHTML = "";

            if (!hasNextPage.localeCompare("1"))
                document.getElementById("button_next").innerHTML =
                    "<button onclick='getSimpleSearchResultsPage(\"" + searchedText + "\", " + (page+1) + ")'>Next</button>";
            else
                document.getElementById("button_next").innerHTML = "";

            document.getElementById("page").innerHTML = "<h3>" + curPage + " / " + maxPage + "</h3>";
        }
    };
    xhttp.open("GET", requestText, true);
    xhttp.send();
}

function getAdvancedSearchResultsFromForm() {

    var category  = document.getElementById("search_category")           .value;
    var name      = document.getElementById("search_item_name")          .value;
    var originLoc = document.getElementById("search_fabrication_country").value;
    var originYr  = document.getElementById("search_fabrication_year")   .value;
    var condition = document.getElementById("search_condition")          .value;
    var material  = document.getElementById("search_material")           .value;
    var color     = document.getElementById("search_color")              .value;
    var other     = document.getElementById("search_other")              .value;

    var finalQuery = "GETADVANCEDSEARCHRESULTSPAGE!1!";

    if (category.length > 0)
        finalQuery += "CATEGORY~" + category;

    if (name.length > 0)
        finalQuery += "?" + "NAME~" + name;

    if (originLoc.length > 0)
        finalQuery += "?" + "FABRICATIONLOCATION~" + originLoc;

    if (originYr.length > 0)
        finalQuery += "?" + "FABRICATIONYEAR~" + originYr;

    if (condition.length > 0)
        finalQuery += "?" + "CONDITION~" + condition;

    if (material.length > 0)
        finalQuery += "?" + "MATERIAL~" + material;

    if (color.length > 0)
        finalQuery += "?" + "COLOR~" + color;

    if (other.length > 0)
        finalQuery += "?" + "OTHER~" + other;

    var xhttp = new XMLHttpRequest();

    xhttp.onreadystatechange = function () {
        if (this.readyState === 4 && this.status === 200) {
            putValueInCookies("advSrcStr", finalQuery);
            putValueInCookies("advSrcRes", this.responseText);
            gotoPage("index");
        }
    };

    xhttp.open("GET", finalQuery, true);
    xhttp.send();

}

function redirectedFromAdvancedSearch() {
    return (getValueFromCookies("advSrcStr").length > 0 && getValueFromCookies("advSrcRes").length > 0);
}

function mostRecent() {
    var requestText = "RECENT?";

    var xhttp = new XMLHttpRequest();

    xhttp.onreadystatechange = function () {
        if (this.readyState === 4 && this.status === 200) {

            var itemRows = this.responseText;

            //window.alert(this.responseText);

            var numberOfObjects = this.responseText.charAt(this.responseText.length)

            var itemImage1 = itemRows.split("#")[0].split("?")[0];
            var itemName1 = itemRows.split("#")[0].split("?")[1];
            var itemPrice1 = itemRows.split("#")[0].split("?")[2];
            var itemEndDate1 = itemRows.split("#")[0].split("?")[3];
            /*window.alert(itemRows.split("#")[0]);*/

            var itemImage2 = itemRows.split("#")[1].split("?")[0];
            var itemName2 = itemRows.split("#")[1].split("?")[1];
            var itemPrice2 = itemRows.split("#")[1].split("?")[2];
            var itemEndDate2 = itemRows.split("#")[1].split("?")[3];

            var itemImage3 = itemRows.split("#")[2].split("?")[0];
            var itemName3 = itemRows.split("#")[2].split("?")[1];
            var itemPrice3 = itemRows.split("#")[2].split("?")[2];
            var itemEndDate3 = itemRows.split("#")[2].split("?")[3];

            var itemImage4 = itemRows.split("#")[3].split("?")[0];
            var itemName4 = itemRows.split("#")[3].split("?")[1];
            var itemPrice4 = itemRows.split("#")[3].split("?")[2];
            var itemEndDate4 = itemRows.split("#")[3].split("?")[3];

            var itemImage5 = itemRows.split("#")[4].split("?")[0];
            var itemName5 = itemRows.split("#")[4].split("?")[1];
            var itemPrice5 = itemRows.split("#")[4].split("?")[2];
            var itemEndDate5 = itemRows.split("#")[4].split("?")[3];

            var itemImage6 = itemRows.split("#")[5].split("?")[0];
            var itemName6 = itemRows.split("#")[5].split("?")[1];
            var itemPrice6 = itemRows.split("#")[5].split("?")[2];
            var itemEndDate6 = itemRows.split("#")[5].split("?")[3];

            var itemImage7 = itemRows.split("#")[6].split("?")[0];
            var itemName7 = itemRows.split("#")[6].split("?")[1];
            var itemPrice7 = itemRows.split("#")[6].split("?")[2];
            var itemEndDate7 = itemRows.split("#")[6].split("?")[3];

            var itemImage8 = itemRows.split("#")[7].split("?")[0];
            var itemName8 = itemRows.split("#")[7].split("?")[1];
            var itemPrice8 = itemRows.split("#")[7].split("?")[2];
            var itemEndDate8 = itemRows.split("#")[7].split("?")[3];

            var itemImage9 = itemRows.split("#")[8].split("?")[0];
            var itemName9 = itemRows.split("#")[8].split("?")[1];
            var itemPrice9 = itemRows.split("#")[8].split("?")[2];
            var itemEndDate9 = itemRows.split("#")[8].split("?")[3];

            document.getElementById("itemImage1").innerHTML = "<img src = '" + itemImage1 + "'></img>";
            document.getElementById("itemName1").innerHTML = itemName1;
            document.getElementById("itemPrice1").innerHTML = itemPrice1;
            document.getElementById("itemEndDate1").innerHTML = itemEndDate1;

            document.getElementById("itemImage2").innerHTML = "<img src = '" + itemImage2 + "'></img>";
            document.getElementById("itemName2").innerHTML = itemName2;
            document.getElementById("itemPrice2").innerHTML = itemPrice2;
            document.getElementById("itemEndDate2").innerHTML = itemEndDate2;

            document.getElementById("itemImage3").innerHTML = "<img src = '" + itemImage3 + "'></img>";
            document.getElementById("itemName3").innerHTML = itemName3;
            document.getElementById("itemPrice3").innerHTML = itemPrice3;
            document.getElementById("itemEndDate3").innerHTML = itemEndDate3;

            document.getElementById("itemImage4").innerHTML = "<img src = '" + itemImage4 + "'></img>";
            document.getElementById("itemName4").innerHTML = itemName4;
            document.getElementById("itemPrice4").innerHTML = itemPrice4;
            document.getElementById("itemEndDate4").innerHTML = itemEndDate4;

            document.getElementById("itemImage5").innerHTML = "<img src = '" + itemImage5 + "'></img>";
            document.getElementById("itemName5").innerHTML = itemName5;
            document.getElementById("itemPrice5").innerHTML = itemPrice5;
            document.getElementById("itemEndDate5").innerHTML = itemEndDate5;

            document.getElementById("itemImage6").innerHTML = "<img src = '" + itemImage6 + "'></img>";
            document.getElementById("itemName6").innerHTML = itemName6;
            document.getElementById("itemPrice6").innerHTML = itemPrice6;
            document.getElementById("itemEndDate6").innerHTML = itemEndDate6;

            document.getElementById("itemImage7").innerHTML = "<img src = '" + itemImage7 + "'></img>";
            document.getElementById("itemName7").innerHTML = itemName7;
            document.getElementById("itemPrice7").innerHTML = itemPrice7;
            document.getElementById("itemEndDate7").innerHTML = itemEndDate7;

            document.getElementById("itemImage8").innerHTML = "<img src = '" + itemImage8 + "'></img>";
            document.getElementById("itemName8").innerHTML = itemName8;
            document.getElementById("itemPrice8").innerHTML = itemPrice8;
            document.getElementById("itemEndDate8").innerHTML = itemEndDate8;

            document.getElementById("itemImage9").innerHTML = "<img src = '" + itemImage9 + "'></img>";
            document.getElementById("itemName9").innerHTML = itemName9;
            document.getElementById("itemPrice9").innerHTML = itemPrice9;
            document.getElementById("itemEndDate9").innerHTML = itemEndDate9;
        }
    };


        xhttp.open("GET", requestText, true);
        xhttp.send();

}

function getLastAdvancedSearchResults() {

    var searchedContent = getValueFromCookies("advSrcStr");

    result      = getValueFromCookies("advSrcRes");

    splitResult = result.split("!");

    hasPrevPage = splitResult[0];
    hasNextPage = splitResult[1];

    curPage = splitResult[2];
    maxPage = splitResult[3];

    items = splitResult[4];
    items = items.split("#").map(function (itemString) { return itemString.replace("%20", " ").split("???") });

    for (i = 0; i < items.length; i++) {
        currItem = items[i];
        window.alert(currItem);
        itemView = "";
        itemView = itemView + "<a id = \"itemImage1\"><img src = \"" + currItem[4] + "\" height=\"150\" width=\"150\"></a> ";
        itemView = itemView + "<p><a id = \"itemName1\">" + currItem[2] + "</a></p> ";
        itemView = itemView + "<p><span>Last price: </span><a id = \"itemPrice1\">" + currItem[5] + "</a></p> ";
        itemView = itemView + "<p><span>End date: </span><a id = \"itemEndDate1\">" + currItem[7] + "</a></p> ";
        itemView = itemView + "<a href = \"#\" onclick=\"putValueInCookies('currItemId', '" + currItem[0] + "');gotoPage('ItemPage')\"> Read more... </a> ";
        document.getElementById("td" + (i+1)).innerHTML = itemView;
    }

    for (i = items.length; i < 9; i++)
        document.getElementById("td" + (i+1)).innerHTML = "";

    if (!hasPrevPage.localeCompare("1"))
        document.getElementById("button_prev").innerHTML =
            "<button onclick='getAdvancedSearchResultsPage(\"" + searchedContent + "\", " + (page-1) + ")'>Previous</button>";
    else
        document.getElementById("button_prev").innerHTML = "";

    if (!hasNextPage.localeCompare("1"))
        document.getElementById("button_next").innerHTML =
            "<button onclick='getAdvancedSearchResultsPage(\"" + searchedContent + "\", " + (page+1) + ")'>Next</button>";
    else
        document.getElementById("button_next").innerHTML = "";

    document.getElementById("page").innerHTML = "<h3>" + curPage + " / " + maxPage + "</h3>";

    // GETADVANCEDSEARCHRESULTSPAGE!1!CATEGORY~Animals?NAME~caine?COLOR~black
    // CATEGORY~Animals?NAME~caine?COLOR~black
    // CATEGORY~Animals  NAME~caine  COLOR~black

    searchedContentTable = "<table>";

    searchedContent.split("!")[2].split("?").forEach(
        function (tagString) {
            tagName = tagString.split("~")[0];
            tagVal  = tagString.split("~")[1];
            searchedContentTable += "<tr><td><br>" + tagName + ": </td><td><br>" + tagVal + "</td></tr>";
        }
    );

    searchedContentTable += "</table>";

    document.getElementById("searched_text").innerHTML = "<br>" + "You searched for:" + searchedContentTable + "<br><br>";

    putValueInCookies("advSrcStr", "");
    putValueInCookies("advSrcRes", "");
}


function getAdvancedSearchResultsPage(queryContent, page) {
    window.alert("Going to page " + page + " of " + queryContent);
}

function getCurrentItemDetails() {

    var lastItemId  = getValueFromCookies("currItemId");
    var requestText = "GETITEMDETAILS?" + lastItemId;

    var xhttp = new XMLHttpRequest();

    xhttp.onreadystatechange = function () {
        if (this.readyState === 4 && this.status === 200) {

            var itemDetails = this.responseText.split("???");

            var title    = itemDetails[2];
            var category = itemDetails[9];

            var imgLink  = itemDetails[4];

            var price    = itemDetails[5];
            var endDate  = itemDetails[7];

            var seller   = itemDetails[11];
            var tlf      = itemDetails[12];
            var email    = itemDetails[13];
            var location = itemDetails[14];

            var desc     = itemDetails[8];
            var tags     = itemDetails[10];

            document.getElementById("itempage_title").innerHTML       = title;
            document.getElementById("itempage_category").innerHTML    = category;

            document.getElementById("itempage_img").innerHTML         = "<img src='" + imgLink + "' width='350' height='350'>";

            document.getElementById("itempage_price").innerHTML       = price;
            document.getElementById("itempage_enddate").innerHTML     = endDate;

            document.getElementById("itempage_seller").innerHTML    = seller;
            document.getElementById("itempage_tlf").innerHTML         = tlf;
            document.getElementById("itempage_email").innerHTML       = email;
            document.getElementById("itempage_location").innerHTML    = location;

            document.getElementById("itempage_description").innerHTML = desc;

            var tagTable = "";

            tags.split("!").forEach(
                function (tagString) {
                    var tag = tagString.split("~")[0].replace("_", " ");
                    var val = tagString.split("~")[1];
                    tagTable += "<tr><td>" + tag + ":</td><td>" + val + "</td></tr>";
                }
            );

            document.getElementById("itempage_tags").innerHTML = tagTable;
        }
    };

    xhttp.open("GET", requestText, true);
    xhttp.send();
}
