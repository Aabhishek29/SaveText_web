function call(){
    var name = document.getElementById("username");
    var pass = document.getElementById("password");
    let pattern = /[0-9]/g;
    if(!pattern.test(name)){
        return false;
    }
    if(pass==="")
        return false;
    return true;
}