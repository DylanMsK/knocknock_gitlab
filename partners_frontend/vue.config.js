module.exports = {
  'transpileDependencies': [
    'vuetify'
  ],
  publicPath: '/',
  devServer: {
    proxy: {
      '/accounts': {
        // target: 'http://localhost:8000/'
        target: 'http://13.125.93.228/'
      }
    }
  },
  lintOnSave: false
}
