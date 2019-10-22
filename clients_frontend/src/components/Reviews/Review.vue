<template>
	<div>
		<div class="pl-1">
			<span class="store-title">store name</span>
			<v-btn icon>
				<v-icon class="grey--text">mdi-chevron-right</v-icon>
			</v-btn>
		</div>
		<div>
			<v-rating 
				v-model="review.score"
				dense
				small
				background-color="yellow darken-3"
				color="yellow darken-3"
				readonly
				class="review-rating mr-3"
			></v-rating>
			<span class="caption">2019-10-22</span>
		</div>
		<div class="pt-2 pl-1">
			<p class="mb-0">{{ review.content }}</p>
		</div>
		<div>
			<v-btn
				icon
				color="primary"
				class="review-btn"	
			>
				수정
			</v-btn>
			<v-divider
				vertical 
				class="vertical-divider"
			></v-divider>
			<v-btn 
				icon	
				color="primary"
				class="review-btn"	
			>
				삭제
			</v-btn>
		</div>
	</div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
	props: {
		reviewId: {
			type: Number,
			default: 0,
		}
	},
	computed: {
		...mapGetters('review', {
			review: 'getReview'
		})
	},
	created() {
		this.getSingleReview(this.reviewId)
	},
	methods: {
		...mapActions('review', ['getSingleReview'])
	}
}
</script>

<style scoped>
.store-title {
	font-size: 20px;
	font-weight: 500;
	vertical-align: middle;
}
.review-rating {
	display: inline-block;
}
.review-btn {
	font-weight: 600;
	text-align: left;
}
.vertical-divider {
	color: black; 
	height: 15px;
	margin: 0 10px;
}
</style>