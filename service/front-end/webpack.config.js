var path = require('path');
var webpack = require('webpack');

// @NOTE npm install -g webpack-dev-server may be required
// @NOTE webpack-dev-server --progress --colors for launch

module.exports = {
    entry: './js/app.js',
    output: {path: __dirname, filename: 'bundle.js'},
    module: {
        loaders: [
            {
                test: /.jsx?$/,
                loader: 'babel-loader',
                exclude: /node_modules/,
                query: {
                    presets: ['es2015', 'react',]
                }
            }
        ]
    },
    devServer: {
        proxy: {
            '/api/*': {
                //target: 'http://escout.dev/',
                target: 'http://localhost:8081/',
                secured: false,
                changeOrigin: true,
                rewrite: function (req) {
                    req.url = req.url.replace(/^\/api/, '');
                }

            }

        }
    }
};
