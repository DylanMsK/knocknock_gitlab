<template>
	<v-container>
		<p class="font-headline">리뷰관리</p>
		<div
			v-for="(review, idx) in reviews"
			:key="idx"	
			class="mb-12"
		>
			<Review :reviewId="idx" />
		</div>
	</v-container>
</template>

<script>
import { mapGetters } from 'vuex'
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
			reviews: 'getAllReviews'
		})
	}
}
</script>

<style scoped>
.font-headline {
  font-size: 24px;
  font-weight: 700;
}
</style>