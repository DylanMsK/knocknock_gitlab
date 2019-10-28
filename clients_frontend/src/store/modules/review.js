const state = {
	reviews: [
		{
			id: 1,
			store: 1,
			score: 5,
			content: '맛있어욤',
		},
		{
			id: 2,
			store: 2,
			score: 4,
			content: '맛있어욤'
		},
		{
			id: 3,
			store: 3,
			score: 1,
			content: '맛없어요'
		},
		{
			id: 4,
			store: 3,
			score: 2,
			content: '맛없어요'
		},
	],
	review: {},
	storesIdInReviews: []
}

const getters = {
	getAllReviews (state) {
		return state.reviews
	},
	getReview (state) {
		return state.review
	},
	getStoresIdInReviews (state) {
		for (var idx in state.reviews) {
			state.storesIdInReviews.push(state.reviews[idx].store)
		}
		return state.storesIdInReviews
	}
}

const actions = {
	getSingleReview({ commit }, reviewId) {
		const review = state.reviews[reviewId-1]
		commit('setSingleReview', review)
	}
}

const mutations = {
	setSingleReview (state, review) {
		state.review = review
	},
}


  export default {
	namespaced: true,
	state,
	getters,
	actions,
	mutations
  }
  