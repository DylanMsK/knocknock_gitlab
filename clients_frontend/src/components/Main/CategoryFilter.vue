<template>
	<v-layout row class="pt-0 ma-0">
		<v-row class="category">
			<v-col 
				v-for="(item, i) in categoryItems"
				:key="i"
				cols="4"
				class="items"
			>
				<v-flex class="text-center item-box">
					<v-img :src="item.icon" class="store-icon"></v-img>
					<p class="mb-0">{{ item.title }}</p>
				</v-flex>
			</v-col>
		</v-row>
	</v-layout>
</template>

<script>
export default {
	data() {
		return {
			categoryItems: [
				{ title: '한식', icon: 'https://image.flaticon.com/icons/svg/135/135669.svg'},
				{ title: '양식', icon: 'https://image.flaticon.com/icons/svg/135/135644.svg'},
				{ title: '아시아음식', icon: 'https://image.flaticon.com/icons/svg/135/135658.svg'},
				{ title: '일식', icon: 'https://image.flaticon.com/icons/svg/135/135659.svg'},
				{ title: '중식', icon: 'https://image.flaticon.com/icons/svg/135/135769.svg'},
				{ title: '분식', icon: 'https://image.flaticon.com/icons/svg/135/135599.svg'},
				{ title: '카페', icon: 'https://image.flaticon.com/icons/svg/135/135766.svg'},
				{ title: '뷔페', icon: 'https://image.flaticon.com/icons/svg/135/135607.svg'},
				{ title: '기타', icon: 'https://image.flaticon.com/icons/svg/135/135561.svg'},
				// '한식', '양식', '아시아음식', '일식', '중식', '분식', '카페', '뷔페', '기타'
			]
		}
	}
}
</script>

<style scoped>
.category {
	margin: 0;
	padding: auto;
}
.category .items {
	height: 12.7vh;
	border-top: 1px solid rgba(0, 0, 0, 0.1);
	border-right: 1px solid rgba(0, 0, 0, 0.1);
	padding: 0;
}
.item-box {
	padding-top: 3vh;
}
.store-icon {
	width: 40px;
	margin: 0 auto;
}
</style>