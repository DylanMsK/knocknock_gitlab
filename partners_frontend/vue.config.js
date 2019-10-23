module.exports = {
  'transpileDependencies': [
    'vuetify'
  ],
  publicPath: '/',
  devServer: {
    proxy: {
      '/accounts': {
        target: 'http://localhost:8000/'
      }
    }
  },
  lintOnSave: false
}
