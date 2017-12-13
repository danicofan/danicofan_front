module.exports = {
    entry: __dirname + "/src/index.js",
    output: {
        path: __dirname + '/static',
        filename: 'bundle.js'
    },


    resolve: {
        alias: {
            'vue$': 'vue/dist/vue.esm.js' // 'vue/dist/vue.common.js' for webpack 1
        }
    },

    module: {
        loaders: [
            {
                test: /\.vue$/, loader: 'vue-loader'
            }
        ]
    },
    devtool: 'source-map',
};