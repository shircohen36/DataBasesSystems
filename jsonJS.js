var xmlhttp = new XMLHttpRequest();
var url = "http://localhost/project_new/connectData.php";

xmlhttp.onreadystatechange=function() {
    if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
        myFunction(xmlhttp.responseText);
    }
}
xmlhttp.open("GET", url, true);
xmlhttp.send();

function myFunction(response) {
    var arr = JSON.parse(response);
    var i;
    var out = "<select id =txtHint onchange = showsubgene(this.value)>";
	out += "<option>"+" "+"</option>"; 
    for(i = 0; i < arr.length; i++) {
        out += "<option>"+arr[i].name+"</option>" ;
       
    }
    out += "</select>";
    document.getElementById("selectgenre").innerHTML = out;
}

function showsubgene(str) {
    if (str == "") {
        document.getElementById("txtHint").innerHTML = "";
        return;
    } else { 
        if (window.XMLHttpRequest) {
            // code for IE7+, Firefox, Chrome, Opera, Safari
            xmlhttp = new XMLHttpRequest();
        } else {
            // code for IE6, IE5
            xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
        }
        xmlhttp.onreadystatechange = function() {
            if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
                document.getElementById("txtHint").innerHTML = xmlhttp.responseText;
            }
        };
        xmlhttp.open("GET","https://localhost/project_new/subQuery.php?q="+str,true);
        xmlhttp.send();
		
		
    }
	
	xmlhttp.onreadystatechange=function() {
    if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
        myFunction(xmlhttp.responseText);
    }
}
xmlhttp.open("GET", url, true);
xmlhttp.send();

function myFunction(response) {
    var arr = JSON.parse(response);
    var i;
    var out = "<select onchange=showsubgene(this.value)>";
	out += "<option>"+" "+"</option>"; 
    for(i = 0; i < arr.length; i++) {
        out += "<option>"+arr[i].name+"</option>" ;
       
    }
    out += "</select>";
    document.getElementById("selectgenre").innerHTML = out;
}x
	
}