<template>
	<div class="mx-5 my-2">
		<v-row
			v-for="(menu, idx) in menus"
			:key="idx"
		>
			<v-col 
				cols="8"
				class="menu-name"
			>	
				{{ menu.name }}
			</v-col>
			<v-col 
				cols="4"
				class="menu-price"
			>	
				{{ menu.price }}원
			</v-col>
		</v-row>
	</div>
</template>

<script>
import { mapState } from 'vuex'

export default {
	computed: {
		...mapState({
			menus: state => state.menu.menu
		})
	},
}
</script>

<style scoped>
.menu-name {
	display: block;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
	padding: 4px 12px;
}
.menu-price {
	text-align: right;
	padding: 4px 12px;
}
</style>