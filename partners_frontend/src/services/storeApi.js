import axios from 'axios'

// const partnerUrl = '/partner/stores'
const partnerUrl = 'http://13.125.93.228/partner/stores'

export default {
  getAllStores (token) {
    return axios.get(`${partnerUrl}/`, {
      headers: {
        'Authorization': 'knock ' + token
      }
    })
  },
  getOneStore (storeId, token) {
    return axios.get(`${partnerUrl}/` + storeId + '/', {
      headers: {
        'Authorization': 'knock ' + token
      }
    })
  },
  enrollStore (info) {
    var params = {

    }
    return axios.get(`${partnerUrl}/`, params)
  }
}
