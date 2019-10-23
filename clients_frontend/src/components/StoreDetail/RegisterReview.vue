<template>
	<!-- Register Review -->
	<v-dialog 
		v-model="dialog" 
		fullscreen
		hide-overlay 
		transition="dialog-bottom-transition"
	>
		<v-card>
			<v-toolbar flat>
				<v-toolbar-title class="font-weight-bold">스윗밸런스 역삼점</v-toolbar-title>
				<v-spacer></v-spacer>
				<v-btn 
					@click="turnOffDialog"
					icon 
				>
					<v-icon>mdi-close</v-icon>
				</v-btn>
			</v-toolbar>
			<v-card-text class="review">
				<v-row>
					<v-col 
						cols="2"
						class="align-self-center"
					>
						<span>평점</span>
					</v-col>
					<v-col cols="10">
						<v-rating 
							v-model="rating"
							dense
							hover
							class="review-rating"
						></v-rating>
					</v-col>
				</v-row>
				<div>
					<p>내용</p>
					<v-textarea
						v-model="content"
						counter
						maxlength="120"
						outlined
						full-width
						auto-grow
						class="font-weight-medium"
					>
					</v-textarea>
				</div>
			</v-card-text>
			<v-card-actions class="px-6">
				<v-btn 
					@click="registerReview"
					block
					color="primary"
					class="review-btn"
				>
					등록
				</v-btn>
			</v-card-actions>
		</v-card>
	</v-dialog>
</template>

<script>
import { mapState, mapMutations } from 'vuex'
 
export default {
	data() {
		return {
			rating: 0,
			content: ''
		}
	},
	computed: {
		...mapState('toggle', {
			dialog: state => state.registerReviewModalShow
		})
	},
	methods: {
		...mapMutations('toggle', ['toggleRegisterReviewModal']),
		turnOffDialog() {
			this.toggleRegisterReviewModal(false)
		},
		registerReview() {
			this.toggleRegisterReviewModal(false)
		}
	}
}
</script>