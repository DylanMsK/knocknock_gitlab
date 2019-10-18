<template>
	<v-container row class="pt-0">
		<v-row class="category">
			<v-col 
				v-for="i in 9"
				:key="i"
				cols="4"
				class="item"
			>
				dsdf
			</v-col>
		</v-row>
	</v-container>
</template>

<style scoped>
.category {
	border: 1px solid rgba(0, 0, 0, 0.2);
	margin: 0;
	padding: auto;
}
.category .item {
	height: 11vh;
}
</style>