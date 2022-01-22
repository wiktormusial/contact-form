const path = require('path')
const ESLintPlugin = require('eslint-webpack-plugin');

module.exports = {
  entry: './src/index.js',
  resolve: {
    extensions: ['*', '.js', '.jsx'],
  },
  output: {
    filename: 'index-bundle.js',
    path: path.resolve(__dirname, "static/js")
  },
  plugins: [
    new ESLintPlugin({
      extensions: ['js', 'jsx']
    })
  ],
  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        exclude: /node_modules/,
        loader: "babel-loader",
        options: { presets: ["@babel/preset-env", "@babel/preset-react"] }
      },
    ]
  }
}
