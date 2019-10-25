import axios from 'axios'

const storesUrl = '/stores'

export default {
  getAllStores (user) {
    var params = {

    }
    return axios.get(`${storesUrl}/`, params)
  },
  getOneStore (storeId) {
    var params = {

    }
    return axios.get(`${storesUrl}/`, params)
  },
  enrollStore (info) {
    var params = {

    }
    return axios.get(`${storesUrl}/`, params)
  }
}