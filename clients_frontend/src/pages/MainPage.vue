<template>
	<div>
		<div class="mb-1 px-1 timecontrol">
			<v-btn 
				v-if="!filterToggle"
				@click="turnonFilter"
				icon
			>
				<v-icon>mdi-filter-outline</v-icon>
			</v-btn>
			<v-btn 
				v-else
				@click="turnonFilter"
				icon
			>
				<v-icon>mdi-store</v-icon>
			</v-btn>
			<v-spacer></v-spacer>
			<v-btn-toggle 
				v-model="toggle_exclusive"
				color="primary"
			>
				<v-btn @click="serveTime(0)">현재 시간</v-btn>
				<v-btn @click="serveTime(1)">1시간</v-btn>
				<v-btn @click="serveTime(2)">2시간</v-btn>
				<v-btn @click="serveTime(3)">3시간</v-btn>
			</v-btn-toggle>
		</div>
		<Map />
		<StoreList v-if="!filterToggle" />
		<CategoryFilter v-else />
	</div>
</template>

<script>
import { mapState, mapMutations } from 'vuex'
import Map from '../components/Main/Map'
import StoreList from '../components/Main/StoreList'
import CategoryFilter from '../components/Main/CategoryFilter'

export default {
	data() {
    return{
      toggle_exclusive: 0,
    }
	},
  components: {
		Map,
		StoreList,
		CategoryFilter
	},
	computed: {
		...mapState({
			filterToggle: state => state.toggle.filterShow
		})
	},
	mounted() {
		this.toggleHeader(true)
	},
	methods: {
		...mapMutations('toggle', ['toggleFilter']),
		...mapMutations('toggle', ['toggleHeader']),
    turnonFilter() {
      this.toggleFilter(!this.filterToggle)
		},
		serveTime(params) {
			console.log(params)
		}
	}
}
</script>

<style scoped>
.timecontrol {
  display: flex; 
  justify-content: space-between;
  /* display: inline; */
}
.timecontrol button {
  height: 36px !important;
  font-weight: bold;
}
</style>