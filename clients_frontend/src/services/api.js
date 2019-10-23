import axios from 'axios'

const accountsUrl = '/accounts'

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
  }
}
