var path = require('path');
var webpack = require('webpack');

// @NOTE npm install -g webpack-dev-server may be required
// @NOTE webpack-dev-server --progress --colors for launch

/**
   TODO

    !!! Use ES6 only

    1. See Webpack + React config. Find Production config
    2. Simplify development process launching
    3. Finish authentication logic (Logout feature doesn't work)
    4. Implement Applications business logic and UI (See nested routing https://github.com/reactjs/react-router/tree/master/examples)
    4.1 Create Create application screen 
    5. Implement Events business logic and UI 
    6. Write some tests
    7. Make some refactoring
    8. Deploy on company server for general purpose usage

 */

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
                // target: 'http://escout.dev/',
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
