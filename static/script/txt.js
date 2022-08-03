



function data()
    {
        var d=document.getElementById("lselect");
        var n1=document.getElementById("num").value;
        var n2=document.createElement("option");
        var n3=document.createTextNode(n1);
        n2.appendChild(n3);
        n2.setAttribute("value",n1);
        d.insertBefore(n2,d.lastChild);

    }

function select()
    {
        var d=document.getElementById("lselect");
        var dis=d.options[d.selectedIndex].text;
        document.getElementById("val").value=dis;
    }