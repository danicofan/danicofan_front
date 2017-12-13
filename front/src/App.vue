<style scoped>
    #sliderbox {
        margin-left: 5%;
    }
</style>

<template>
    <div>
        <div id="drawarea" class="container">
            <h1>Hello</h1>
            <li v-for="item in items">
                {{ item }}
            </li>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'

    export default {
        components: {},
        data: {
            items: []
        },
        methods: {
            drawAll() {
                axios.get(this.apiUrl + "/all").then((response) => {
                    console.log(response)
                    response.data.forEach((video) => {
                        this.items.push(video)
                    })
                })
            }
        },
        mounted() {
            this.drawAll()
        },
        created() {
            this.apiUrl = "http://" + location.hostname + ":" + location.port + "/api"
        }
    }
</script>