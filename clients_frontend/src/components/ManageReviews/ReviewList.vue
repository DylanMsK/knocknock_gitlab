<template>
	<v-container>
		<p class="font-headline">리뷰관리</p>
		<div v-if="reviews.length">
			<div
				v-for="(review, idx) in reviews"
				:key="idx"	
				class="mb-12"
			>	
				<Review :review="review" />
			</div>
		</div>
		<div v-else>
			<p>등록된 리뷰가 없습니다.</p>
		</div>
	</v-container>
</template>

<script>
import { mapState, mapGetters, mapMutations } from 'vuex'
import Review from './Review'

export default {
	data() {
		return {
			rating: 0,
		}
	},
	components: {
		Review
	},
	computed: {
		...mapGetters('review', {
			reviews: 'getAllReviews',
			storesId: 'getStoresIdInReviews'
		}),
	},
	mounted() {
		this.getStoresName()
	},
	methods: {
		...mapMutations('store', ['getStoresNameInReviews']),
		getStoresName () {
			this.getStoresNameInReviews(this.storesId)
		}
	}
}
</script>

<style scoped>
.font-headline {
  font-size: 24px;
  font-weight: 700;
}
</style>