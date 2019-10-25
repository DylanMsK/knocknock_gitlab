const state = {
	stores: [
		{
			id: 1,
			name: '스윗밸런스',
			thumbnail: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRVNHS4l0U1FoL5I-kWK6TuDze7Ta4aMD75Vz4OjK5lEKUuXm5gKw&s',
			subCategory: '기타',
			contact: '02-556-3222',
			addr: '서울 강남구 테헤란로25길 9',
			biztime: '매일 11:30~22:30',
			reviewCnt: 10,
			remainingTime: 60,
			lat: 37.5012272,
			lon: 127.0350094,
		},
		{
			id: 2,
			name: '마구로젠 역삼점',
			thumbnail: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTR0XkJwZO76xd6X1fFoa3c-BucmEExW_csYMKhhcLOko5kIFeE&s',
			subCategory: '생선회',
			contact: '02-573-2777',
			addr: '서울 강남구 논현로86길 32',
			biztime: '토요일 11:30~22:30',
			reviewCnt: 10,
			remainingTime: 60,
			lat: 37.5059506,
			lon: 127.0218631,
		},
		{
			id: 3,
			name: '베이징코야 역삼동점',
			thumbnail: 'https://www.menupan.com/common/service/img_proxy.asp?src=http%3A%2F%2Fpostfiles14.naver.net%2F20121125_253%2Fsj92165_1353847739845phVbD_JPEG%2FDSCF0608.JPG%3Ftype%3Dw2',
			subCategory: '중식당',
			contact: '02-733-5292',
			addr: '서울 강남구 논현로86길 20',
			biztime: '매일 11:30 - 22:00',
			reviewCnt: 10,
			remainingTime: 30,
			lat: 37.511168,
			lon: 127.029248,
		},
		{
			id: 4,
			name: '순남시래기 역삼점',
			thumbnail: 'https://mblogthumb-phinf.pstatic.net/MjAxODA2MjBfMjgw/MDAxNTI5NDc2OTc4Mzcz.d8xBr2qE7kDzXVBYnxb9_66JZVBMaDBKmDUtX8cMKWog.UGEOvhsZwMpUvaNmf6EhOZC8VqOUYK8-jBQK693OHycg.JPEG.kduckyoung/output_3606736563.jpg?type=w800',
			subCategory: '백반,가정식',
			contact: '02-508-0887',
			addr: '서울 강남구 테헤란로34길 5',
			biztime: '평일 11:00~01:00 / 토요일 11:00~24:00',
			reviewCnt: 10,
			remainingTime: 150,
			lat: 37.5059506,
			lon: 127.0219404,
		},
	],
	store: ''
}


const actions = {
	getStores ({ commit}) {
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
	}
}

export default {
	namespaced: true,
	state,
	actions,
	mutations,
  }
  