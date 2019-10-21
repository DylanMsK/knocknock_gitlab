<template>
	<div class="mb-12 pb-4">
		<v-tabs
			v-model="tab"
			background-color="transparent"
			grow
		>
			<v-tab
				v-for="item in items"
				:key="item"
			>
				{{ item }}
			</v-tab>
		</v-tabs>

		<v-tabs-items v-model="tab">
			<v-tab-item>
				<v-card flat>
					<Notice />
				</v-card>
			</v-tab-item>
			<v-tab-item>
				<v-card flat>
					<Menu />
				</v-card>
			</v-tab-item>
			<v-tab-item>
				<v-card flat>
					<Location />
				</v-card>
			</v-tab-item>
			<v-tab-item>
				<v-card flat>
					<Review />
				</v-card>
			</v-tab-item>
		</v-tabs-items>
	</div>
</template>

<script>
import Notice from './Notice'
import Menu from './Menu'
import Location from './Location'
import Review from './Review'

export default {
	data() {
		return {
			tab: null,
			items: [
				'공지사항', '메뉴', '지도', '리뷰'
			]
		}
	},
	components: {
		Notice,
		Menu,
		Location,
		Review
	}
}
</script>

<style scoped>
</style>