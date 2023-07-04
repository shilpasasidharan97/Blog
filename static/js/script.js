function login(){
    var username = document.getElementById('loginUsername').value
    var password = document.getElementById('loginPassword').value
    var csrf = document.getElementById('csrf').value

    if(username == '' && password == ''){
        alert('You must enter both')
    }

    var data = {
        'username' : username,
        'password' : password
    }

    fetch('/api/login/' , {
        method : 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken' : csrf,
        },
       
        body : JSON.stringify(data)
    }).then(result => result.json())
    .then(response => {
        
        if(response.status == 200){
            window.location.href = '/home/'
        }
        else{
            alert(response.message)
        }

    })

}


function register(){
    var first_name = document.getElementById('firstname').value
    var last_name = document.getElementById('lastname').value
    var email = document.getElementById('email').value
    var phone = document.getElementById('phone').value
    var username = document.getElementById('loginUsername').value
    var password = document.getElementById('loginPassword').value
    var csrf = document.getElementById('csrf').value
    alert(first_name)
    if(username == '' && password == ''){
        alert('You must enter both')
    }

    var data = {
        'username' : username,
        'password' : password,
        'first_name' : first_name,
        'last_name' : last_name,
        'email' : email,
        'phone' : phone,
    }
alert(data)
    fetch('/api/register/' , {
        method : 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken' : csrf,
        },
       
        body : JSON.stringify(data)
    }).then(result => result.json())
    .then(response => {
        console.log(response)
        if(response.status == 200){
            alert('ss')
            // window.location.href = '/home/login/'
        }
        else{
            alert(response.message)
        }

    })

}