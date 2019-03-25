var app = new Vue({
  el: '#app',
  data: {
      show: 'acerca',
    },
    nuevoUsuario:"",
    nuevaContraseña:"",
    methods:{
      mensaje(){
      if (this.nuevoUsuario =""){
          alert("Por favor ingrese un usuario")
      }
      if (this.nuevaContraseña = ""){
        alert("Por favor ingrese una contraseña")
      }
    }
  }
      })