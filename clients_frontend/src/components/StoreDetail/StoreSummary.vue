<template>
	<div>
		<!-- Info -->
		<div class="thumbnail-wrap">
			<v-img :src="storeInfo.thumbnail"></v-img>
		</div>
		<div class="mx-5 my-2">
			<div class="store-title text-center">
				<span class="store-name">{{ storeInfo.name }}</span>
				<span class="store-subcategory">{{ storeInfo.subCategory }}</span>
			</div>
			<div class="store-info text-center">
				<span>최근리뷰 {{ storeInfo.reviewCnt }}</span>
				<v-divider
					vertical 
					class="vertical-divider"
				></v-divider>
				<span class="primary--text">{{ storeInfo.contact }}</span>
			</div>
			<v-divider class="my-2"></v-divider>
			<v-row class="charcoal--text">
				<v-col cols="12">
					<p class="store-remaining">마감 {{ storeInfo.remainingTime }}분 전</p>
				</v-col>
				<v-col 
					cols="10"
					class="pt-0"
				>
					<p class="mb-2">
						<v-icon class="store-icon">mdi-clock-outline</v-icon><span>{{ storeInfo.biztime }}</span>
					</p>
					<p class="mb-2">
						<v-icon class="store-icon">mdi-map-marker-outline</v-icon><span>{{ storeInfo.addr }}</span>
					</p>
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
	font-size: 28px;
}
.store-subcategory {
	color: grey;
	font-size: 14px;
	padding-left: 12px;
}
.store-remaining {
	background-color: #1976d2;
	color: white;
	/* color: red; */
	font-size: 20px;
	font-weight: 700; 
	margin: 0;
	padding: 5px 10px;
}
.store-info {
	color: gray;
	font-size: 14px;
}
.vertical-divider {
	color: black; 
	height: 15px;
	margin: 0 10px;
}
.store-icon {
	color: darkgray;
	margin-right: 8px;
}
.charcoal--text {
	color: rgb(102, 102, 102);
}
</style>