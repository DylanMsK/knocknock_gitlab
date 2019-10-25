import api from "../../services/api"

const state = {
	stores: [
		{
			id: 1,
			name: '스윗밸런스',
			thumbnail: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRVNHS4l0U1FoL5I-kWK6TuDze7Ta4aMD75Vz4OjK5lEKUuXm5gKw&s',
			subCategory: '기타',
			contact: '02-556-3222',
			roadAddr: '서울 강남구 테헤란로25길 9',
			commonAddr: '서울 강남구',
			addr: '역삼동 644-18',
			biztime: '매일 11:30~22:30',
			reviewCnt: 10,
			remainingTime: 60,
			lat: 37.5012272,
			lon: 127.0350094,
			description: '',
		},
		{
			id: 2,
			name: '마구로젠 역삼점',
			thumbnail: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTR0XkJwZO76xd6X1fFoa3c-BucmEExW_csYMKhhcLOko5kIFeE&s',
			subCategory: '생선회',
			contact: '02-573-2777',
			roadAddr: '서울 강남구 논현로86길 32',
			commonAddr: '',
			addr: '',
			biztime: '토요일 11:30~22:30',
			reviewCnt: 10,
			remainingTime: 60,
			lat: 37.5059506,
			lon: 127.0218631,
			description: '',
		},
		{
			id: 3,
			name: '베이징코야 역삼동점',
			thumbnail: 'https://www.menupan.com/common/service/img_proxy.asp?src=http%3A%2F%2Fpostfiles14.naver.net%2F20121125_253%2Fsj92165_1353847739845phVbD_JPEG%2FDSCF0608.JPG%3Ftype%3Dw2',
			subCategory: '중식당',
			contact: '02-733-5292',
			roadAddr: '서울 강남구 논현로86길 20',
			commonAddr: '',
			addr: '',
			biztime: '매일 11:30 - 22:00',
			reviewCnt: 10,
			remainingTime: 30,
			lat: 37.511168,
			lon: 127.029248,
			description: '',
		},
		{
			id: 4,
			name: '순남시래기 역삼점',
			thumbnail: 'https://mblogthumb-phinf.pstatic.net/MjAxODA2MjBfMjgw/MDAxNTI5NDc2OTc4Mzcz.d8xBr2qE7kDzXVBYnxb9_66JZVBMaDBKmDUtX8cMKWog.UGEOvhsZwMpUvaNmf6EhOZC8VqOUYK8-jBQK693OHycg.JPEG.kduckyoung/output_3606736563.jpg?type=w800',
			subCategory: '백반,가정식',
			contact: '02-508-0887',
			roadAddr: '서울 강남구 테헤란로34길 5',
			commonAddr: '',
			addr: '',
			biztime: '평일 11:00~01:00 / 토요일 11:00~24:00',
			reviewCnt: 10,
			remainingTime: 150,
			lat: 37.5059506,
			lon: 127.0219404,
			description: '',
		},
	],
	store: '',
	// store name in Management Review
	storesNameInReviews: [],
	// store location in Map component
	storesLoc: [],
	// store list 요청하기 위한 정보들 
	requestObj: {
		'lat': 0,
		'lon': 0,
		'hour': 0,
		'd': 500, 
	},
}

const getters = {
	storesLoc (state) {
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
	async getStores ({ commit}) {
		const obj = state.requestObj
		const resp = await api.searchStores(obj.lon, obj.lat, obj.hour, obj.d)
		console.log(resp)
		commit('setStores')
	},
	getSingleStore ({ commit }, storeId) {
		var store = state.stores[storeId-1]
		commit('setSingleStore', store)
	}
}

const mutations = {
	setStores (state) {
		//
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
	getRequestObj (state, params) {
		console.log(params)
		state.requestObj = params
	}
}

export default {
	namespaced: true,
	state,
	getters,
	actions,
	mutations,
  }
  