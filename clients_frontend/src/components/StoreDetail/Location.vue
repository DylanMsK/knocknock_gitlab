<template>
<div>
	<vue-daum-map 
		:appKey="appKey"
		:center.sync="center"
		:level.sync="level"
		:mapTypeId="mapTypeId"
		:libraries="libraries"
		@load="onLoad" 
		class="map-size" />
</div>
</template>

<script>
import VueDaumMap from 'vue-daum-map'
import config from '../../../map.config';
import { mapState, mapActions } from 'vuex'

export default {
	components: {
		VueDaumMap
	},
	data() {
		return {
			storeId: 0,
			appKey: config.appKey,
			center: {lat: 0, lng: 0,},
			level: 3,
			mapTypeId: VueDaumMap.MapTypeId.NORMAL,
			libraries: [],
			map: null,
		}
	},
	created() {
		this.storeId = this.$router.app._route.params.storeId
	},
	computed: {
		...mapState('store', ['store']),
	},
	mounted() {
		this.getSingleStore(this.storeId),
		this.getCenter ()
	},
	methods: {
		...mapActions('store', ['getSingleStore']),
		getCenter () {
			this.center.lat = this.store.lat
			this.center.lng = this.store.lon
		},
		onLoad (map) {
			var bounds = map.getBounds()
			var boundsStr = bounds.toString();
			this.map = map;

			this.curMarker = new kakao.maps.Marker({
				map: map,
				position: new kakao.maps.LatLng(this.center.lat, this.center.lng),
			})
		}
 	}
}
</script>

<style scoped>
.map-size {
	width: 100%;
	height: 350px;
}
</style>