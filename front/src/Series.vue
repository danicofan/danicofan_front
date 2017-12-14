<template>
    <div>
        <div id="drawarea" class="container">
            <h1>Series</h1>
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
        data: () => {
            return {
                items: []
            }
        },
        methods: {
            drawAll() {
                var params = new URLSearchParams();
                params.append('title', this.$route.params.title);
                axios.post(
                    this.apiUrl + "/series",
                    params
                ).then((response) => {
                    response.data.videos.forEach((video) => {
                        this.items.push(video.title)
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