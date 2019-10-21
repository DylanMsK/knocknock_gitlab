<template>
	<div>
		<!-- SnackBar -->
		<v-snackbar 
			v-model="snackbar"
			:timeout=this.timeout
			bottom
		>
			마감 {{ storeInfo.remainingTime }}분 전
			<v-btn
				color="primary"
				text
				@click="snackbar = false"
			>
				Close
			</v-btn>
		</v-snackbar>

		<!-- Info -->
		<div class="thumbnail-wrap">
			<v-img :src="storeInfo.thumbnail"></v-img>
		</div>
		<div class="mx-5 my-2">
			<!-- <p class="store-remaining">마감 {{ storeInfo.remainingTime }}분 전</p> -->
			<div class="store-title text-center">
				<span class="store-name">{{ storeInfo.name }}</span>
				<span class="store-subcategory">{{ storeInfo.subCategory }}</span>
			</div>
			<div class="store-info text-center">
				<span>최근리뷰 {{ storeInfo.reviewCnt }}</span>
				<v-divider
					vertical 
					class="divider"
				></v-divider>
				<span>{{ storeInfo.contact }}</span>
			</div>
			<v-divider class="my-3"></v-divider>
			<v-row class="charcoal--text">
				<v-col 
					cols="10"
					class="pt-0"
				>
					<p>{{ storeInfo.biztime }}</p>
					<p class="mb-0">{{ storeInfo.addr }}</p>
				</v-col>
				<v-col 
					cols="2"
				>
					<v-btn 
						@click="checkBookmark"
						icon
					>
						<v-icon v-if="!bookmark">mdi-bookmark-outline</v-icon>
						<v-icon v-else>mdi-bookmark-check</v-icon>
					</v-btn>
				</v-col>
			</v-row>
		</div>
	</div>
</template>

<script>
import { mapState } from 'vuex'

export default {
	data() {
		return {
			snackbar: true,
			timeout: 0,
			bookmark: false,
		}
	},
	computed: {
		...mapState({
			storeInfo: state => state.storeInfo.storeInfo,
		})
	},
	methods: {
		checkBookmark() {
			this.bookmark = !this.bookmark
		}
	}
}
</script>

<style scoped>
.thumbnail-wrap {
	width: 100%;
	height: 280px;
}
.store-title {
	padding: 5px;
}
.store-name {
	font-size: 30px;
}
.store-subcategory {
	color: grey;
	padding-left: 15px;
}
.store-remaining {
	color: red;
	font-size: 20px;
}
.store-info {
	color: gray;
	font-size: 15px;
}
.divider {
	color: black; 
	height: 15px;
	margin: 0 10px;
}
.charcoal--text {
	color: rgb(102, 102, 102);
}
</style>