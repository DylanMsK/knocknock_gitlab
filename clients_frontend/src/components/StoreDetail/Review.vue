<template>
	<div class="ma-2">
		<v-btn 
			@click="registerReview"
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
					<v-list-item 	@click="goTo('modify-review', 1)">
						<v-list-item-title>수정</v-list-item-title>
					</v-list-item>
					<v-list-item @click="dialog=true">
						<v-list-item-title>삭제</v-list-item-title>
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
		<RegisterReview />

		<!-- Chechk Modal -->
		<v-dialog
      v-model="dialog"
      max-width="290"
    >
      <v-card class="text-center">
        <p class="pt-5">
          리뷰를 정말 삭제하시겠습니까?
        </p>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="blue darken-3"
            text
            @click="dialog=false"
          >
            닫기
          </v-btn>
          <v-btn
            color="blue darken-3"
            text
            @click="dialog=false"
          >
            확인
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
	</div>
</template>

<script>
import { mapMutations } from 'vuex'
import router from '../../router'
import RegisterReview from './RegisterReview'

export default {
	components: {
		RegisterReview
	},
	data() {
		return {
			dialog: false,
			rating: 5,
			content: '친구의 강력추천으로 가게된 역삼역 스윗밸런스!! 샐러드 카페 보다는 식당에 가까웠어요. 역삼역 가까이 위치해서 접근성이 좋았어요. 메뉴의 가격대도 적당하고 맛있었어요.',
			items: [
        { title: '수정', params: 'true' },
        { title: '삭제', params: 'true' },
      ],
		
		}
	},
	methods: {
		...mapMutations('toggle', ['toggleRegisterReviewModal']),
		goTo (path, params) {
			router.push({ name: path, params:{ reviewId: params} });
		},
		registerReview () {
			this.toggleRegisterReviewModal(true)
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