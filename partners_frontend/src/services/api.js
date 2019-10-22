import axios from 'axios'

const accountsUrl = '/accounts'

export default {
  userSignIn (user) {
    var params = {
      username: user.email,
      password: user.password
    }
    return axios.post(`${accountsUrl}/partner/login/`, params)
  },
  userSignUp (newUser) {
    var params = {
      name: newUser.partnerName,
      username: newUser.email,
      phone: newUser.phoneNumber,
      password: newUser.password
    }
    return axios.post(`${accountsUrl}/partner/signup/`, params)
  },
  userAuth (token) {
    return axios.get(`${accountsUrl}/partner/auth/`, {
      headers: {
        'Authorization': 'knock ' + token
      }
    })
  }
}
