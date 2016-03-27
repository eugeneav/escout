var path = require('path');
var webpack = require('webpack');

// @NOTE npm install -g webpack-dev-server may be required
// @NOTE webpack-dev-server --progress --colors for launch

module.exports = {
  entry: './js/app.js',
  output: { path: __dirname, filename: 'bundle.js' },
  module: {
    loaders: [
      {
        test: /.jsx?$/,
        loader: 'babel-loader',
        exclude: /node_modules/,
        query: {
          presets: ['es2015', 'react']
        }
      }
    ]
  },
};
