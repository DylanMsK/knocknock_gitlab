<template>
	<v-list 
		flat 
		class="storelist py-0"
	>
		<v-list-item 
			v-for="(store, idx) in stores"
			:key=idx
			@click="goTo('store-detail', idx)"
			class="d-block px-0 py-1"
		>
			<div class="store-content">
				<div class="store-title">{{ store.title }}</div>
				<div class="store-subcategory">{{ store.subCategory }}</div>
				<div class="ellipsis">
					<div class="store-remainingtime">마감 {{ store.remainingTime }}분 전</div>
					<v-divider vertical class="divider"></v-divider>
					<div class="store-biztime">{{ store.biztime }}</div>
				</div>
				<div class="ellipsis">
					<div class="store-biztel">{{ store.biztel }}</div>
					<v-divider vertical class="divider"></v-divider>
					<div class="store-addr">{{ store.addr }}</div>
				</div>
			</div>
			<v-divider 
				v-if="idx != stores.length -1"
				class="mt-1"
			></v-divider>
		</v-list-item>
	</v-list>
</template>

<script>
import router from '../../router'

export default {
	data() {
		return {
			stores: [
				{
					title: '마구로젠 역삼점',
					subCategory: '생선회',
					addr: '서울 강남구 논현로86길 32',
					biztel: '02-573-2777',
					biztime: '토요일 11:30~22:30 일요일 몇시까지',
					remainingTime: '60',
				},
				{
					title: '베이징코야 역삼동점',
					subCategory: '중식당',
					addr: '서울 강남구 논현로86길 어떤빌딩 몇층',
					biztel: '02-573-2777',
					biztime: '매일 11:30~22:30',
					remainingTime: '30',
				},
				{
					title: '순남시래기 역삼점',
					subCategory: '백반, 가정식',
					addr: '서울 강남구 논현로86길 32',
					biztel: '02-573-2777',
					biztime: '토요일 11:30~22:30',
					remainingTime: '30',
				},
				{
					title: '베이징코야 역삼동점',
					subCategory: '중식당',
					addr: '서울 강남구 논현로86길 어떤빌딩 몇층',
					biztel: '02-573-2777',
					biztime: '매일 11:30~22:30',
					remainingTime: '30',
				},
				{
					title: '순남시래기 역삼점',
					subCategory: '백반, 가정식',
					addr: '서울 강남구 논현로86길 32',
					biztel: '02-573-2777',
					biztime: '토요일 11:30~22:30',
					remainingTime: '30',
				},
			]
		}
	},
	methods: {
		goTo (path, storeId) {
			router.push({ 'name': path })
		}
	}
}
</script>

<style scoped>
.storelist {
	height: 38vh;
	overflow: auto;
	/* border: 1px solid rgba(0, 0, 0, 0.2) !important;  */
	border-radius: 5px;
}
.store-content {
	padding: 0 15px;
}
.store-title {
	display: inline;
	font-weight: 700; 
}
.store-subcategory {
	display: inline;
	font-size: 14px;
	color: gray;
	padding: 10px 0 0 5px;
}
.store-remainingtime {
	display: inline;
	color: red;
}
.store-biztime {
	display: inline;
	font-size: 14px;
	padding: 0;
}
.store-biztel {
	display: inline;
	font-size: 14px;
}
.store-addr {
	display: inline;
	font-size: 14px;	
	padding: 0;
}
.ellipsis {
	display: block;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.divider {
	color: black; 
	height: 15px;
	margin: 0 10px;
}
</style>