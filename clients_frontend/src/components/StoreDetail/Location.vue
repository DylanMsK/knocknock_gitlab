<template>
	<div>
		<div 
			id="staticMap" 
			class="map-size"
		>
		</div>    
	</div>
</template>

<script>
var staticMap = function() {
	var markerPosition  = new kakao.maps.LatLng(37.5012272, 127.0350094); 

	var marker = {
			position: markerPosition
	};

	var staticMapContainer  = document.getElementById('staticMap'), 
			staticMapOption = { 
					center: new kakao.maps.LatLng(37.5012272, 127.0350094), 
					level: 3, 
					marker: marker 
			};    
	// 이미지 지도를 생성합니다
	var staticMap = new kakao.maps.StaticMap(staticMapContainer, staticMapOption);
}

export default {
	mounted () {
    staticMap ()
  },
}
</script>

<style scoped>
.map-size {
	width: 100%;
	height: 350px;
}
</style>