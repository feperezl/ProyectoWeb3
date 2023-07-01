function validarIngreso() {
    var usuario = document.getElementById("usuario").value;
    var contraseña = document.getElementById("contraseña").value;
  
    if (usuario === "" || usuario === null) {
      mostrarError("username", "Por favor, ingresa tu nombre de usuario.");
      return false;
    }

    if (usuario.length < 4 || usuario.length > 20) {
        mostrarError("usuario", "El nombre de usuario debe tener entre 4 y 20 caracteres.");
        return false;
      }
  
    if (contraseña === "" || contraseña === null) {
      mostrarError("password", "Por favor, ingresa tu contraseña.");
      return false;
      
    } else {
      window.location.href = "index.html";
    }
  
    
  
    return true;
  }
  
  function mostrarError(fieldId, errorMessage) {
    var errorContainer = document.getElementById(fieldId + "-error");
  
    if (errorContainer) {
      errorContainer.innerHTML = errorMessage;
    } else {
      var field = document.getElementById(fieldId);
      var errorElement = document.createElement("div");
      errorElement.id = fieldId + "-error";
      errorElement.className = "error-message";
      errorElement.innerHTML = errorMessage;
      field.parentNode.insertBefore(errorElement, field.nextSibling);
    }
  }

  function enviarCorreo() {
    var correo = document.getElementById("correo").value;
    // Aquí va la lógica para enviar el correo de recuperación
    if(correo.includes("@")){
        
        // Mostrar mensaje emergente
        alert("Se ha enviado un correo de recuperación a: " + correo);
        
        // Redirigir al inicio
        window.location.href = "index.html";
    } else {
        alert("El correo ingresado no es valido")
    }   
  }

( function burbuja(){
   function createElement(){
    const burbujas = document.querySelector(".burbujas");
    const element = document.createElement("span");
    const size = Math.random() * 60;

    element.style.width = 20 + size +  "px";
    element.style.height = 20 + size + "px";
    element.style.left = Math.random() * innerWidth + "px";
    burbujas.appendChild(element);
    console.log(size);

    setTimeout(() => {
      element.remove();
    }, 4000);
   }
   setInterval(createElement, 50);
})();  

  
  
  