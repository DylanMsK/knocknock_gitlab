import axios from 'axios'

const accountsUrl = 'http://13.125.93.228/accounts'
const storesUrl = 'http://13.125.93.228/stores'

export default {
  signUp (newUser) {
    var params = {
      username: newUser.email,
      password: newUser.password
    }
    return axios.post(`${accountsUrl}/client/signup/`, params)
  },
  signIn (user) {
    var params = {
      username: user.email,
      password: user.password
    }
    return axios.post(`${accountsUrl}/client/login/`, params)
  },
  signOut (token) {
    return axios.get(`${accountsUrl}/client/logout/`, {
      headers: {
        'Authorization': 'knock ' + token
      }
    })
  },
  userAuth (token) {
    return axios.get(`${accountsUrl}/client/auth/`, {
      headers: {
        'Authorization': 'knock ' + token
      }
    })
	},
	
	// Store
	searchStores(lon, lat, hour, d) {
		return axios.get(`${storesUrl}/?loc=${lon},${lat}&hour=${hour}&d=${d}`)
	}
}
