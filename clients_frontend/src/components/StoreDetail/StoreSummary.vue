<template>
	<div>
		<!-- Info -->
		<div class="thumbnail-wrap">
			<v-img :src="store.thumbnail" class="thumbnail"></v-img>
		</div>
		<div class="mx-5 my-2">
			<div class="store-title text-center">
				<span class="store-name">{{ store.name }}</span>
				<span class="store-subcategory">{{ store.subCategory }}</span>
			</div>
			<div class="store-info text-center">
				<span>최근리뷰 {{ store.reviewCnt }}</span>
				<v-divider
					vertical 
					class="vertical-divider"
				></v-divider>
				<span class="primary--text">{{ store.contact }}</span>
			</div>
			<v-divider class="my-2"></v-divider>
			<v-row class="charcoal--text">
				<v-col cols="12">
					<p class="store-remaining">마감 {{ store.remainingTime }}분 전</p>
				</v-col>
				<v-col 
					cols="10"
					class="pt-0"
				>
					<div class="mb-2 d-flex">
						<v-col cols="1" class="pa-0">
							<v-icon class="store-icon">mdi-clock-outline</v-icon>
						</v-col>
						<v-col cols="11" class="py-0">
							<span>{{ store.biztime }}</span>
						</v-col>
					</div>
					<div class="mb-2 d-flex">
						<v-col cols="1" class="pa-0">
							<v-icon class="store-icon">mdi-map-marker-outline</v-icon>
						</v-col>
						<v-col cols="11" class="py-0">
							<span>{{ store.roadAddr }}</span>
						</v-col>
					</div>
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
import { mapState, mapActions } from 'vuex'

export default {
	data() {
		return {
			storeId: 0,
			snackbar: true,
			timeout: 0,
			bookmark: false,
		}
	},
	created() {
		this.storeId = this.$router.app._route.params.storeId
	},
	computed: {
		...mapState('store', ['store'])
	},
	mounted() {
		this.getSingleStore(this.storeId)
	},
	methods: {
		...mapActions('store', ['getSingleStore']),
		checkBookmark() {
			this.bookmark = !this.bookmark
		}
	}
}
</script>

<style scoped>
.thumbnail {
	width: 100%;
	height: 280px;
	object-fit: cover;
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