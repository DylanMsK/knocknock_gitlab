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
			@dragend="getAddr"
			@zoom_changed="getAddr"
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
	</div>
</template>

<script>
import VueDaumMap from 'vue-daum-map'
import config from '../../../map.config';

export default {
	components: {
		VueDaumMap
	},
	data() {
		return {
			appKey: config.appKey,
			center: {lat: 37.553190, lng: 126.972759}, 
			level: 3,
			mapTypeId: VueDaumMap.MapTypeId.NORMAL,
			libraries: ['services'],
			map: null,
			curMarker: null,
			pointMarker: null,
			centerAddr: '',
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

					// 현재 위치 마커 표시
					this.map = map					
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
			// 클릭한 곳 마커 표시
			this.pointMarker = new kakao.maps.Marker({
				map: map,
				position: ''
			})
			this.searchAddrFromCoords(map.getCenter(), this.displayCenterInfo);
		},
		onMapEvent (params) {
			this.pointMarker.setPosition(params[0].latLng)
			this.searchAddrFromCoords(params[0].latLng, this.displayCenterInfo);
			console.log(params[0].latLng)
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
            // 행정동의 region_type 값은 'H' 이므로
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
		}}
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
	width: 40px;
	background-color: white;
	top: 200px;
	right: 10px;
	z-index: 1;
	text-align: center;
}
.gpsBtn {
	position: absolute;
	width: 40px;
	background-color: white;
	top: 450px;
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