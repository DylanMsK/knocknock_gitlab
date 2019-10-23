<template>
	<div class="pa-6">
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
				background-color="yellow darken-3"
				color="yellow darken-3"
				class="review-rating mr-3"
			></v-rating>
			<v-textarea 
				:value="review.content"
				outlined
				counter
				maxlength="120"
				class="mb-0 pt-2"
			>
			</v-textarea>
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
				@click="goTo"
				icon	
				class="review-btn"	
			>
				취소
			</v-btn>
		</div>
	</div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import router from '../../router'

export default {
	data() {
		return {
			reviewId: 0,
		}
	},
	computed: {
		...mapGetters('review', {
			review: 'getReview'
		})
	},
	created() {
		this.reviewId = this.$router.app._route.params.reviewId
	},
	mounted() {
		this.getSingleReview(this.reviewId)
	},
	methods: {
		...mapActions('review', ['getSingleReview']),
		goTo() {
			router.go(-1)
		}
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