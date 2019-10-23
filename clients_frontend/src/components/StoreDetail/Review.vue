<template>
	<div class="ma-2">
		<v-btn 
			@click="dialog=true"
			text
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
			<v-card-title class="pb-0">
				hay***
			</v-card-title>
			<v-spacer></v-spacer>
			<v-menu bottom left>
				<template v-slot:activator="{ on }">
					<v-btn
						icon
						v-on="on"
						class="mt-2 mx-2"
					>
						<v-icon>mdi-dots-vertical</v-icon>
					</v-btn>
				</template>

				<v-list>
					<v-list-item
						v-for="(item, i) in items"
						:key="i"
						@click=""
					>
						<v-list-item-title>{{ item.title }}</v-list-item-title>
					</v-list-item>
				</v-list>
			</v-menu>
		</div>
			<v-card-subtitle class="py-0">
				<v-rating 
					v-model="rating"
					dense
					small
					color="yellow darken-3"
					readonly
					class="review-rating mr-3"
				></v-rating>
				2019-10-21
			</v-card-subtitle>
			<v-card-text class="pa-4 black--text">
				<p class="ellipsis-3line">
					{{ content }}
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
        <v-toolbar flat>
          <v-toolbar-title class="font-weight-bold">스윗밸런스 역삼점</v-toolbar-title>
					<v-spacer></v-spacer>
          <v-btn 
						@click="dialog = false"
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
	</div>
</template>

<script>
export default {
	data() {
		return {
			dialog: false,
			rating: 5,
			content: '친구의 강력추천으로 가게된 역삼역 스윗밸런스!! 샐러드 카페 보다는 식당에 가까웠어요. 역삼역 가까이 위치해서 접근성이 좋았어요. 메뉴의 가격대도 적당하고 맛있었어요.',
			items: [
        { title: '수정' },
        { title: '삭제' },
      ],
		
		}
	},
	methods: {
		registerReview () {
			this.dialog = false
		}
	}
}
</script>

<style scoped>
.review {
	font-size: 16px;
	font-weight: 700;
}
.review-rating {
	display: inline-block;
	text-align: right;
}
.review-btn{
	font-weight: 700;
	font-size: 16px;
}
</style>