<template>
	<div class="map-wrap">
		<vue-daum-map
			:appKey="appKey"
			:center.sync="center"
			:level.sync="level"
			:mapTypeId="mapTypeId"
			:libraries="libraries"
			@load="onLoad"
			@dblclick="zoomIn"
			@click="onMapEvent($event)"
			@dragend="changedLoc"
			@zoom_changed="changedLoc"
			@bounds_changed="getAddr"
			class="map" />
		<div class="hAddr">
			<p class="ma-0">{{ this.centerAddr }}</p>
		</div>
		<div class="zoomControl radius_border">
			<v-btn 
				@click="zoomIn"
				icon
			>
				<v-icon>mdi-plus</v-icon>
			</v-btn>
			<v-divider class="color_919191"></v-divider>
			<v-btn 
				@click="zoomOut"
				icon
			>
				<v-icon>mdi-minus</v-icon>
			</v-btn>
		</div>
		<div class="gpsBtn radius_border">
			<v-btn
				@click="currentAddr"
				icon
			>
				<v-icon>mdi-crosshairs-gps</v-icon>
			</v-btn>
		</div>
		<transition
			name="fade"
		>
			<div 
				v-if="refresh"
				@click="refreshStoreList"
				class="refreshBtn radius_border"
			>
				<v-btn>
					<v-icon>mdi-refresh</v-icon>여기에서 재탐색
				</v-btn>
			</div>
		</transition>
	</div>
</template>

<script>
import VueDaumMap from 'vue-daum-map'
import { mapState, mapGetters, mapActions } from 'vuex'

export default {
	components: {
		VueDaumMap
	},
	data() {
		return {
			appKey: process.env.VUE_APP_KEY,
			center: {lat: 37.553190, lng: 126.972759}, 
			level: 3,
			mapTypeId: VueDaumMap.MapTypeId.NORMAL,
			libraries: ['services'],
			map: null,
			curMarker: null,
			pointMarker: null,
			centerAddr: '',
			refresh: false,
		}
	},
	computed: {
		...mapGetters('store', ['storesLoc']),
		...mapState('store', ['stores'])
	},
	methods: {
		...mapActions('store', ['getStores']),
		onLoad (map) {
			this.map = map
			// 지도가 load 되면 현재위치를 center로 지정
			if (navigator.geolocation) {
				navigator.geolocation.getCurrentPosition((position) => {
					var lat = position.coords.latitude,
							lng = position.coords.longitude

					// 지도 중심위치 바꿔줌
					this.center.lat = lat
					this.center.lng = lng

					// 현재 위치 마커 표시
					var imageSrc = 'http://testrottenwifi.ito.lt/bundles/itowififront/images/my-location-icon.png',
							imageSize = new kakao.maps.Size(70, 70),
							imageOption = {offset: new kakao.maps.Point(27, 69)}; 
					var curMarkerImage = new kakao.maps.MarkerImage(imageSrc, imageSize, imageOption)
					this.curMarker = new kakao.maps.Marker({
						map: map,
						position: new kakao.maps.LatLng(lat, lng),
						image: curMarkerImage
					})
				})
			} else {
				console.log('geolocation 사용 불가능')
			}
			this.getStoreList()
			// // 클릭한 곳 마커 표시
			// this.pointMarker = new kakao.maps.Marker({
			// 	map: map,
			// 	position: ''
			// })
			// this.searchAddrFromCoords(map.getCenter(), this.displayCenterInfo);
			this.markingStore()
		},
		markingStore () {
			// stores 불러와서 마커 찍기
			for (var idx in this.storesLoc) {
				var storeLoc = new kakao.maps.LatLng(this.storesLoc[idx].latlon.lat, this.storesLoc[idx].latlon.lon)
				var storeMarker = new kakao.maps.Marker({
					map: this.map,
					position: storeLoc
				})

				var infowindow = new kakao.maps.InfoWindow({
					position : storeLoc, 
					content : `<div style="width: 100%; padding: 5px;">${this.storesLoc[idx].name}</div>`
				});
				
				infowindow.open(this.map, storeMarker);
			// for (var idx in this.stores) {
			// 	var storeLoc = new kakao.maps.LatLng(this.storesLoc[idx].latlon.lat, this.storesLoc[idx].latlon.lon)
			// 	var storeMarker = new kakao.maps.Marker({
			// 		map: this.map,
			// 		position: storeLoc
			// 	})

			// 	var infowindow = new kakao.maps.InfoWindow({
			// 		position : storeLoc, 
			// 		content : `<div style="width: 100%; padding: 5px;">${this.storesLoc[idx].name}</div>`
			// 	});
				
			// 	infowindow.open(this.map, storeMarker);
			}
		},
		onMapEvent (params) {
			// this.pointMarker.setPosition(params[0].latLng)
			this.searchAddrFromCoords(params[0].latLng, this.displayCenterInfo);
		},
		changedLoc () {
			this.refresh = true
			this.searchAddrFromCoords(this.map.getCenter(), this.displayCenterInfo);
		},
		refreshStoreList() {
			this.refresh = false
			this.getStoreList()
		},
		getStoreList() {
			this.getStores({
				'lat': this.center.lat,
				'lon': this.center.lng,
				'hour': 0,
				'd': 500
			})
			console.log(this.stores)
			this.markingStore()
		},
		getAddr () {
			this.searchAddrFromCoords(this.map.getCenter(), this.displayCenterInfo);
		},
		searchAddrFromCoords (coords, callback) {
			var geocoder = new kakao.maps.services.Geocoder();
			geocoder.coord2RegionCode(coords.getLng(), coords.getLat(), callback);
		},
		displayCenterInfo (result, status) {
    if (status === kakao.maps.services.Status.OK) {
			var infoDiv = document.getElementById('centerAddr');
			for(var i = 0; i < result.length; i++) {
            // 행정동의 region_type 값 'H' 
					if (result[i].region_type === 'H') {
							this.centerAddr = result[i].address_name;
							break;
			}}}
		},
		currentAddr () {
			if (navigator.geolocation) {
					navigator.geolocation.getCurrentPosition((position) => {
						var lat = position.coords.latitude,
								lng = position.coords.longitude

						// 지도 중심위치 바꿔줌
						this.center.lat = lat
						this.center.lng = lng

						var coords = new kakao.maps.LatLng(lat, lng);
						this.map.setCenter(coords);
						this.level = 3

						this.curMarker.setPosition(coords)
			})}
		},
		zoomIn () {
			if (this.level > 1) {
				this.level -= 1
			}
		},
		zoomOut () {
			if (this.level < 14) {
				this.level += 1
			}
		}
	}
}
</script>

<style scoped>
.map-wrap {
	width: 100vw;
	height: 50vh;
}
.map {
	width: 100vw;
	height: 50vh;
}
.hAddr {
	position: absolute;
	background-color: rgba(255, 255, 255, 0.8);
	top: 105px;
	left: 10px;
	padding: 10px 10px;
	z-index: 1;
}
.zoomControl {
	position: absolute;
	top: 200px;
	right: 10px;
	z-index: 1;
	width: 40px;
	background-color: white;
	text-align: center;
}
.gpsBtn {
	position: absolute;
	top: 55vh;
	right: 10px;
	z-index: 1;
	width: 40px;
	background-color: white;
	text-align: center;
}
.refreshBtn {
	position: absolute;
	top: 55vh;
	z-index: 1;
	width: 150px;
	background-color: white;
	margin: 0 30vw;
}
.radius_border {
  border: 1px solid #919191;
  border-radius: 5px;
}
.color_919191 {
	border-color: #919191 !important;
}

.fade-enter-active,
.fade-leave-active {
	transition-duration: 0.2s;
	transition-property: opacity;
	transition-timing-function: ease;
}

.fade-enter,
.fade-leave-active {
	opacity: 0
}
</style>