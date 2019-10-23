const state = {
	profiles: [
		{
			id: 1,
			email: 'hayley@ssafy.com',
			nickname: 'hayley',
			password: 'ssafy1234',
		},
		{
			id: 2,
			email: 'user1@ssafy.com',
			nickname: 'user1',
			password: 'ssafy1234',
		},
	],
	profile: {}
}

const getters = {
	getprofile (state) {
		return state.profile
	}
}

const actions = {
	getSingleProfile({ commit }, profileId) {
		const profile = state.profiles[profileId]
		commit('setSingleProfile', profile)
	}
}

const mutations = {
	setSingleProfile (state, profile) {
		state.profile = profile
	},
}


  export default {
	namespaced: true,
	state,
	getters,
	actions,
	mutations
  }
  