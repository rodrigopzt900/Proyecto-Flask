Vue.component('product-list', {
    data: function() {
        return {
            products: [],
            productSelected:0,  
            productIndexSelected:0,
            timeDelete:0,
            timeSave:0
            
        }
    },
    mounted(){
        this.findAll(); //Este metodo hce que desde el principio corra una template designado
    },
    methods: {
        findAll: function() {
            console.log("Hola mundo")

            fetch('http://127.0.0.1:5000/api/products/')
                .then(res => res.json())
                .then(res => this.products = res)


        },
        productDelete: function(product,index) {
            this.timeDelete = new Date().getTime()
            this.productSelected = product
            this.productIndexSelected = index
        },
        ProductSave: function() {
            this.timeSave = new Date().getTime()
        },
        eventProductDelete: function(   ){
            console.log("Eliminado")
            this.$delete(this.products.data,this.productIndexSelected)
        },
        eventProductInsert: function(product){
            console.log(product.data.name)
        }
    },
    
    //    <button class='btn btn-success' v-on:click='findAll'>Click</button> Cuando clickes en este boton se ejecutara la funcion de abajo pero esta desactivado

    template: `
        <div>
            <button class="btn btn-success" v-on:click="ProductSave">Crear</button>
            <div v-if='products.length == 0'>
                <h1>No hay productos</h1>
                

                </div>
                <div v-else><h1>Productos</h1></div>
                <div v-for='(product, index) in products.data' class="jumbotron pb-2 pt-3">
                    <h3>            
                        <a href="#">
                            {{ product.name }}
                            
                        </a>
                    </h3>
                    
                    <h5>{{ product.category }} </h5>

                    <a data-toggle="tooltip" data-placement="top" title="Editar" class="btn btn-success btn-sm" href="#"><i class="fa fa-edit"></i></a>

                <button  v-on:click="productDelete(product,index)" class="btn btn-danger btn-sm"><i  data-toggle="tooltip"  :title="'Eliminar producto '+ product.name " data-placement="top"class="fa fa-trash"></i></button>
            </div>
            
            <product-delete v-on:eventProductDelete="eventProductDelete" :time="timeDelete" :product="productSelected"></product-delete>
            <product-save :v-on:eventProductInsert="eventProductInsert" :time="timeSave"></product-save>

        </div>
        `
})