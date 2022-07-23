console.log("Javasript file connected");




// To Create New File Use This Function
const newFile = () => {
    var data = document.getElementById("textarea");
    if(data.value != "")
        var flag = confirm("Do you want to save file?");
    if(flag){
        saveFileData();
    }else{
        clearFileData();
    }
    console.log("new file method called");
}



// To Save New or Existing file use this function
const saveFileData = () =>{
    
    var file_name = prompt("enter file name:");
    $.ajax({
        type: "GET",
        url: "/save_users_content",   
        data: { 
                // csrfmiddlewaretoken: '{{ csrf_token }}',
                text: document.getElementById("textarea").value,
                file_name : file_name
            },  
        success:  function(response){
               console.log(response)
           },
        error: function(e){
            console.log(e)
        }
    });
    
    console.log("data Sucessfully send to server");
}


// Function used to Clear File
const clearFileData = () => {
    var data = document.getElementById("textarea");
    if(data.value != "")
    {
        var flag = confirm("do you want to remove all data?")
        if(!flag)
            return;
    }
    data.value = "";
    console.log("clear Data function called...");
}