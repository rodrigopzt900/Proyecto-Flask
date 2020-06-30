Vue.component('product-save', {
    props:[,'time'],
    data: function() {
        return {
            products: [],
            fcategory_id:0,
            fname:"",
            fprice:0,
            product:0
        }
    },
    methods: {
        productSave: function() {
            var formData = new FormData()
            formData.append("name",this.fname)
            formData.append("price",this.fprice)
            formData.append("category_id",this.fcategory_id)
            this.productInsert(formData)            
        },
        productInsert(formData){
            fetch(' http://127.0.0.1:5000/api/products/',{
                method: 'POST',
                body: formData
            })
                .then(res => res.json())
                .then(res => this.$emit("eventProductDelete"))

        }
    },
    watch:{
        time: function(newValue,oldValue){

            $("#saveModal").modal("show")

        

        }
    },
    //    <button class='btn btn-success' v-on:click='findAll'>Click</button> Cuando clickes en este boton se ejecutara la funcion de abajo pero esta desactivado

    template: `
    
    <div  class="modal fade" id="saveModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog" role="document">
            <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title" id="exampleModalLabel">Crear Producto: </h5>
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
                <div class="modal-body">
        
                <div class="form-group">
                    <label for="name">Nombre</label> 
                    <input class="form-control" v-model="fname" type="text" value="">
                </div>

                <div class="form-group">
                    <label for="price">Precio</label> 
                    <input class="form-control" v-model="fprice" type="text" value="">
                </div>

                <div class="form-group">
                    <label for="category_id">Categoría</label> 
                    <select class="form-control" v-model="fcategory_id"><option value="1">Categoria 1</option><option value="2">Categoria 2</option><option value="3">Categoria 3</option><option value="4">Categoria 4</option><option value="5">Categoria 5</option><option value="6">Categoria 6</option><option value="7">Categoria 7</option><option value="8">Categoria 9</option><option value="9">Categoria 8</option></select>
                </div>

                </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-dismiss="modal">Cerrar</button>
                <button v-on:click="productSave" class="btn btn-success">Enviar</button>
                </div>
            </div>
        </div>
    </div>`
})