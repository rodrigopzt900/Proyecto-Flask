Vue.component('product-delete', {
    props:['product','time'],
    data: function() {
        return {
            products: [],
        }
    },
    methods: {
        productDelete: function() {

            fetch('http://127.0.0.1:5000/api/products/'+this.product.id,{
                method: 'DELETE'
            })
                .then(res => res.json())
                .then(res => this.$emit("eventProductDelete"))


        }
    },
    watch:{
        //productId: function(newValue, oldValue){
            // console.log("Nuevo valor: " + newValue +" ,Viejo valor: "+ oldValue) Muestras el valor que tenia antes y el nuevo valor
        //    console.log(this.productId)
        //    $("#deleteModal").modal("show")

        time: function(newValue,oldValue){  //El watch solo funciona cuando hay un cambio , sacamos el tiempo y como el tiempo no se repite pues siempre 
                                            //Actualizara el watch
            console.log(this.time+" "+this.product.id)
            $("#deleteModal").modal("show")

        

        }
    },
    //    <button class='btn btn-success' v-on:click='findAll'>Click</button> Cuando clickes en este boton se ejecutara la funcion de abajo pero esta desactivado

    template: `
    
    <div  class="modal fade" id="deleteModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog" role="document">
            <div v-if="product" class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title" id="exampleModalLabel">Borrar: {{product.name }}</h5>
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
                <div class="modal-body">
                    ¿Seguro que desea borrar el registro seleccionado?
                </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-dismiss="modal">Cerrar</button>
                <button v-on:click="productDelete" class="btn btn-danger" data-dismiss="modal">Borrar</button>
                </div>
            </div>
        </div>
    </div>`
})