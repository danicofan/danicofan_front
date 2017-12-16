<template>
    <div class="container">
        <h1>{{ tag }}</h1>
        <div v-if="items.length > 0">
            <a class="btn btn-primary" role="button"
               v-bind:href="'http://www.nicovideo.jp/watch/'+items[0].contentId+'?playlist_type=tag&tag='+tag+'+d%E3%82%A2%E3%83%8B%E3%83%A1%E3%82%B9%E3%83%88%E3%82%A2&sort=f&order=a&page=1&continuous=1'">
                連続再生
            </a>
        </div>
        <li v-for="item in items">
            {{ item.title }}
        </li>

    </div>
</template>

<script>
    import axios from 'axios'

    export default {
        components: {},
        data: () => {
            return {
                items: [],
                tag: ""
            }
        },
        methods: {
            drawAll() {
                var params = new URLSearchParams();
                this.tag = this.$route.params.title
                params.append('title', this.$route.params.title);
                axios.post(
                    this.apiUrl + "/series",
                    params
                ).then((response) => {
                    response.data.videos.forEach((video) => {
                        this.items.push(video)
                    })
                    console.log(this.items[0])
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