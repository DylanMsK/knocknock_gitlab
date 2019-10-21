<template>
	<div class="ma-2">
		<v-btn 
			@click="dialog=true"
			block
			color="primary"
			class="my-2"
		>
			리뷰 남기기
		</v-btn>
		<v-card
			v-for="idx in 5"
			:key="idx"
			outlined
			class="mb-1"
		>
		<div class="d-flex">
			<v-card-title class="pa-4 pb-0">
				hay***
			</v-card-title>
			<v-spacer></v-spacer>
			<v-btn 
				icon
				class="pa-4"
			>
				<v-icon>mdi-dots-vertical</v-icon>
			</v-btn>
		</div>
			<v-card-subtitle class="py-0">
				2019-10-21
			</v-card-subtitle>
			<v-card-text class="pa-4 black--text">
				<p class="ellipsis-3line">
					{{ review }}
				</p>
			</v-card-text>
		</v-card>

		<!-- Register Review -->
		<v-dialog 
			v-model="dialog" 
			fullscreen
			hide-overlay 
			transition="dialog-bottom-transition"
		>
      <v-card>
        <v-toolbar 
					dark 
					color="primary"
				>
          <v-toolbar-title>리뷰 남기기</v-toolbar-title>
					<v-spacer></v-spacer>
          <v-btn 
						@click="dialog = false"
						icon 
						dark 
					>
            <v-icon>mdi-close</v-icon>
          </v-btn>
        </v-toolbar>
				<div class="ma-5">
					<p class="review-rating">평점</p>
					<v-rating 
						v-model="rating"
						hover
						dense
						large
					></v-rating>
					<p>내용</p>
					<v-text-field outlined></v-text-field>
				</div>
      </v-card>
    </v-dialog>

	</div>
</template>

<script>
export default {
	data() {
		return {
			dialog: false,
			rating: 5,
			review: '친구의 강력추천으로 가게된 역삼역 스윗밸런스!! 샐러드 카페 보다는 식당에 가까웠어요. 역삼역 가까이 위치해서 접근성이 좋았어요. 메뉴의 가격대도 적당하고 맛있었어요.'
		}
	},
}
</script>

<style scoped>
.review-rating {
	font-size: 20px;
	font-weight: 700;
}
</style>