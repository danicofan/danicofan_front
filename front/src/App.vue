<template>
    <div>
        <div id="drawarea" class="container">
            <h1>登録済み作品</h1>
            <li v-for="item in items">
                <router-link v-bind:to="'/series/'+item.title">{{ item.title }}</router-link>
            </li>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'

    export default {
        components: {},
        data: () => {
            return {
                items: []
            }
        },
        methods: {
            drawAll() {
                axios.get(this.apiUrl + "/all").then((response) => {
                    response.data
                        .sort((x, y) => (- (x.firstAppeared - y.firstAppeared)))
                        .forEach((video) => {
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