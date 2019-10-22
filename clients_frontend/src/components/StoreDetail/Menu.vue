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
			<v-tooltip 
				bottom
				max-width="350px"
			>
				<template v-slot:activator="{ on }">
					<span v-on="on">{{ menu.name }}</span>
				</template>
				<span>{{ menu.name }}</span>
			</v-tooltip>
				<!-- {{ menu.name }} -->
			</v-col>
			<v-col 
				cols="4"
				class="menu-price"
			>	
				{{ menu.price }}원
			</v-col>
			<v-col 
				v-if="idx != menus.length -1"
				cols="12"
				class="menu-divider"
			>
				<v-divider></v-divider>
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
	font-size: 15px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
	padding: 4px 12px;
}
.menu-price {
	text-align: right;
	font-size: 15px;
	padding: 4px 12px;
}
.menu-divider {
	padding: 4px 12px;
}
</style>