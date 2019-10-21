<template>
	<div class="map_wrap">
		<div
		id="map"
		class="map-50vh"
		>
		</div>
		<!-- 위치 주소 표시 div -->
		<div class="hAddr">
		<span id="centerAddr"></span>
		</div>
		<!-- 지도 확대, 축소 컨트롤 div -->
		<div class="custom_zoomcontrol radius_border"> 
		<span onclick="zoomIn()">
			<img src="http://t1.daumcdn.net/localimg/localimages/07/mapapidoc/ico_plus.png" alt="확대" />
		</span>  
		<span onclick="zoomOut()">
			<img src="http://t1.daumcdn.net/localimg/localimages/07/mapapidoc/ico_minus.png" alt="축소" />
		</span>
		</div>
		<!-- 새로고침 버튼 div -->
		<div class="refresh radius_border">
		<span>
			<img src="https://images.vexels.com/media/users/3/131903/isolated/preview/dc1162fe4ecfe2abaccb5f7dad552d46-reload-flat-icon-by-vexels.png" alt="새로고침" />
		</span>
		</div>
	</div>
</template>

<script>
var map = function() {
  // 지도 init setting 
  var mapContainer = document.getElementById('map'), // 지도를 표시할 div 
    mapOption = {
      center: new kakao.maps.LatLng(37.566826, 126.9786567), // 지도의 중심좌표
      level: 3 // 지도의 확대 레벨
    };  
  var map = new kakao.maps.Map(mapContainer, mapOption); // 지도 생성


  // 현재 위치 확인
  if (navigator.geolocation) { // geolocation 사용할 수 있는지 확인
      navigator.geolocation.getCurrentPosition(function(position) {
          var lat = position.coords.latitude, // 위도
              lon = position.coords.longitude; // 경도
          var locPosition = new kakao.maps.LatLng(lat, lon) // 마커가 표시될 위치를 geolocation으로 얻어온 좌표로 생성
          displayMarker(locPosition); // 마커 표시
        });
  } else { // GeoLocation 사용할 수 없을때
      var locPosition = new kakao.maps.LatLng(33.450701, 126.570667)
      displayMarker(locPosition);
  }

  var imageSrc = 'http://testrottenwifi.ito.lt/bundles/itowififront/images/my-location-icon.png', // 마커이미지 주소   
  // var imageSrc = '@/assets/current_location_marker.png', // 마커이미지 주소   
    imageSize = new kakao.maps.Size(70, 70), // 마커이미지 크기
    imageOption = {offset: new kakao.maps.Point(27, 69)}; // 마커이미지 옵션. 마커의 좌표와 일치시킬 이미지 안에서의 좌표 설정.
      
  // 마커의 이미지정보를 가지고 있는 마커이미지 생성
  var markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize, imageOption),
      markerPosition = new kakao.maps.LatLng(37.54699, 127.09598); // 마커가 표시될 위치
      
  // 마커 표시
  function displayMarker(locPosition) {
      var marker = new kakao.maps.Marker({  
          map: map, 
          position: locPosition,
          image: markerImage
      }); 
  map.setCenter(locPosition); // 지도 중심좌표를 접속위치로 변경


  // 지도 확대, 축소
  var zoomInFunc = function zoomIn() {
    map.setLevel(map.getLevel() - 1);
  }
  var zoomOutFunc = function zoomOut() {
    map.setLevel(map.getLevel() + 1);
  }


  // 주소-좌표 변환
  var geocoder = new kakao.maps.services.Geocoder(); // 객체 생성
  var marker = new kakao.maps.Marker() // 클릭한 위치를 표시할 마커
  searchAddrFromCoords(map.getCenter(), displayCenterInfo); // 현재 지도 중심좌표로 주소를 검색해서 지도 하단에 표시
  // 지도를 클릭했을 때 클릭 위치 좌표에 대한 주소정보를 표시하도록 이벤트 등록
  kakao.maps.event.addListener(map, 'click', function(mouseEvent) {
    searchDetailAddrFromCoords(mouseEvent.latLng, function(result, status) {
      if (status === kakao.maps.services.Status.OK) {
        var detailAddr = !!result[0].road_address ? '<div>도로명주소 : ' + result[0].road_address.address_name + '</div>' : '';
        detailAddr += '<div>지번 주소 : ' + result[0].address.address_name + '</div>';

        marker.setPosition(mouseEvent.latLng); // 마커를 클릭한 위치에 표시
        marker.setMap(map);
      }   
    });
  });

  // 중심 좌표나 확대 수준이 변경됐을 때 지도 중심 좌표에 대한 주소 정보를 표시하도록 이벤트 등록
  kakao.maps.event.addListener(map, 'idle', function() {
    searchAddrFromCoords(map.getCenter(), displayCenterInfo);
  });

  function searchAddrFromCoords(coords, callback) {
    // 좌표로 행정동 주소 정보 요청
    geocoder.coord2RegionCode(coords.getLng(), coords.getLat(), callback);         
  }
  function searchDetailAddrFromCoords(coords, callback) {
    // 좌표로 법정동 상세 주소 정보 요청
    // 표출하진 않는데 없으면 오류남 
    geocoder.coord2Address(coords.getLng(), coords.getLat(), callback);
  }

  // 주소정보 표출하는 함수
  function displayCenterInfo(result, status) {
    if (status === kakao.maps.services.Status.OK) {
      var infoDiv = document.getElementById('centerAddr');

      for(var i = 0; i < result.length; i++) {
        // 행정동의 region_type 값은 'H' 이므로
        if (result[i].region_type === 'H') {
            infoDiv.innerHTML = result[i].address_name;
            break;
        }
      }
    }    
  }
}
}
import { mapState, mapMutations } from 'vuex'

export default {
  mounted () {
    map ()
  },
  methods: {
    zoomIn() {
      console.log(map)
      map.zoomInFunc
      // console.log(map.zoomInFunc())
    },
    zoomOut() {
      map.zoomOutFunc
    }
  }
}
</script>

<style scoped>
.map_wrap {
  position: relative;
  overflow: hidden;
  width: 100%;
  height: 50vh;
}
.map-50vh {
  width: 100%;
  height: 50vh;
}
.hAddr {
  position: absolute;
  left: 10px;
  top: 20px;
  border-radius: 2px;
  background: #fff;
  background: rgba(255,255,255,0.8);
  z-index: 1;
  padding: 5px;
}
#centerAddr {
  display: block;
  margin-top: 2px;
  font-weight: normal;
}
.bAddr {
  padding: 5px;
  text-overflow: ellipsis;
  overflow: hidden;
  white-space: nowrap;
}
.radius_border {
  border: 1px solid #919191;
  border-radius: 5px;
}
.custom_zoomcontrol {
  position: absolute;
  top: 120px;
  right: 10px;
  width: 36px;
  height: 80px;
  overflow: hidden;
  z-index: 1;
  background-color: #f5f5f5;
} 
.custom_zoomcontrol span {
  display: block;
  width: 36px;
  height: 40px;
  text-align: center;
}     
.custom_zoomcontrol img {
  width: 15px;
  height: 15px;
  margin: 10px 0 10px -2px;
  /* padding: ; */
  border: none;
}   
.custom_zoomcontrol span:first-child{
  border-bottom: 1px solid #bfbfbf;
}
.refresh {
  position: absolute;
  top: 350px;
  right: 10px;
  width: 36px;
  height: 36px;
  overflow: hidden;
  z-index: 1;
  background-color: #f5f5f5;
}
.refresh span {
  display: block;
  width: 20px;
  height: 20px;
  text-align: center;
} 
.refresh img {
  width: 20px;
  height: 20px;
  margin: 7px;
}
</style>
