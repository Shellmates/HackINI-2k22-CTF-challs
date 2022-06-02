function myFunc(eventObj) {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
      if (this.readyState == 4 && this.status == 200) {
        document.getElementById("content").innerHTML = xhttp.responseText;
      }
    };
    xhttp.open("POST", '/request');
    xhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhttp.send("service=" + this.attributes.link.value);

  }

  var dep = document.getElementsByClassName('department');
  for (var i = 0; i < dep.length; i++) {
    dep[i].addEventListener('click', myFunc);
  }