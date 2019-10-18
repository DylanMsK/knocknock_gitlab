<template>
	<div>
		<Map />
		<StoreList v-if="!filterToggle" />
		<CategoryFilter v-else />
	</div>
</template>

<script>
import { mapState } from 'vuex'
import Map from '../components/Main/Map'
import StoreList from '../components/Main/StoreList'
import CategoryFilter from '../components/Main/CategoryFilter'

export default {
  components: {
		Map,
		StoreList,
		CategoryFilter
	},
	computed: {
		...mapState({
			filterToggle: state => state.toggle.filterShow
		})
	}
}
</script>