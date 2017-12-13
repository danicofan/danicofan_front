<style scoped>
    #sliderbox {
        margin-left: 5%;
    }
</style>

<template>
    <div>
        <div id="drawarea" class="container">
            <h1>Hello</h1>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    import LocalCanvas from './LocalCanvas.vue'

    export default{
        components: {
        },
        data: {
        },
        methods: {
        },
        mounted(){
        },
        created(){
            this.apiUrl = "http://" + location.hostname + ":" + location.port + "/api"
        }
    }
</script>