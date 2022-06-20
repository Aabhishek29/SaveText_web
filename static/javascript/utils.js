console.log("Javasript file connected");

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


const saveFileData = () =>{
    var file_name = prompt("enter file name:");
    $.ajax({
        type: "POST",
        url: "{{ url 'save_users_content' }}",   
        data: { 
                csrfmiddlewaretoken: '{{ csrf_token }}',
                text: "this is my test view",
                fileName : file_name
            },  
        success:  function(response){
               console.log(response)
           },
        error: function(e){
            console.log(e)
        }
    });
    console.log("file saved");
}

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