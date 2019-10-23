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
  }
}
