<template>
	<div>
		<StoreSummary />
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