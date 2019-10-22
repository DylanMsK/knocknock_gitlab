import axios from 'axios'

const accountsUrl = '/accounts'

export default {
  userSignUp (newUser) {
    var params = {
      name: newUser.partnerName,
      username: newUser.email,
      phone: newUser.phoneNumber,
      password: newUser.password
    }
    return axios.post(`${accountsUrl}/partner/signup/`, params)
  }
}
