<template>
	<div>
		<StoreSummary />
		<div class="divide-box"></div>
		<StoreInfo />
	</div>
</template>

<script>
import StoreSummary from '../components/StoreDetail/StoreSummary'
import StoreInfo from '../components/StoreDetail/StoreInfo'

export default {
	components: {
		StoreSummary,
		StoreInfo
	}
}
</script>

<style scoped>
.divide-box {
	width: 100%; 
	height: 30px; 
	background-color: whitesmoke;
}
</style>