var updateBttns = document.getElementsByClassName("btn_update")

for( i = 0; i < updateBttns.length; i++){
    updateBttns[i].addEventListener('click', function(){
        var appoitmentId = this.dataset.appointment
        var action = this.dataset.action
        console.log('El id de la cita es :', appoitmentId, 'La accion es ', action)
        update_appointment_client(appoitmentId, action)
    })
}

function update_appointment_client(appoitmentId, action){
    var url = 'update_state/'
    fetch(url, {
        method: 'POST',
        headers: { 'Content-Type':'application/json',
                    'X-CSRFToken': csrftoken
                },
        body: JSON.stringify({'appoitmentId': appoitmentId, 'action': action}), 
    })
    .then((response) => {
        return response.json()
    })
    .then((data)=>{
        location.reload()
    })
}
