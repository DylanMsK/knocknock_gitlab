import axios from 'axios'

const accountsUrl = '/accounts'

export default {
  signUp (newUser) {
    var params = {
      username: newUser.email,
      password: newUser.password
    }
    return axios.post(`${accountsUrl}/client/signup/`, params)
  }
}
