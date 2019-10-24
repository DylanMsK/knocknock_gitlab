<template>
	<div class="map-wrap">
		<vue-daum-map
			:appKey="appKey"
			:center.sync="center"
			:level.sync="level"
			:mapTypeId="mapTypeId"
			:libraries="libraries"
			@load="onLoad"
			@click="onMapEvent($event)"
			class="map" />
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
	</div>
</template>

<script>
import VueDaumMap from 'vue-daum-map'

export default {
	components: {
		VueDaumMap
	},
	data() {
		return {
			appKey: '74d1e73195cf5ac2a0bb5a6b0aa60434',
			center: {lat: 37.553190, lng: 126.972759}, 
			level: 3,
			mapTypeId: VueDaumMap.MapTypeId.NORMAL,
			libraries: [],
			map: null
		}
	},
	methods: {
		onLoad (map) {
			// 지도가 load 되면 현재위치를 center로 지정
			if (navigator.geolocation) {
				navigator.geolocation.getCurrentPosition((position) => {
					var lat = position.coords.latitude,
							lng = position.coords.longitude

					// 지도 중심위치 바꿔줌
					this.center.lat = lat
					this.center.lng = lng

					// 현재 위치 마커 표시. 
					// 현재 위치와 클릭한 곳 마커 이미지 어떻게 구분할지 못정해서 따로 빼놓는데, 구분 가능하면 아래코드 지우고 displayMarker 호출
					this.map = map					
					var imageSrc = 'http://testrottenwifi.ito.lt/bundles/itowififront/images/my-location-icon.png',
							imageSize = new kakao.maps.Size(70, 70),
							imageOption = {offset: new kakao.maps.Point(27, 69)}; 
					var markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize, imageOption)
					var marker = new kakao.maps.Marker({
						map: map,
						position: new kakao.maps.LatLng(lat, lng),
						image: markerImage
					})
				})
			} else {
				console.log('geolocation 사용 불가능')
			}
		},
		onMapEvent (params) {
			var lat = params[0].latLng.Ha
			var lng = params[0].latLng.Ga
			console.log(`lat: ${lat}, lng: ${lng}`)
			this.displayMarker(lat, lng)
		},
		displayMarker (lat, lng) {
			var marker = new kakao.maps.Marker({
				map: this.map,
				position: new kakao.maps.LatLng(lat, lng)
			})

			marker.setPosition((lat, lng));
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
.map {
	width: 100vw;
	height: 50vh;
}
.zoomControl {
	position: absolute;
	width: 40px;
	background-color: white;
	top: 200px;
	right: 10px;
	z-index: 1;
	text-align: center;
}
.radius_border {
  border: 1px solid #919191;
  border-radius: 5px;
}
.color_919191 {
	border-color: #919191 !important;
}
</style>