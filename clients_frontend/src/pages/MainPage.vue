<template>
  <v-container>
    <div
      id="map"
      class="map-300h"
    >
    </div>

  </v-container>
</template>

<script>
export default {
  mounted () {
    var container = document.getElementById('map')
    var options = {
      center: new kakao.maps.LatLng(33.450701, 126.570667),
      level: 3
    }

    var map = new kakao.maps.Map(container, options)
  }
}
</script>

<style scoped>
.map-300h {
  width: 100%;
  height: 300px;
}
</style>
