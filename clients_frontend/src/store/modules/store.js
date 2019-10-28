import api from "../../services/api"

const state = {
	stores: [],
	store: '',
	// store name in Management Review
	storesNameInReviews: [],
	// store location in Map component
	storesLoc: [],
}

const getters = {
	storesLoc (state) {
		console.log(state.stores)
		for (var idx in state.stores) {
			var store = state.stores[idx]
			var storeObj = {
				'name': store.name,
				'latlon': {'lat': store.lat, 'lon': store.lon}
			}
			state.storesLoc.push(storeObj)
		}
		return state.storesLoc
	}
}

 const actions = {
	async getStores ({ commit}, params) {
		const obj = params
		// params = {
		// 	'lat': 0,
		// 	'lon': 0,
		// 	'hour': 0,
		// 	'd': 500, 
		// }
		const resp = await api.searchStores(obj.lon, obj.lat, obj.hour, obj.d)
		const stores = resp.data.map(store => ({
			'id': store.id,
			'originId': store.origin_id,
			'name': store.name,
			'location': store.location,
			'roadAddr': store.road_addr,
			'commonAddr': store.common_addr,
			'addr': store.addr,
			'thumbnail': store.thumbnail,
			'category': store.category,
			'contact': store.contact,
			'description': store.description,
			'options': store.options,
			'partner': store.partner,
			'priceAvg': store.price_avg,
			'reviewCnt': store.review_cnt,
			'tags': store.tags,
			'updatedAt': store.updated_at,
			'viewCnt': store.view_cnt
		}))
		// console.log(resp)
		commit('setStores', stores)
	},
	getSingleStore ({ commit }, storeId) {
		var store = state.stores[storeId-1]
		commit('setSingleStore', store)
	}
}

const mutations = {
	setStores (state, stores) {
		state.stores = stores 
		console.log(state.stores)
	},
	setSingleStore (state, store) {
		state.store = store
	},
	getStoresNameInReviews (state, storesIdArr) {
		// for (var idx in storesIdArr) {
		for (var i=0, item; item=storesIdArr[i]; i++ ) {
			state.storesNameInReviews.push(state.stores[item].name)
		}
	},
}

export default {
	namespaced: true,
	state,
	getters,
	actions,
	mutations,
  }
  